# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
high = 20
day = 3
night = 2
sum = 0
n = 0
while sum < high:
    n = n + 1
    sum = sum + day
    if sum < high:
        sum = sum - night
    else:
        print(n)