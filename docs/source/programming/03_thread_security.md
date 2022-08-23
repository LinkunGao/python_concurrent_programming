# Thread Security

## 线程安全概念介绍
- 安全：线程安全指的是某个函数，函数库在多线程环境中被调用时，能够正确地处理多个线程之间的共享变量，使程序功能正确完成。
- 不安全：由于线程的执行随时会发生切换，就造成了不可预料的结果，出现线程不安全。
## Lock 用于解决线程安全问题

- 用法一：try-finally 模式
```python
import threading
lock = threading.Lock()
lock.acquire()

try:
    # do something here
finally:
    lock.release()
```
- 用法二：with 模式
```python
import threading

lock = threading.Lock()
with lock:
    # do something here
```

## 实例代码演示问题以及解决方案