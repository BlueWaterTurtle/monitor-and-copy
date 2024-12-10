import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the source and destination directories
source_dir = r"C:\Users\Public\Documents\1ststep"
destination_dir = r"C:\Users\Public\Documents\Waves"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            source_file = event.src_path
            destination_file = os.path.join(destination_dir, os.path.basename(source_file))
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {os.path.basename(source_file)}")

def monitor_folder():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=False)
    observer.start()
    print("Monitoring started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_folder()
