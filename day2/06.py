# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
count = 0
while count < 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if (username == "root") and (password == "admin"):
        print("登录成功！！！")
    else:
        print("登录失败！！！")
        count = count + 1
print("系统锁定！！！")