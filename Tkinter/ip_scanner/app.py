import eel
import threading
import os

eel.init('web')

valid_ips = []
MAX_IP = 255
lock = threading.Lock()


# @eel.expose
def scan_ip(ip, lock):
    print(ip)
    result = os.popen("ping {0} -c 1".format(ip)).read()
    # global valid_ips
    if result.find("ttl") != -1:
        with lock:
            valid_ips.append(ip)


@eel.expose
def scan_ips(ip):
    print(ip)
    base_ip = ip[:ip.rfind(".") + 1]
    threads = []

    for i in range(1, MAX_IP):
        t = threading.Thread(target=scan_ip, args=(base_ip + str(i), lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return ", ".join(valid_ips)


try:
    eel.start('index.html', size=(400, 300), port=0)

except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit")
