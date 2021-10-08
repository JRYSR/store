from threading import Thread
import time

basket = 0


class Cook(Thread):
    def run(self) -> None:
        global basket
        while True:
            if basket < 500:
                basket += 1
                print("篮子里现在有{}个蛋挞".format(basket))
            else:
                print("等待3秒")
                time.sleep(3)


class Consumer(Thread):
    name = ""

    def run(self) -> None:
        money = 3000
        global basket
        while True:
            if basket > 0 and money > 0:
                basket -= 1
                money -= 2
                print("篮子里现在有{}个蛋挞,顾客{}有{}元钱。".format(basket, self.name, money))
            elif basket == 0 and money > 0:
                print("等待2秒")
                time.sleep(2)
            else:
                break


cook1 = Cook()
cook2 = Cook()
cook3 = Cook()

consumer1 = Consumer()
consumer2 = Consumer()
consumer3 = Consumer()
consumer4 = Consumer()
consumer5 = Consumer()
consumer6 = Consumer()
consumer1.name = "1"
consumer2.name = "2"
consumer3.name = "3"
consumer4.name = "4"
consumer5.name = "5"
consumer6.name = "6"

cook1.start()
cook2.start()
cook3.start()

consumer1.start()
consumer2.start()
consumer3.start()
consumer4.start()
consumer5.start()
consumer6.start()
