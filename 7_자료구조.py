# 7.자료구조.py
# (1) 리스트 list 
# 기호 : [] 
# 특징 : 자료의 순서 0, 인덱스를 통해 값 접근 및 수정
# 독특한 문법 : 리스트컴프리헨션 

# (2) 튜플 tuple 
# 기호 : () 
# 특징 : 리스트와 유사하지만, 자료 수정 및 삭제가 불가능해서 상수로 활용
# (3) 집합 set 
# 기호 : {} 
# 특징 : 중복을 허용하지 않는 자료구조, 자료의 순서 x, 집합 연산이 가능(합집합, 교집합, 차집합)
# (4) 딕셔너리 dict 
# 기호 : {k:v} 
# 특징 : 키를 통해 값 접근 가능, 자료의 순서 x 

# 자료구조와 반복문
# (1) 리스트, 튜플, 셋
# numList1 - 크기가 같은 경우
# numList2
# for n1,n2 in zip(numList1, numList2) :
#     print(n1,n2)

# (2) 딕셔너리
# for k,v in itemDic.items() :
#    print(k,v)

# 집합
#%%
#(1) 리스트
#데이터의 순서가 있고, 인덱스를 통해 값 접근이
#가능한 자료구조

#리스트 컴프리헨션 (list comprehension)
#기존 리스트를 이용해 새로운 리스트를 만들때 사용
#리스트와 for문을 한 줄에 사용할 수 있는 장점을 가짐

# 0~9까지 숫자 리스트
numList = [i for i in range(10)]
print(numList)


# 0~90까지 10의 배수가 담긴 리스트
numList = [i*10 for i in range(10)]
print(numList)

# 0~9까지 짝수만 담긴 리스트
# 값을 필터링 for문 뒤에 if문 사용
evenList = [i for i in range(10) if i%2==0]
print(evenList)

evenList = []
for i in range(10) :
    if i%2==0 :
        evenList.append(i)
print(evenList)
 
#짝수 1, 홀수 0인 리스트
# 조건에 따라 값을 바꾸고 싶을 때 사용
result = [1 if i%2==0 else 0 for i in range(10)]
print(result)

result = []
for i in range(10) :
    result.append(1 if i%2==0 else 0)
print(result)

#알파벳 a~z까지 list
#alphaList = ['a', 'b', 'c', ....]
#ord() : 문자의 아스키코드값 정수값 얻음
alphaList = [(ord('a')+i) for i in range(26)] 
print(alphaList)

#chr() : 아스키코드값 -> 문자
alphaList = [chr(ord('a')+i) for i in range(26)] 
print(alphaList)

#중첩 반복문(구구단 출력)
guguList = [(i,j,i*j) for i in range(2,10) for j in range(1, 10)]
print(guguList)

guguList = []
for i in range(2, 10) :
    for j in range(1, 10) :
        guguList.append([i,j,i*j])
print(guguList)

#기존 리스트를 활용한 방법
#이름의 성만 가져오기
names = ['홍길동', '김현수', '강하늘']
sungs = [n[0] for n in names]
print(sungs)

#리스트의 값 바꾸기
numStr = ['1', '2', '3', '4']
#numStr = [int(n) for n in numStr]
print(numStr)
numStr = list(map(int, numStr))
print(numStr)

def getCircleArea(r) :
    return r**2*3.14
numList = [1,2,3]
numArea = list(map(int, numStr))
numArea = list(map(getCircleArea, map(float, numStr)))
print(numArea)

numArea = [getCircleArea(int(n)) for n in numStr]
print(numArea)

#--------------------------------------------------------
#%%
#튜플
#리스트와 유사하지만, 데이터의 변경을 혀용하지 않는 자료구조
#상수로 활용함

tu = (1,2,3)
print(tu[0], tu[:2])

tu += (4,5,6)
print(tu)

tu *= 2 
print(tu)

print(len(tu)) #튜플 요소의 개수
# tu[0] = 3 #! 오류 : 값 수정 안됨

# t1 = (i for i in range(i))
#리스트를 튜플로 형변환
l1 = [1,2,3]
t1 = tuple(l1)
print(t1)

#%%
# 셋 (SET) : 데이터의 중복을 허용하지 않고, 순서가 없는 자료구조
# 집합 연산을 지원함
numList = [1,1,1,2,2,3]
s1 = set(numList)
print(s1)
s2 = {1,2,3,3,3}
print(s2)
s3 = {i for i in numList}
print(s3)

#집합 값 추가
s1.add(4)
print(s1) 

#집합 값 여러개 추가
s1.update([7,8,9])
s1.update({7,8,9})
s1.update((7,8,9))
#s1.update(7,8,9) #오류
print(s1)

#값 제거
s1.remove(9)
print(s1)

#집합 연산
fruit1 = {'사과','딸기','포도'}
fruit2 = {'배','딸기','귤'}
#1) 합집합
fruit_all = fruit1 | fruit2
print(fruit_all)

#2) 교집합
fruit_inter = fruit1 & fruit2
print(fruit_inter)

#3) 차집합
fruit_diff1 = fruit1 - fruit2 #fruit1원소에서 fruit2와 공통된 원소 제거
fruit_diff2 = fruit2 - fruit1 #fruit2원소에서 fruit1와 공통된 원소 제거
print(fruit_diff1)
print(fruit_diff2)

#%%
#딕셔너리
#key, value로 이루어진 자료구조, 자료의 순서가 없음
#기호 : {key:val}, dict()

#선언
person = {'name':'홍길동', 'age':30, 'birth':'02-12'}
print(person)

#키를 통한 값 참조
print(person['name'])
print(person['age'])
print(person['birth'])

person2 = dict() #딕셔너리 객체 선언, 초기화된 상태 key, value 는 지정이 안되어 있음
person2['name'] = '임꺽정'
person2['age'] = 50
person2['birth'] = '08-27'
print(person2)

#get() 함수를 통한 값 접근
#key값이 없는 경우 초기값 지정 가능
# person['address'] #! 오류
addr = person.get('address', '대한민국')
age = person.get('age', -1)
print(addr, age)
#딕셔너리를 get()함수를 통해서 값을 오류없이 안정적으로 가져올 수 있다.

#값 수정 : 리스트 처럼 값 수정 가능 
person['age'] = 40
print(person)

#key-value 쌍 삭제
del person['birth']
print(person)

#모든 요소 삭제
person.clear()
print(person)

#키값 리스트
print(list(person2.keys()))
#밸류값 리스트
print(list(person2.values()))
#키,밸류를 쌍으로 리스트
print(list(person2.items()))

#딕셔너리를 반복문 처리
for k,v in person2.items() :
    print(k,v)

print('-'*10)
for k in person2.keys() :
    print(k, person2[k])

#키 및 값 검색
#키 검색
print('name' in person2)
print('address' in person2)
#값 검색
print('임꺽정' in person2.values())
print('홍길동' in person2.values())


# %%
#딕셔너리 예제
members = dict()
members['id1'] = ['홍길동', 30, '대전광역시']
members['id2'] = ['임꺽정', 40, '대전광역시']
members['id3'] = ['김하나', 25, '서울특별시']
members['id4'] = ['강현수', 60, '부산광역시']

#1) 대전에 거주하는 회원만 출력하시오.
for k,v in members.items() :
    #조건문
    #v[2] 주소
    if '대전' in v[2] :
        print(k,v)

#2) 등록된 회원들의 평균 나이값을 구하시오.
totalAge = 0
for v in members.values() :
    totalAge += v[1]
print(f'평균나이 > {totalAge/len(members)}')

#리스트컴프리헨션
avg_age = sum([v[1] for v in members.values()]) / len(members)
print(f'평균나이 > {avg_age}')


# %%
#숙제 : 과일의 개수 세기
#각 과일명을 key, 각 과일의 개수를 value로 하는 딕셔너리를 만드시오.
#출력 {'사과':3, '딸기':1, '포도':2, '배':1}
#hint : 각 과일의 개수를 얻을때는 count()
#유니크한 과일 이름을 얻을 때 set()
#fruit.count('사과') #사과의 개수를 얻을 수 있음

fruit = ['사과','사과','사과','딸기','포도','포도','배']
fruit1 = set(fruit)
print(fruit1)
fruit1 = dict()
fruit1['배'] = fruit.count('배')
fruit1['사과'] = fruit.count('사과')
fruit1['딸기'] = fruit.count('딸기')
fruit1['포도'] = fruit.count('포도')
print(fruit1)

fruit_set = set(fruit)
fruit_dict = dict()
print(fruit_set)
for f in fruit_set :
    print(f, fruit.count(f))
    fruit_dict[f] = fruit.count(f)
print(fruit_dict)

#개수가 가장 많은 과일을 출력하시오.
#(1) 가장 많은 과일의 개수 
#최대값(MAX)
numList = [3,4,5,6,1]
print(max(numList))

maxNum = numList[0]
for n in numList :
    if n > maxNum :
        maxNum = n
print(maxNum)

#최소값(MIN)
minNum = numList[0]
for n in numList :
    if n < minNum :
        minNum = n
print(minNum)
print(min(numList))
    
#fruit_dict에서 개수가 가장 많은 과일을 출력하시오.
#단, 과일의 가장 많은 개수가 여러개 라면, 모두 출력하세요.

max_num = max(fruit_dict.values())
for k,v in fruit_dict.items() :
    if v == max_num :
        print(k,v)
        
#------------------------------------------




