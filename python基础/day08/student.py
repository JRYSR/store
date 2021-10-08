class Student:
    __name = ""
    __age = 0

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        if "." in age:
            print("数据错误！！！")
        elif age.isdecimal() is True and 0 < int(age) < 120:
            self.__age = age
        else:
            print("数据错误！！！")

    def getage(self):
        return self.__age

    def show(self):
        print("大家好，我叫%s，今年%s岁了！"%(self.__name, self.__age))

    def compare(self, student):
        if int(self.__age) < int(student.getage()):
            print("我比同桌小{}岁！".format(int(student.getage()) - int(self.__age)))
        elif int(self.__age) > int(student.getage()):
            print("我比同桌大{}岁！".format(int(self.__age) - int(student.getage())))
        else:
            print("我和同桌一样大！")


s = Student()
s.setname(input("请输入姓名："))
s.setage(input("请输入年龄："))
s.show()

s1 = Student()
s1.setname(input("请输入姓名："))
s1.setage(input("请输入年龄："))
s1.show()

s.compare(s1)
s1.compare(s)
