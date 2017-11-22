import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np
import scipy
import scipy.stats
from scipy import stats

u,v=[],[]
e,f=[],[]
with open('user1_variables.csv') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
        u.append(float(i[0]))
        v.append(float(i[1]))

with open('user2_variables.csv') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for k in data:
        e.append(float(k[0]))
        f.append(float(k[1]))


avg_ID,avg_MT=[],[]
for i in range (0,6):
	avg_ID.append(float((u[i]+e[i])/2))
	avg_MT.append(float((v[i]+f[i])/2))

a=np.array(avg_ID)
b=np.array(avg_MT)
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
reg_line=[slope*j+intercept for j in avg_ID]
print("slope",slope)
print("intercept",intercept)
plt.figure(1)
plt.scatter(avg_ID,avg_MT,color='blue')
plt.plot(avg_ID,reg_line,'c')    
plt.xlabel('Index of Difficulty')
plt.ylabel('Movement time (milli seconds)')

x,y=[],[]
j,k=[],[]

with open('user1_variables.csv') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
        x.append(float(i[0]))
        y.append(float(i[2]))


with open('user2_variables.csv') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for m in data:
        j.append(float(m[0]))
        k.append(float(m[2]))


merge_x=[]
merge_y=[]
for q in range(0,6):
    merge_x.append((x[q]+j[q])/2)
    merge_y.append((y[q]+k[q])/2)
p=np.array(merge_x)
q=np.array(merge_y)
slope, intercept, r_value, p_value, std_err = stats.linregress(p,q)
reg_line=[slope*j+intercept for j in avg_ID]
print("slope",slope)
print("intercept",intercept)
plt.figure(2)
plt.scatter(p,q,color='blue')
plt.plot(p,reg_line,'c')
plt.xlabel('Index of Difficulty')
plt.ylabel('Throughput (bits/second)')
plt.show()
