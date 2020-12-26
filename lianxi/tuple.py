# -*-coding:UTF-8 -*-

# 元祖：是无序       工作中，2维可以解决很多问题；看几个括号就是几维
          #  取值时一定要心中有沟壑
# 定义
userinfo=()
userinfo1=(1,'张飞','小郡',20,100000,None)#一维    插入，更新、批量删除，查出一行数据也叫一维
userinfo2=(
    (1,'张飞','小郡',20,100000,None),
    (2,'刘备','长安',28,1000,'甘夫人'),
    (3,'关羽','谢良',25,2000,None))#二维

# 访问
# 正、反、切片
userinfo1=(1,'张飞','小郡',20,100000,None)
print(userinfo1[1])#正
print(userinfo1[-4])#反
print(userinfo1[0:3])#从0开始切到3但是包含3    切片   

# 幺蛾子
# 1、如果是头或尾，可以不写
print(userinfo1[:3])

# 2、可以混合
print(userinfo1[2:-3])
#左边定好以后，一定是向右取（右值），左切一定是空值



# 遍历
userinfo1=(1,'张飞','小郡',20,100000,None)
print(userinfo1[0])
print(userinfo1[1])
print(userinfo1[2])
print(userinfo1[3])
print(userinfo1[4])
print(userinfo1[5])



#预备知识
for i in range(6):
    print(i)
    
    
#改造
for i in range(6):
    print(userinfo1[i])

# 2次改造（最终方案）
#一维遍历
for i in range(len(userinfo1)):
    print(len(userinfo1[i]))


userinfo2=(
    (1,'张飞','小郡',20,100000,None),
    (2,'刘备','长安',28,1000,'甘夫人'),
    (3,'关羽','谢良',25,2000,None))

print(userinfo2[1][1])

print(userinfo2[0][1])

#二维遍历

for i in range(len(userinfo2)):
    for j in range(len(userinfo[i])):#注意这里的写法
        print(userinfo2[i][j])









# 列表








# 字典
























