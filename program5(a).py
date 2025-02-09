import matplotlib.pyplot as plt
#%matplotlib inline
"""age_men=[25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
plt.hist(age_men,bins=6)
plt.show()"""
"""bins=[10,20,30,40,50,60,70]
plt.hist(age_men,bins=bins,edgecolor='r')
plt.show()"""

from matplotlib import style
"""style.use("fivethirtyeight")
plt.hist(age_men,bins=10,edgecolor='y',color='g',rwidth=0.7)
plt.xlabel("age of people",fontsize=20)
plt.ylabel("number of people",fontsize=20)
plt.title("age vs number of people",fontsize=20)
plt.show()"""

age_men=[25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
age_women=[48,57,59,25,19,37,18,56,22,25,26,25,14,49,53,45,46,19,28,70,31]
plt.figure(figsize=(6,6))
style.use("ggplot")
bins=[10,20,30,40,50,60,70]
plt.hist([age_men,age_women],bins=bins,color=["blue","orange"],rwidth=0.5,label=["mens","women"])
plt.xlabel("age of people",fontsize=20)
plt.ylabel("number of people",fontsize=20)
plt.title("age vs number of people",fontsize=20)
plt.legend(loc="upper right")
plt.show()




