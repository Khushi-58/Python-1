m1=int(input("enter the test1 marks:"))
m2=int(input("enter the test2 marks:"))
m3=int(input("enter the test3 marks:"))
if(m1<=m2 and m1<=m3):
    avgmarks=(m2+m3)/2
elif(m2<=m1 and m2<=m3):
    avgmarks=(m1+m3)/2
else:
    (m3<=m1 and m3<=m2)
    avgmarks=(m1+m2)/2
print("Average of best two marks out of three tests marks is",avgmarks)




