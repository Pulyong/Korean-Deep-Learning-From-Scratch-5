# fit
어떤 데이터의 분포를 정규분포라고 가정한다면, 우리는 데이터를 이용하여 실제 데이터 분포를 근사하는(approximation) 모델을 만들 수 있습니다.  
이때 모델은 $\mu , \sigma$ 파라미터를 갖는 정규분포 모델입니다.

사람의 키에 대한 데이터가 존재할 때, 해당 데이터를 바탕으로 평균과 분산을 구할 수 있습니다.  
이 평균과 분산을 모델의 파라미터로 이용하여 실제 데이터 분포에 근사하는 간단한 정규분포 모델을 만들 수 있습니다.

$$P_{data}(x) \approx N(\mu , \sigma)$$

### Plot
![Figure_1](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/caf203ad-75d8-4a0f-a8b6-c1a6b50f1b9a)

# generate
어떤 데이터의 분포를 잘 근사한 모델이 있다면 해당 분포를 바탕으로 새로운 데이터를 생성해낼 수 있습니다.  
결국 Generative model의 목표는 data 분포를 잘 근사하는 모델을 만들고 그 모델을 이용해서 새로운 data를 생성해내는 것 입니다.  
본 예시에서는 간단한 정규분포 모델을 통해서 새로운 height에 대한 데이터 x를 생성 할 수 있습니다.

### Plot
![Figure_2](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/b5ead5a3-f067-47a2-a119-74a7baee4004)

# hist
height.txt 파일의 히스토그램을 plot합니다. data의 분포를 확인할 수 있습니다.

### Plot
![Figure_3](https://github.com/oreilly-japan/deep-learning-from-scratch-5/assets/76218918/5ff5e394-9af4-4997-83c3-4e9341a99404)

# prob
cdf를 이용하여 정규분포에서 확률변수 X가 특정 값보다 같거나 작을 확률을 확인 할 수 있습니다.  
cdf는 cumulative distribution function의 약자로 주어진 확률 변수가 특정 값보다 작거나 같은 확률을 나타냅니다.  
$$F_X(x) = P_X(X \leq x)$$