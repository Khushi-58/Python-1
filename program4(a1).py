import matplotlib.pyplot as plt
import numpy as np
categories=["0-10","10-20","20-30","30-40","40-50"]
values1=[55,48,25,68,90]
values2=[65,38,35,58,80]
width=0.4
p=np.arange(len(categories))
p1=[j+width for j in p]
plt.xlabel("overs",fontsize=15)
plt.bar(p,values1,width,color="yellow",label="player1")
plt.bar(p1,values1,width,color="red",label="player2")
plt.legend
plt.xticks(p+width/2,categories)
plt.title("bar plot showing runs scored in an ODI match")
plt.show()