#接收用户输入的一个列表，如果列表中元素存在重复，则返回True，否则返回False。
ls=eval(input())
def f(l):
    return len(l)>len(set(l))
print(f(ls))
