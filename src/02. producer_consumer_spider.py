import queue
import blog_spider
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        if url_queue.qsize()==0:
            break
        url = url_queue.get()
        if url is None:
            html_queue.put(None)
            continue
        html = blog_spider.craw(url)
        html_queue.put(html)
        # print(threading.current_thread().name, f"craw{url}", "url_queue.size=", url_queue.qsize())
        # time.sleep(random.randint(1, 2))
        print("----------->1")


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        if html is None:
            print("finish consumer")
            break
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        # print(threading.current_thread().name, f"results.size", len(results), "html_queue.size=", html_queue.qsize())
        # time.sleep(random.randint(1, 2))
        print("------------->2")


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    threads = []

    for url in blog_spider.urls:
        url_queue.put(url)
    url_queue.put(None)
    url_queue.put(None)
    url_queue.put(None)
    url_queue.put(None)

    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        threads.append(t)
        t.start()

    fout = open("02.data.txt", "w")
    for idx in range(4):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse{idx}")
        t.start()

    # 无法结束
    for thread in threads:
        thread.join()

