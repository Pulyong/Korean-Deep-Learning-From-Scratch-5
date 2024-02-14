import os
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__),'height.txt') 
'''
os.path.dirname(__file__)은 현재 script가 돌아가는 .py파일의 폴더 경로를 반환 
파일이 /home/user/example/fit.py경로에 위치해있다면
os.path.dirname(__file__)는 /home/user/example 경로를 반환
'''

xs = np.loadtxt(path)

mu = np.mean(xs)
sigma = np.std(xs)

# normal distribution
def normal(x, mu=0, sigma=1):
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    return y
x = np.linspace(150, 190, 1000)
y = normal(x, mu, sigma)

# plot
plt.hist(xs, bins='auto', density=True,label='Real data distribution')
plt.plot(x, y,label='Modeling data distribution')
plt.xlabel('Height(cm)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()