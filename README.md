# python_learning

pyc文件的生成是什么情况下生成呢：
当 import导入另一个模块的时候会生成
python3会生成 __pycache__
如何不生成编译文件呢：
1.使用 -B参数 即
python3 -B test.py
里面的包含的就不会生成pyc了

2.设置环境变量

export PYTHONDONTWRITEBYTECODE=1
1
还有一种更方便的
3. 在导入的地方写

import sys
sys.dont_write_bytecode = True
1
2
以上三种方式都可以实现不生成pyc文件。


## python多线程
多线程简单理解：一个CPU，也就是单核，将时间切成一片一片的，CPU轮着去处理一件一件事情，到了规定时间片就处理下一件事情。

### 01 显示当前线程信息的属性和方法

`python_thread.py`
```python3
# coding:utf-8
# 导入threading包
import threading
if __name__ == "__main__":
    print("当前活跃线程数量：",threading.active_count())
    print("当前所有线程具体信息展示：",threading.enumerate())
    print("当前的线程信息展示：",threading.current_thread())
```
### 02 添加线程
`python_thread.py`
```python3
#创建一个新的线程
    new_thread = threading.Thread(target=job1,name="T1")
    #启动新线程
    new_thread.start()
```
### 03 线程中的join函数
join作用：
某个线程使用join函数，此线程正在执行时，其他线程不能执行。等待这个被阻塞的线程全部执行完毕之后，方可执行。
`python_thread.py`
```python3
 new_thread = threading.Thread(target=job1,name="T1")
    #启动新线程
    new_thread.start()
    # 阻塞这个T1线程
    new_thread.join()
```
### 04 使用Queue存储线程的结果
线程的执行结果，无法通过return进行返回，使用Queue存储
`python_queue.py`
### 05 线程锁lock
```python3
def stu1():
    global lock
    lock.acquire()
    ...
    lock.release()
```
```python3
if __name__ == "__main__":
    # 篮球课名称
    course = 2
    # 创建同步锁
    lock = threading.Lock()
    T1 = threading.Thread(target = stu1, name="T1")
    T2 = threading.Thread(target = stu2, name="T2")
    T3 = threading.Thread(target = stu3, name="T3")
    T2.start()
    T1.start()
    T3.start()
```
## python多进程
目前计算机都是多核的，通俗来讲就是多个处理或者计算单元。为了加快运算速度和处理速度，我们可以将不同的任务交给多个核心进行同时处理，从而提高了运算速度和效率，多个核心同时运作就是多个进程同时进行，即为多进程。
### 01 创建进程
`process_create

