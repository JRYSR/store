from threading import Thread
import threading
import time

# 全局变量
sum = 500
# 为了防止厨师的打印比较的混乱，使用厨师的全局锁
# mutex = threading.Lock()

# 为了防止顾客的打印比较的混乱，使用顾客的全局锁
# mutex1 = threading.Lock()
start = time.time()  # 获取现在时间


class Consumer(Thread):
    mutex1 = threading.Lock()
    count = 0

    username = ""

    def run(self) -> None:
        # global  mutex1
        global sum
        while True:
            end = time.time()
            if end - start >= 300:
                SystemExit
            self.mutex1.acquire()  # 当执行该代码后，锁定当前人的打印的程序，其他人的打印暂且先排队，优先打印当前的程序
            if sum > 0:
                self.count = self.count + 1
                sum = sum - 1
                print(self.username, "--------------抢了1个面包！还剩", sum, "个面包！！已经买了", self.count, "个面包！")
                time.sleep(0.1)
            else:
                print(self.username, "-------------面包不足，请等待3秒钟！", end="")
                for i in range(3):
                    time.sleep(1)
                    print(".", end="")
            self.mutex1.release()  # 释放这个打印锁，让排队的其他人继续执行


class Chief(Thread):
    mutex = threading.Lock()
    username = ""
    count = 0

    def run(self) -> None:
        global sum
        while True:
            self.mutex.acquire()  # 当执行该代码后，锁定当前人的打印的程序，其他人的打印暂且先排队，优先打印当前的程序
            if sum < 500:
                sum = sum + 1
                self.count = self.count + 1
                print(self.username, "-------------造了一个面包！还剩", sum, "个面包！已经造了", self.count, "个面包！")

            else:
                print(self.username, "-----------面包篮子已满！请等待6秒.")
                for i in range(6):
                    time.sleep(1)
                    print(".", end="")
            self.mutex.release()  # 释放这个打印锁，让排队的其他人继续执行


c1 = Consumer()
c2 = Consumer()
c3 = Consumer()
c4 = Consumer()
c5 = Consumer()
p1 = Chief()
p2 = Chief()
p3 = Chief()
p4 = Chief()
p5 = Chief()
c1.username = "张三"
c2.username = "李四"
c3.username = "王五"
c4.username = "赵六"
c5.username = "田七"
p1.username = "厨师1"
p2.username = "厨师2"
p3.username = "厨师3"
p4.username = "厨师4"
p5.username = "厨师5"

c1.start()
p1.start()
c2.start()
# p2.start()
c3.start()
# p3.start()
c4.start()
# p4.start()
c5.start()
# p5.start()
