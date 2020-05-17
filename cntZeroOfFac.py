import math
n = eval(input("Please enter the number to be calculated:"))
cnt = 0
fac = math.factorial(n)
while fac>0:
    cnt = cnt+1
    fac = float(fac/10)
    print(float(fac/10))
    if float(fac/10)!=int(fac/10):
        break
print("{}!={},output: {}".format(n,math.factorial(n),cnt))


# code from Zhao Jiaqi
# import math as m
# s=eval(input("Please input a positive integer: "))
# fact = m.factorial(s)
# count=0
# for a in str(fact)[::-1]:
#     if eval(a)==0:
#         count+=1
#     else :
#         break
# print("{}!={})".format(s,fact),",Output:",count)
