def bin2Dec(val):
    return int(val,2)
def oct2Hex(val):
    dval=int(val,8)
    return hex(dval)
try:
    num1=input("enter a binary number:")
    print(bin2Dec(num1))
except ValueError:
    print("invalid literal in input with base 2")
try:
    num2=input("enter octal number:")
    print(oct2Hex(num2))
except ValueError:
    print("invalid literal in input with base 8")