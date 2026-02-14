import threading
import time

def run_on_thread(func):
    """
    Run a function in a separate thread and show a loading message until done.
    """
    def wrapper(*args, **kwargs):

        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

        # simple spinner animation
        spinner = ["|", "/", "-", "\\"]
        i = 0
        while thread.is_alive():
            print(f"\rLoading... {spinner[i % len(spinner)]}", end="")
            time.sleep(0.2)
            i += 1

        thread.join()
        print("\r✅ Done!            ")

    return wrapper
