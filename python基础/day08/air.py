class Air:
    __brand = ""
    __price = 0.0
    __time = 0

    def setbrand(self, brand):
        if brand is not None:
            self.__brand = brand
        else:
            print("品牌名不能为空！！！")

    def getbrand(self):
        return self.__brand

    def setprice(self, price):
        if "." in price:
            date = price.split(".")
            if date[0].isdecimal() is True and date[1].isdecimal() is True:
                self.__price = price
            else:
                print("售价必须是数值！！！")
        elif price.isdecimal():
            self.__price = price
        else:
            print("售价必须是数值！！！")

    def getprice(self):
        return self.__price

    def settime(self, time):
        if time.isdecimal():
            self.__price = time
        else:
            print("售价必须是整数值！！！")

    def turn_on(self):
        print("空调开机了………")

    def turn_off(self):
        print("空调将在{}分钟后自动关机！！！".format(self.__time))

    def show(self):
        print("{}空调，售价仅为{}元！！！".format(self.__brand, self.__price))


a = Air()
a.turn_on()
a.setbrand(input("请输入空调品牌："))
a.setprice(input("请输入空调售价："))
a.show()
a.settime(input("请输入关机时间在多少分钟以后："))
a.turn_off()
