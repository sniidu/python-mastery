import threading
import time
from concurrent.futures import Future


def parse_line(line):
    try:
        name, value = line.split("=")
        return (name, value)
    except ValueError:
        return None


def worker(x, y):
    print("About to work")
    time.sleep(15)
    print("Done")
    return x + y


def do_work(x, y, fut: Future):
    fut.set_result(worker(x, y))


if __name__ == "__main__":
    fut = Future()
    t = threading.Thread(target=do_work, args=(2, 3, fut))
    t.start()

    res = fut.result()
    print(res)

    # import threading
    #
    # t = threading.Thread(target=worker, args=(2, 3))
    # t.start()
