# 2019.11.7python学习笔记

## 目录

[文内链接使用方法](##文内链接使用方法)

[函数内全局变量](##函数内全局变量)

[lambda——匿名函数](##lambda——匿名函数)

[datetime库的使用](##datetime库的使用)

[库的引用方法](###库的引用方法)

## 文内链接使用方法

在文内用连接来实现目录跳转效果，格式如下：

```markdown
[名称](#id) #名称表示链接文字，几级标题就有几个#,id是跳转的标题名称
```

### 函数内全局变量

```python
def funs(a,b)
	global n
    c=a*b
    return c
```

此函数中n为全局变量，可以在函数外调用

### lambda——匿名函数

<函数名>=lambda<参数列表>

```python
sum=lambda(a,b):c
```

等价于

```python
def sum(a,b):
    return c
```

例子：

```python
def f(x,y):
    return x+y
print(f(10,12))
'''
f=lambda x,y:x+y
print(f(10,12))
'''
```

## datetime库的使用

datetime可以从系统中获得时间，并按照用户要求的格式输出

```python
datetime.date #日期表示类，可以表示年月日等
datetime.time #时间表示类，可以表示小时分钟秒毫秒等
datetime.datatime #日期和时间表示类，功能覆盖date和time类
datetime.timedelta #时间间隔有关的类
datetime.tzinfo #与时区有关的类
```

### 库的引用方法

```python
from datatime import datetime
```

### datetime.now()

返回一个datetime类型，表示当前的日期和时间，精确到微秒。

```python
>>> from datetime import datetime
>>> today = datetime.now()
>>> today
datetime.datetime(2016, 9, 20, 10, 29, 43, 928549)
```

### datetime.utcnow()

获得当前日期和时间对应的UTC（世界标准时间）时间对象

```python
>>> today = datetime.utcnow()
>>> today
datetime.datetime(2016, 9, 20, 2, 35, 1, 427954)
```

### 直接用datetime()构造一个日期和时间对象

返回一个datetime类型，表示指定的日期和时间，可以精确到微秒。

```python
datetime(year,month, day, hour=0, minute=0,second=0, microsecond=0)
```

例：

调用datetime()函数直接创建一个datetime对象，表示2016年9月16日22:33，32秒7微秒，执行结果如下：

```python
>>> someday = datetime(2016,9,16,22,33,32,7)
>>> someday
datetime.datetime(2016, 9, 16, 22, 33, 32, 7)
```

程序已经有了一个datetime对象，进一步可以利用这个对象的属性显示时间，为了区别datetime库名，采用上例中的someday代替生成的datetime对象

|        属性         |                             描述                             |
| :-----------------: | :----------------------------------------------------------: |
|     someday.min     |     固定返回datetime的最小时间对象，datetime(1,1,1,0,0)      |
|     someday.max     | 固定返回datetime的最大时间对象，
datetime(9999,12,31,23,59,59,999999) |
|    someday.year     |                    返回someday包含的年份                     |
|    someday.month    |                    返回someday包含的月份                     |
|     someday.day     |                    返回someday包含的日期                     |
|    someday.hour     |                    返回someday包含的小时                     |
|   someday.minute    |                    返回someday包含的分钟                     |
|   someday.second    |                    返回someday包含的秒钟                     |
| someday.microsecond |                   返回someday包含的微秒值                    |

### 时间格式化方法

| 属性                     | 描述                                         |
| ------------------------ | -------------------------------------------- |
| someday.isoformat()      | 采用ISO 8601标准显示时间                     |
| someday.isoweekday()     | 根据日期计算星期后返回1-7,对应星期一到星期日 |
| someday.strftime(format) | 根据格式化字符串format进行格式显示的方法     |

isoformat()和isoweekday()方法的使用如下：

```python
>>> someday = datetime(2016,9,16,22,33,32,7)
>>> someday.isoformat()
'2016-09-16T22:33:32.000007'
>>> someday.isoweekday()
5
```

strftime()方法是时间格式化最有效的方法，几乎可以以任何通用格式输出时间

```python
>>> someday.strftime("%Y-%m-%d %H:%M:%S")
'2016-09-16 22:33:32'
```

| 格式化字符串 |   日期/时间   |          值范围和实例          |
| :----------: | :-----------: | :----------------------------: |
|      %Y      |     年份      |     0001~9999，例如：1900      |
|      %m      |     月份      |        01~12，例如：10         |
|      %B      |     月名      | January~December，例如：April  |
|      %b      |   月名缩写    |       Jan~Dec，例如：Apr       |
|      %d      |     日期      |       01 ~ 31，例如：25        |
|      %A      |     星期      | Monday~Sunday，例如：Wednesday |
|      %a      |   星期缩写    |       Mon~Sun，例如：Wed       |
|      %H      | 小时（24h制） |       00 ~ 23，例如：12        |
|      %I      | 小时（12h制） |        01 ~ 12，例如：7        |
|      %p      |    上/下午    |        AM, PM，例如：PM        |
|      %M      |     分钟      |       00 ~ 59，例如：26        |
|      %S      |      秒       |       00 ~ 59，例如：26        |

strftime()格式化字符串的数字左侧会自动补零，上述格式也可以与print()的格式化函数一起使用

```python
>>>from datetime import datetime
>>>now = datetime.now()
>>>now.strftime("%Y-%m-%d")
'2016-09-20'
>>>now.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 20. September 2016 01:53PM'
>>>print("今天是{0:%Y}年{0:%m}月{0:%d}日".format(now))
今天是2016年09月20日
```

