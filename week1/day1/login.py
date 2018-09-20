#conding:utf-8
#_author:贡金敏
#date:2018/9/18

# for i in range(3):
#     print("loop:",i)


# for a in range(1,101):
#     if a % 2 == 1:
#         print("loop:",a)


# for a in range(1,101,2): #2步长
#     print("loop:",a)


# for i in range(101):  ##打印1~100，但不打印50~70之间的数
#     if i < 50 or i > 70:
#         print(i)



# _user = 'xiaoming'
# _passwd = 'abc123'
# passed_authentication = False #假，不成立
# for i in range(3):
#     username = input("name:")
#     password = input("password:")
#     if _user == username and _passwd == password:
#         print("welcome %s loging...." % _user)
#         passed_authentication =True #真，成立
#         break #跳出，中断
#     else:
#         print("invalid username or password!")
# if not passed_authentication: #只有条件在true的情况下，条件成立
#     print("登录错误次数太多")




_user = 'xiaoming'
_passwd = 'abc123'
for i in range(3):    ##for后面可以加else但是不可以加elif
    username = input("name:")
    password = input("password:")
    if _user == username and _passwd == password:
        print("welcome %s loging...." % _user)
        break #跳出，中断
    else:
        print("invalid username or password!")
else:
    print("登录错误次数太多")

















