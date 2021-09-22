import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
     df = pd.read_csv(event.src_path, encoding="utf-16", engine="python", error_bad_lines=False)
     print(df.)

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created

    path = "./data/"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

   

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()