import platform

if platform.system() == "Windows":
    from watcher.windows_watcher import start_watch
else:
    from watcher.unix_watcher import start_watch  # <- you need to create this


#  Update this to any folder you want to monitor
path_to_monitor = "C:\\Users\\DELL\\Documents"


if __name__ == "__main__":
    path = "/Users/mounikanagapuri/Desktop/test"
    start_watch(path)

