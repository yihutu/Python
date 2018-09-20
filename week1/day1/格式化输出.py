#conding:utf-8
#_author:贡金敏
#date:2018/9/18

name = input("Name:")
age = int(input("age:")) ##输出数字
job = input("job:")
salary = input("salary:")
if salary.isdigit():  #判断salary变量长得像不像数字，比如200d，‘200’
     salary = int(salary)
# else:
#     print()
#     exit("must input digit") ##退出程序

#%d只能输入数字
msg = '''
-------info of %s------
Name:%s
age:%d  
job:%s
salary:%f
you will be retired in %s years
'''%(name,name,age,job,salary,65-age)  ##括号里的变量与%s占位符一一对应
print(msg)