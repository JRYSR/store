class Cook:
    __name = ""
    __age = 0

    def setName(self, name):
        if name is not None:
            self.__name = name
        else:
            print("厨师姓名不能为空！")

    def getName(self):
        return self.__name

    def setAge(self, age):
        if age.isdecimal() and 0 < int(age) < 120:
            self.__age = age
        else:
            print("年龄必须是正整数！")

    def getAge(self):
        return self.__age

    def steamed_rice(self):
        print("{}岁的厨师{}正在蒸饭！".format(self.__age, self.__name))


class Cook1(Cook):
    def fried_dish(self):
        print("{}岁的厨师{}正在炒菜！".format(self.__age, self.__name))


class Cook2(Cook1):
    def steamed_rice(self):
        print("蒸饭！")

    def fried_dish(self):
        print("炒菜！")


c = Cook2()
c.setName(input("请输入厨师姓名："))
c.setAge(input("请输入厨师年龄："))
print("厨师的姓名是%s。" % c.getName())
print("厨师今年{}岁。".format(c.getAge()))
c.steamed_rice()
c.fried_dish()
