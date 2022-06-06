import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('stockholm_tmp.dat',)

ms = np.unique(data[:, 1])
print(ms)
srs = []
for i in ms:
    x = data[np.where(data[:, 1] == i)]
    
    srs.append(np.sum(x[:, 3])/len(x))
    plt.hist(range(1, len(srs)+1), bins=len(srs), weights=srs, rwidth=0.9, color='teal') # tan

plt.xlabel("Месяц")
plt.ylabel("Температура")


ms = 4.
april_data = data[np.where(data[:, 1] == ms)]
years = np.unique(april_data[:, 0])
ans = []
for i in years:plt.hist(range(1, len(srs)+1), bins=len(srs), weights=srs, rwidth=0.9, color='teal') # tan

plt.xlabel("Месяц")
plt.ylabel("Температура")
    x = data[np.where((data[:, 0] == i))]
    ans.append(np.sum(x[:, 3])/len(x))
print(*ans, sep='\n')


plt.figure(figsize=(15, 5))
plt.plot(years, ans, color='tan')
plt.xlabel("Год")
plt.ylabel("Т-па")


plt.show()
