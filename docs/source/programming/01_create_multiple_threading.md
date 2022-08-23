# Method of creating multiple threading

1. prepare a function
```python
def my_func(a,b):
    do_craw(a,b)

def do_craw(a,b):
    pass
```
2. 怎样创建一个线程
```python
import threading
t = threading.Thread(target=my_func,args=(100,200))
```
3. 启动线程
```python
t.start()
```
4. 等待结束
```python
t.join()
```