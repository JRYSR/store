# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长）
# 行为（打字，打游戏，看视频）
class Computer:
    __size = 0
    __price = 0.0
    __cpu_type = ""
    __memory = ""
    __time = ""

    def setsize(self, size):
        if size > 0:
            self.__size = size
        else:
            print("数据错误！！！")

    def getsize(self):
        return self.__size

    def setprice(self, price):
        if price > 0:
            self.__price = price
        else:
            print("数据错误！！！")

    def getprice(self):
        return self.__price

    def setcpu(self, cpu):
        self.__cpu_type = cpu

    def getcpu(self):
        return self.__cpu_type

    def setmemory(self, memory):
        self.__memory = memory

    def getmemory(self):
        return self.__memory

    def settime(self, time):
        if time > 0:
            self.__time = time
        else:
            print("数据错误！！！")

    def gettime(self):
        return self.__time

    def write(self):
        print("这台尺寸为{}英寸、售价为{}元、CPU型号为{}、内存为{}、待机时长为{}小时的电脑可以用来打字。"
              .format(self.__size, self.__price, self.__cpu_type, self.__memory, self.__time))

    def play(self):
        print("这台尺寸为{}英寸、售价为{}元、CPU型号为{}、内存为{}、待机时长为{}小时的电脑可以用来打游戏。"
              .format(self.__size, self.__price, self.__cpu_type, self.__memory, self.__time))

    def watch(self):
        print("这台尺寸为{}英寸、售价为{}元、CPU型号为{}、内存为{}、待机时长为{}小时的电脑可以用来看视频。"
              .format(self.__size, self.__price, self.__cpu_type, self.__memory, self.__time))


pc = Computer()
pc.setsize(15.6)
pc.setprice(6599)
pc.setcpu("AMD 2700")
pc.setmemory("金士顿2*4GB")
pc.settime(4)
pc.write()
pc.play()
pc.watch()

