# coding:utf-8
import threading
import time
def stu1():
    global lock
    lock.acquire()
    print("stu1 start to select course")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu1 success, now the remaining places are: %d" % course)
    else:
        time.sleep(2)
        print("stu1 unsuccess, now the remaining place is zero,please choose others")
    lock.release()

def stu2():
    global lock
    lock.acquire()
    print("stu2 start to select course")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu2 success, now the remaining places are: %d" % course)
    else:
        time.sleep(2)
        print("stu2 unsuccess, now the remaining place is zero,please choose others")
    lock.release()

def stu3():
    global lock
    lock.acquire()
    print("stu3 start to select course")
    global course
    if course > 0:
        course -= 1
        time.sleep(2)
        print("stu3 success, now the remaining places are: %d" % course)
    else:
        time.sleep(2)
        print("stu3 unsuccess, now the remaining place is zero,please choose others")
    lock.release()

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
