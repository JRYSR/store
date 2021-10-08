class Glass:
    __height = 0
    __volume = 0.0  # 容积
    __color = ""
    __material = ""

    def set_height(self, height):
        if height < 0:
            print("高度错误！！！")
        else:
            self.__height = height

    def get_height(self):
        return self.__height

    def set_volume(self, volume):
        if volume < 0.0:
            print("容积数值错误！！！")
        else:
            self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_material(self, material):
        self.__material = material

    def get_material(self):
        return self.__material

    def show(self):
        print("这是一个高度为{}厘米、容积为{}毫升、颜色是{}、材质是{}的水杯。".format(self.__height, self.__volume,
                                                           self.__color, self.__material))


g = Glass()
g.set_height(17)
g.set_volume(800)
g.set_color("black")
g.set_material("玻璃")
g.show()
