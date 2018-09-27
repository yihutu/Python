#conding:utf-8
#_author:贡金敏
#date:2018/9/20

name0 = 'aaa'
name1 = 'bbb'
name2 = 'ccc'
name3 = 'ddd'
name4 = 'eee'

names = 'aaa bbb ccc ddd eee'

#a = ['aaa','bbb','ccc','ddd','eee'] ##[]是创建列表并且赋予变量a

#增删改查
#a[] ##[]通过索引（就是下标）拿值，[]里的信息就是位置

#查 切片 []
# print(a[1:4]) ##左包括，右不包括
# print(a[1:]) ##从头取到最后
# print(a[1:-1]) ##最后一个元素的前一个，倒数第二个
# print(a[1:-1:2])
# print(a[1::2])
# print(a[3::-2])
# print(a[-2::-1])


# 增 append 与 insert（两种添加方法）
#append 把值放到列表的最后一个位置
# insert 将数据插到任何位置
# a.append('fff')
# print(a)
# a.insert(1,'fff')
# print(a)

#修改
# a[1] = 'ggg'  ##先查询定位在赋值修改
# print(a)
# a[1:2] = ['a','b'] ##多个定位，多个修改
# print(a)

#删除 remove pop del
# a.remove('bbb') ##列表内置remove
# a.remove(a[1]) ##删除内容同上
# print(a)
# b=a.pop(1) ##通过索引删除，还可以返回删除的值
# print(a)
# print(b)
# del a[0]
# print(a)
# del a  ##删除a这个对象
# print(a)

#count 统计某个元素在列表中出现的次数
# t=['to','be','or','not','to','be'].count('to')
# print(t)

#extend 添加元素
# a = ['1','2','3']
# b = ['4','5','6']
# a.extend(b)
# print(a)
# print(b)

#index
#a = ['aaa','bbb','ddd','ccc','ddd','eee']
##print(a.index('bbb'))

# first_lg_index = a.index("ddd")
# print("first_lg_index",first_lg_index)
# little_list = a[first_lg_index+1:]
# second_lg_index = little_list.index("ddd")
# print("second_lg_index",second_lg_index)
# second_lg_index_in_big_list = first_lg_index + second_lg_index +1
# print("second_lg_index_in_big_list",second_lg_index_in_big_list)
# print("second lg:",a[second_lg_index_in_big_list])

#reverse 倒序排序
# a = ['aaa','bbb','ddd','ccc','ddd','eee']
# a.reverse()
# print(a)

#sort 排序
# x = [4,6,2,1,7,9]
# x.sort(reverse=True)
# print(x)

# a = ['aaa','Ddd','bbb','ddd','Ccc','eee']
# a.sort()  ##按ascii码排序
# print(a)


a = ['aaa','Ddd','bbb','ddd','Ccc','eee']
print(a.count("ff"))
print("ff" in a) ##查询ff在不在a里



