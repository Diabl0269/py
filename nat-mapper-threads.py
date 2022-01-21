import math
import os
import threading
from functions import get_ip

MAX_IP = 255
valid_ips = []
lock = threading.Lock()


def ping_ips(ip, lock):
    res = os.popen("ping {0} -c 1".format(ip)).read()
    if res.find("ttl") != -1:
        with lock:
            valid_ips.append(ip)
            print("{0} is valid".format(ip))


def scan_ips():
    own_ip = get_ip()
    threads = []
    base_ip = own_ip[:own_ip.rfind(".") + 1]

    for i in range(1, MAX_IP):
        t = threading.Thread(target=ping_ips, args=(base_ip + str(i), lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Valid ips are: {0}".format(valid_ips))


if __name__ == "__main__":
    scan_ips()
