# Thread Pool Accelerate

## Web服务的架构以及特点
![](../_static/threadpool2.jpg)
## 使用线程池ThreadPoolExecutor加速
使用线程池ThreadPoolExecutor的好处：
1. 方便的将磁盘文件，数据库，远程API的IO调用并发执行
2. 线程池的线程数目不会无限创建（导致系统挂掉），具有防御功能
## 代码用Flask实现Web服务并实现加速