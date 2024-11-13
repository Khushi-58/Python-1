def fn(n):
    if n<=2:
        return n-1
    else:
        return fn(n-1)+fn(n-2)
try:
    num=int(input("enter a number:"))
    if num>0:
        print(f'fn{(num)}={fn(num)}')
    else:
        print("input should be greater than 0")
except ValueError:
    print("try with numeric value")
