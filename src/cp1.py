from multiprocessing import Process, Queue
import time
import random
import os


def consumer(q):
    while 1:
        res = q.get()
        if res is None:  # 收到信号就结束
            break
        time.sleep(random.randint(2, 5))
        print('\033[31m%s消耗了%s\033[0m' % (os.getpid(), res))


def producer(q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = "食物%s" % i
        q.put(res)
        print('\033[32m%s生产了%s\033[0m' % (os.getpid(), res))


if __name__ == '__main__':
    q = Queue()
    p_one = Process(target=producer, args=(q,))
    p_two = Process(target=producer, args=(q,))
    p_thr = Process(target=producer, args=(q,))

    c_one = Process(target=consumer, args=(q,))
    c_two = Process(target=consumer, args=(q,))
    c_thr = Process(target=consumer, args=(q,))
    c_fou = Process(target=consumer, args=(q,))


    p_one.start()
    p_two.start()
    p_thr.start()

    c_one.start()
    c_two.start()
    c_thr.start()
    c_fou.start()

    p_one.join()
    p_two.join()
    p_thr.join()

    q.put(None)  # 四次发送结束信号
    q.put(None)
    q.put(None)
    q.put(None)

    print("主进程结束")