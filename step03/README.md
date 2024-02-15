# plot_dataset
height_weight.txt 파일에 있는 data를 산점도(scatter)로 plot합니다. 
해당 txt 파일의 각 row는 25000개의 관측치, col은 Height, Weight feature로 구성되어있습니다.  
shape = (25000, 2)  

### Plot
![Figure_1](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/a72c6c1e-90e8-4ab1-a3a8-f184aee93efb)  


# plot_3d
변수가 2개이면 3차원 상에 plot을 해야합니다.  
X,Y라는 변수가 주어졌을 때 $Z=X^2 + Y^2$을 표현하는 함수를 plot합니다.  

이 때
```
X = np.array([[-2, -1, 0, 1, 2],
              [-2, -1, 0, 1, 2],
              [-2, -1, 0, 1, 2],
              [-2, -1, 0, 1, 2],
              [-2, -1, 0, 1, 2]])
Y = np.array([[-2, -2, -2, -2, -2],
              [-1, -1, -1, -1, -1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2]])
```
를 사용해도 좋지만,
```
x = y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(x, y)

'''
X -> [-2.0, -1.9 ... 1.8, 1.9]
     [-2.0, -1.9 ... 1.8, 1.9]

Y -> [-2.0, -2.0 ... -2.0, -2.0]
     [-1.9, -1.9 ... -1.9, -1.9]
'''
```
를 사용하면 meshgrid함수를 통해 (-2,-2)부터 (1.9,1.9) 사각형 안에 들어있는 모든 grid에 대한 좌표값을 X,Y에 return합니다. 형식은 위의 리스트와 같습니다.

$Z = X^2 + Y^2$은 2차함수 형태의 convex function으로 그려집니다.

### Plot
![Figure_1](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/f679e950-2b5d-4ec9-a773-55d4bba5d272)

이 함수를 3차원이 아닌 contour함수를 통해 2차원 등고선 형태로도 나타낼 수 있습니다.

### Plot
![Figure_2](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/f18ea2a4-776e-48f3-9f3a-056ccf9af358)


# plot_norm
변수가 2개일 때의 다변량 정규분포를 plot합니다.  
다변량 정규분포식은 다음과 같습니다.  
$$p(x;\mu , \sigma)=\frac{1}{\sqrt{(2\pi)^n{\vert \Sigma \vert }}}\exp{(-\frac{(x-\mu)^T\Sigma^{-1}(x-\mu)}{2})}$$

코드로 작성하면 다음과 같습니다.
```
def multivariate_normal(x, mu, cov):
    det = np.linalg.det(cov) # Sigma의 determinent
    inv = np.linalg.inv(cov) # Sigma의 inverse
    D = len(x) # 공식에서의 n 값
    z = 1 / np.sqrt((2 * np.pi) ** D * det)
    y = z * np.exp((x - mu).T @ inv @ (x - mu) / -2.0)
    return y
```

$\mu = [0.5, -0.2]$  
$\Sigma = \begin{bmatrix}
2.0 & 0.3 \\
0.3 & 0.5 \\
\end{bmatrix}$  

일 때,  
-5 ~ 5까지의 X,Y좌표를 바탕으로 함수 값 Z를 구해 plot 합니다.
```
xs = ys = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(xs, ys)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        x = np.array([X[i, j], Y[i, j]])
        Z[i, j] = multivariate_normal(x, mu, cov)
```

### Plot
![Figure_1](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/18f94943-5354-4abd-8efa-bc85dc6a1af3)

covariance가 존재하기 때문에 타원형의 분포가 나온 것을 알 수 있습니다.

# mle
MLE는 Maximum Likelihood Estimation의 약자로 Likelihood를 Maximize시키는 Parameter를 찾는 방법론 입니다.  
자세한 설명은 https://angeloyeo.github.io/2020/07/17/MLE.html 사이트를 참고하시면 됩니다.

간단히 말하면 data들이 존재할 때 어떤 분포에 대해서 해당 data들이 sampling될 수 있는 가능도(likelihood)를 가장 크게하는 파라미터 $\theta$를 찾는 것 입니다.  
정규분포를 예를 들면, 어떤 data들이 존재할 때 해당 data가 나올 가능도를 가장 크게 하는 $\mu , \sigma$를 찾는 방식입니다.

![image](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/0c20dd06-39fa-4f69-beac-4534ead6fcf4)  
위의 그림에서 data [1,4,5,6,9]는 주황색 분포에서 sampling 되었다는게 더 타당할 것입니다. 이 때 주황색 분포가 정규분포라고 하면 주황색 정규 분포의 $\mu , \sigma$를 MLE를 통해 찾을 수 있습니다.

간단하게 분포를 파라미터 $\theta = [\mu, \sigma]$에 대해서 미분하여 0이 되는 지점을 찾아 MLE를 이용할 수 있습니다.
$$ \frac{\partial logP(x|\theta)}{\partial \theta} = \sum_{i=1}^n\frac{\partial}{\partial \theta}logP(x|\theta) = 0$$

해당 예제에서는 간단하게 data의 mean, variance를 이용해서 정규분포의 파라미터를 추정합니다. 이 방법 또한 파라미터를 추정하는 방법 중 하나이지만 MLE보다 신뢰성이 낮습니다. 하지만 간단하게 파라미터를 추정할 수 있습니다.  

```
# Maximum Likelihood Estimation(MLE)
mu = np.mean(xs, axis=0)
cov = np.cov(xs, rowvar=False) # if rowvar -> 각각의 row가 feature else -> 각각의 col이 feature

```

### Plot
![Figure_1](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/db8a851a-ff15-4464-bf2a-16acf539af5b)