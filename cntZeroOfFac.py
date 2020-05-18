# import math
# n = eval(input("Please enter the number to be calculated:"))#接收数据
# cnt = 1
# fac = math.factorial(n) #计算阶乘
# while fac>0: #循环和一个其实没有实际用处的循环条件
#     fac = (fac / 10) #每次循环都把阶乘除以10（相当于抹掉小数点后一1位）
#     # if float(fac/10)!=int(fac/10):#当除以10，有小数点和不能有小数点两种结果不等时，跳出循环
#     #     break
#     print(fac)
#     if fac%10==0:#假如阶乘能被10整除（除10）没有余数，计数器加1
#         cnt = cnt +1
#     else:
#         break
# print("{}!={},output: {}".format(n,math.factorial(n),cnt))


import math
n = eval(input("Please enter the number to be calculated:"))
fac = math.factorial(n)
cnt = 0
for a in str(fac)[::-1]:
  if eval(a)==0:
    cnt+=1
  else:
    break
print("{}!={},output: {}".format(n,math.factorial(n),cnt))