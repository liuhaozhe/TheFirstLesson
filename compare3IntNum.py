a = eval(input("Please enter the first number to be sort:"))
b = eval(input("Please enter the second number to be sort:"))
c = eval(input("Please enter the third number to be sort:"))

arr = [a,b,c]
arr.sort();
for i in range(len(arr)):
    print("large to small:",arr[len(arr)-i-1],"  samll to largr:",arr[i])

