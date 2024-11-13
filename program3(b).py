from difflib import SequenceMatcher
str1=input("enter String1:")
str2=input("enter String2:")
sim=SequenceMatcher(None,str1,str2).ratio()
print("similarity between strings\""+str1+"\"and\""+str2+"\"is:",sim)