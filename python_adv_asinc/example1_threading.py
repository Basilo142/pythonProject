import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print('Value: {}'.format(result))


params = {'finished': 2 ** 26}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('Result_1')
task.start()
task.join()
print('Time: {}'.format(time.time()-started_at))

started_at = time.time()
print('Result_2')
handler(**params)
print('Time: {}'.format(time.time()-started_at))
