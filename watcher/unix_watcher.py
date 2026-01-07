# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time

# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         print(f"[MODIFIED] {event.src_path}")

#     def on_created(self, event):
#         print(f"[CREATED] {event.src_path}")

#     def on_deleted(self, event):
#         print(f"[DELETED] {event.src_path}")

# def start_watch(path):
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path=path, recursive=True)
#     observer.start()
#     print(f"Monitoring started on '{path}'")

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()








# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time
# import os
# import sys

# # Add alerts folder to import path so we can use notifier
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))

# from notifier import log_event  # Import the logging & alert function

# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         message = f"{event.src_path} was modified."
#         print(f"[MODIFIED] {event.src_path}")
#         log_event("MODIFIED", message)

#     def on_created(self, event):
#         message = f"{event.src_path} was created."
#         print(f"[CREATED] {event.src_path}")
#         log_event("CREATED", message)

#     def on_deleted(self, event):
#         message = f"{event.src_path} was deleted."
#         print(f"[DELETED] {event.src_path}")
#         log_event("DELETED", message)  # This will trigger email alert

# def start_watch(path):
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path=path, recursive=True)
#     observer.start()
#     print(f"📡 Monitoring started on '{path}'...")

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#         print("🛑 Monitoring stopped.")
#     observer.join()



# unix_watcher.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
# Add this at the top
import sys
import os

# Fix the import path so it can find 'alerts/notifier.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))

from notifier import log_event


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            message = f"{event.src_path} was modified."
            log_event("MODIFIED", message)

    def on_created(self, event):
        if not event.is_directory:
            message = f"{event.src_path} was created."
            log_event("CREATED", message)

    def on_deleted(self, event):
        if not event.is_directory:
            message = f"{event.src_path} was deleted."
            log_event("DELETED", message)

def start_watch(path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"📡 Monitoring started on '{path}'...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Monitoring stopped.")
    observer.join()

if __name__ == "__main__":
    watch_path = "/Users/mounikanagapuri/Desktop/test"  # Change to your directory
    start_watch(watch_path)
