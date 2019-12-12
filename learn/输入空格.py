'''
stopword = '' # 输入停止符
str = ''
for line in iter(raw_input, stopword): # 输入为空行，表示输入结束
  str += line + '\n'

# print (str)  #测试用
'''


#原代码中没有输入，并且在Python3中raw_input被input代替
l=[]
l.append(input())
stopword = '' # 输入停止符
str = ''
for line in iter(input, stopword): # 输入为空行，表示输入结束
  str += line + '\n'
print(l)
# print (str)  #测试用
