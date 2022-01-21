import threading
import time

startTime = time.time()


def counter(number):
    for num in range(number):
        print(num)


threads = []

for i in range(5):
    counter(100000)
    # t = threading.Thread(target=counter, args=(100000,))
    # threads.append(t)
    # t.start()

for t in threads:
    t.join()

print(time.time() - startTime)
