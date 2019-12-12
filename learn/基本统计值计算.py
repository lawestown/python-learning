# CalStatisticsV1
print("请输入数字(Enter确认/两次Enter退出),且至少需要输入两个数字。")

# 从键盘获取数字
def getNum():
    list= []
    while True :
        list.append(input())
        t=str(list[-1])
        if not len(t):
            del list[-1]
            break
    for i in range(len(list)):
        list[i]=eval(list[i])
    return list

# 求输入数据的个数
def count(numbers):
    return len(numbers)

# 求和
def summation(numbers):
    return sum(numbers)

# 计算平均值
def mean(numbers):
    return sum(numbers)/len(numbers)
# 计算方差
def dev(numbers, mean):
    sum2=0.0
    N=len(numbers)
    for i in range(N):
        sum2+=(numbers[i]-mean)**2
    var=sum2/N
    return var
 # 计算中位数
def median(numbers):
    numbers.sort()
    half=len(numbers)//2
    return (numbers[half]+numbers[~half])/2

n = getNum()
m=median(n)
print('个数:{}, 和:{}, 平均值:{:.1f}, 方差:{:.1f}, 中位数:{}.'.format(count(n),summation(n),mean(n),dev(n, mean(n)),median(n)))




