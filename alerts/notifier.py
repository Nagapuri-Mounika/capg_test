# # alerts/notifier.py
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
# from datetime import datetime
# from config import EMAIL_CONFIG
# import yagmail  # make sure it's installed with: pip install yagmail

# def send_email_alert(event_type, message):
#     yag = yagmail.SMTP(EMAIL_CONFIG["sender"], EMAIL_CONFIG["app_password"])
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     subject = f"⚠️ Alert: {event_type}"
#     body = f"{message}\n\nTimestamp: {timestamp}"

#     yag.send(to=EMAIL_CONFIG["recipient"], subject=subject, contents=body)
#     print("✅ Email alert sent.")



# def log_event(event_type, message):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_line = f"[{timestamp}] {event_type}: {message}"

#     print(log_line)  # Print it to the console

#     # Write to the log file with utf-8 encoding
#     with open("alerts.log", "a", encoding="utf-8") as f:
#         f.write(log_line + "\n")

#     # Trigger email alert for specific events like INTEGRITY_FAIL or DELETED
#     if event_type in ["INTEGRITY_FAIL", "DELETED"]:
#         send_email_alert(event_type, message)
# if __name__ == "__main__":
#     send_email_alert("TEST", "This is a test email from the file monitor system.")



# alerts/notifier.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from datetime import datetime
from config import EMAIL_CONFIG
import yagmail  # pip install yagmail

def send_email_alert(event_type, message):
    yag = yagmail.SMTP(EMAIL_CONFIG["sender"], EMAIL_CONFIG["app_password"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = f"⚠️ Alert: {event_type}"
    body = f"{message}\n\nTimestamp: {timestamp}"
    yag.send(to=EMAIL_CONFIG["recipient"], subject=subject, contents=body)
    print("✅ Email alert sent.")

def log_event(event_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {event_type}: {message}"
    print(log_line)

    with open("alerts.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

    # Send emails for ALL significant file events
    if event_type in ["INTEGRITY_FAIL", "DELETED", "CREATED", "MODIFIED"]:
        send_email_alert(event_type, message)

if __name__ == "__main__":
    send_email_alert("TEST", "This is a test email from the file monitor system.")
