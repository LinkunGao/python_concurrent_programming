import blog_spider
import threading
import time


def single_thread():
    print("single_thread start")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread start")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    #     start
    for thread in threads:
        thread.start()

    #   waiting for end
    for thread in threads:
        thread.join()
    print("multi_thread end")

if __name__ == '__main__':
    start  = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")