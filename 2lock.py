# https://python-scripts.com/synchronization-between-threads ссылка про синхронизацию потоков в python
import threading
import time

a = 5
b = 5
a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1calc():
    global a
    global b

    print('thread 1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread 1 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5
    print('Thread 1 releasing both locks')
    a_lock.release()
    b_lock.release()


def thread2calc():
    global a
    global b

    print('thread 2 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    print('Thread 2 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('Thread 2 releasing both locks')
    a_lock.release()
    b_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1calc)
    t1.start()
    t2 = threading.Thread(target=thread2calc)
    t2.start()
