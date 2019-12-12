# 利用集合没有重复元素的原理，将列表转换成集合后，再恢复成列表

list1 = [i for i in range(1,21)]
list2 = [x for x in range(-20,21) if x%2==0]

list3 = set(list1+list2)
list3.discard(20)
list3=list(list3)
print(list3)
