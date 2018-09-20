#conding:utf-8
#_author:贡金敏
#date:2018/9/18

#无限循环

_user = 'xiaoming'
_passwd = 'abc123'
counter = 0
while counter <3:
    name = input("Name:")
    password = input("Password:")
    if name == _user and password == _passwd:
        print("welcome %s loging..." % _user)
        break
    else:
        print("invalid username or password!")
    counter += 1
    if counter == 3 :
        keep = input("还想玩吗？[y/n]")
        if keep == "y":
            counter = 0
else:
    print("登错错误次数太多")
