import os
import numpy as np
from scipy.stats import norm


path = os.path.join(os.path.dirname(__file__), 'height.txt')
xs = np.loadtxt(path)
mu = np.mean(xs)
sigma = np.std(xs)

# cdf = cumulative distribution function 즉, 주어진 확률 변수가 특정 값보다 작거나 같을 확률
p1 = norm.cdf(160, mu, sigma) # 어떤 input x가 mu sigma를 갖는 정규분포에서 160보다 작거나 같을 확률
print('p(x <= 160):', p1)

p2 = norm.cdf(180, mu, sigma) # input x가 180보다 작거나 같을 확률에서 1을 빼줌
print('p(x > 180):', 1-p2)