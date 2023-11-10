#그래프 그리는 파이썬 라이브러리
#pip install matplotlib

#%%
import matplotlib.pyplot as plt #as 별칭 선언
#꺽은선 그래프
# plt.plot([x좌표리스트], [y좌표리스트])
plt.plot([1,2,3], [2,4,1])
plt.show()

# %%
#pip install numpy 
#수치 처리 관련 라이브러리
import numpy as np
x = np.arange(0.0, 5.0, 0.01) #0부터 5.0까지 0.01씩 값 증가
print(x)

plt.title('Test Graph')
plt.plot(x, x**2, 'r--', label='y=x**2')
plt.plot(x, 3*x, 'b', label='y=3x')

#각 축에 이름 추가
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.legend() #범례 추가
plt.grid(True) #눈금표시

#그래프 저장
plt.savefig('./testGaph.png', dpi=300) #dpi해상도
plt.show()

