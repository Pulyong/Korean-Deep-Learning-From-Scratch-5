# norm_dist
Normal Distribution, Gaussian Distribution이라고 불리는 정규분포의 수식을 코딩하고 plot합니다.  
단변량 정규분포에 대해서만 적용 가능한 코드입니다.

단변량 정규분포식은 다음과 같습니다.
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}}\exp(-\frac{(x-\mu)^2}{2\sigma ^2})$$

$\mu$와 $\sigma$는 정규분포의 파라미터인 평균과 표준편차이고, $x$는 input값 입니다.

### $\mu = 0, \sigma = 1$인 정규분포
![Figure_1](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/7a0b358f-6ff5-42b1-985a-8e0c94873891)


정규분포 공식 유도는 다음 사이트에서 확인할 수 있습니다.  
https://angeloyeo.github.io/2020/09/14/normal_distribution_derivation.html

# norm_param
정규분포의 파라미터 $\mu$와 $\sigma$가 바뀔 때 정규분포가 어떻게 변하는지 볼 수 있습니다.  
$\mu$가 바뀌면 분포가 좌우로 이동하고(단변량 정규분포에서), $\sigma$가 바뀌면 분포가 뾰족해지거나 smooth해집니다.

### $\mu$에 따른 정규분포 ($\sigma$는 1로 고정)
![norm_param1](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/9482f886-ce4f-4698-b381-2925eb9bee96)
### $\sigma$에 따른 정규분포 ($\mu$는 0으로 고정)
![norm_param2](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/1e98e257-38ed-4381-9848-ea4a6963d04a)


# sample_avg
0 ~ 1에서 Uniform한 확률을 갖는 균등분포에서 N개를 sampling한 다음 N개의 평균을 구하는 것을 10000번 반복 한 후 10000개의 값에 대한 histogram을 plot합니다.

N이 커질수록 중심극한정리에 의해 histogram은 정규분포에 근사합니다.

### N=1일 때
![1](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/1cec46ba-720c-47fb-a3f4-f1d86a1bd3fa)

### N=10일 때
![10](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/439acfb9-bef8-464b-9b6d-df941f08c206)

### N=100일 때
![100](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/8a7411b4-95ee-4b1e-afda-878831167835)


중심극한 정리는 다음 사이트에서 확인할 수 있습니다.  
https://angeloyeo.github.io/2020/09/15/CLT_meaning.html  
https://angeloyeo.github.io/2020/01/10/CLT_proof.html

# sample_sum
0 ~ 1에서 Uniform한 확률을 갖는 균등분포에서 N개를 sampling한 다음 N개의 합을 구하는 것을 10000번 반복 한 후 10000개의 값에 대한 histogram을 plot합니다.  
**sample_avg**에서는 N개의 mean을 구했지만 여기서는 N개의 sum을 구합니다.  

$x \sim U(0,1)$이기 때문에 N개의 x에 대한 sum은 0~N 사이의 값을 갖게 됩니다.uniform 분포이기 때문에 평균은 중간인 N/2의 값을 갖습니다.  
![Figure_1](https://github.com/Pulyong/Korean-Deep-Learning-From-Scratch-5/assets/76218918/829930be-a9a9-443e-833c-a900f19cd736)
