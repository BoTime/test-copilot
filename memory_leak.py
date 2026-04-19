from time import sleep
import resource
import sys

class Node:
    def __init__(self):
        self.ref = None
        # 50 MB of data
        self.data = bytearray(50 * 1024 * 1024)
    def __del__(self):
        pass

def rss_mb():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return rss / (1024 * 1024) if sys.platform == "darwin" else rss / 1024

def init():
    a = Node()
    b = Node()
    a.ref = b
    b.ref = a

if __name__ == "__main__":
    print(f"Before init(): {rss_mb():.1f} MB")

    init()
    
    while True:
        sleep(2)
        print(f"After init(): {rss_mb():.1f} MB")
        