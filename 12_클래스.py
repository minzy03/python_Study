#%%
#축구 선수 캐릭터에 대한 클래스
class SoccerPlayer :
    #생성자 함수 : 객체를 만들때 실행되는 함수
    def __init__(self, name, position, backNumber) :
        self.name = name
        self.positon = position
        self.backNumber = backNumber
    #self 클래스 자기 자신을 가리킨다
    #함수선언할때, 필드값 사용시에 self를 사용한다
    
    def changeBackNumber(self, num) :
        if 1<= num <= 25 :
            self.backNumber = num
        else :
            print('잘못된 숫자를 입력했습니다.')
            
    def __str__(self) :
        return f"이름:{self.name}, 포지션:{self.positon}, 번호{self.backNumber}"
    
    def __repr__(self) :
        #객체가 자료구조 안에 있을 때 출력될 문장
        return f"{self.name}({self.backNumber})"
     
player1 = SoccerPlayer('손흥민', 'MF', 12)
print(player1.name)
print(player1.positon)
print(player1.backNumber)
player1.changeBackNumber(10)
print(player1.backNumber)

player1.backNumber = 20 #객체의 필드값에 직접 접근해서 값 변경하는 것은 안좋음
print(player1.backNumber)
player1.changeBackNumber(50)
player1.backNumber = 50 #필드값에 대한 특정 처리할 수 없어 오류날 확률 높아짐

print(player1)

# %%
#객체 여러개 선언
names = ['메시','호날두','박지성']
poses = ['MF','DF','GK']
backNums = [10,4,6]

playerList = [SoccerPlayer(n,p,b) for n,p,b in zip(names,poses,backNums)]
print(playerList)

for p in playerList :
    if p.name == '박지성' :
        print(p)

#정렬
print(sorted(playerList, key=lambda x:x.backNumber))

# %%
#클래스 상속
#상속받은 클래스 (자식 클래스)
#부모의 필드 및 메서드를 사용가능
#pip install multipledispatch

from multipledispatch import dispatch

class Person :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
        
    def work(self) :
        print('일을 합니다.')
        
class Employee(Person) :
    def __init__(self, name, age, gender, job, id, salary) :
        super().__init__(name, age, gender) #부모의 생성자 호출
        self.job = job
        self.id = id
        self.salary = salary
    
    #부모 함수 재정의(메서드 오버라이딩)
    @dispatch()
    def work(self) :
        print(f"{self.job} 일을 합니다.")
    
    #메서드 오버로드(같은 함수 이름으로 여러개 버전을 만듦(단, 입력 매개변수가 달라야함))
    #입력 매개변수의 갯수, 타입 등이 달라야 메서드 오버로딩이 가능함.
    @dispatch(int)
    def work(self, time) :
        print(f"{time}시간 동안 {self.job} 일을 합니다.")
      
    def __str__(self) :
        return f"{self.name}({self.id})"
    
    def __repr__(self) :
        return self.__str__()
        
e1 = Employee('홍길동',30,'M','의적',3000,10)
print(e1.name)
e1.work()
print(e1)
print([e1])
e1.work(8)


# %%
class Employee(Person) :
    def __init__(self, name, age, gender, job, id, salary) :
        super().__init__(name, age, gender) #부모의 생성자 호출
        self.job = job
        self.id = id
        self.salary = salary
    
    #부모 함수 재정의(메서드 오버라이딩)
    def work(self) :
        print(f"{self.job} 일을 합니다.")
    
    #메서드 오버로드(같은 함수 이름으로 여러개 버전을 만듦(단, 입력 매개변수가 달라야함))
    #입력 매개변수의 갯수, 타입 등이 달라야 메서드 오버로딩이 가능함.
    def work(self, time) :
        print(f"{time}시간 동안 {self.job} 일을 합니다.")
      
    def __str__(self) :
        return f"{self.name}({self.id})"
    
    def __repr__(self) :
        return self.__str__()
    
    #객체끼리 비교연산 특수펑션
    def __hash__(self) :
        return hash(self.id)
    
    def __eq__(self, other) :
        return self.id == other.id
    #객체끼리 == 항등연산 동작시, hash코드로 한번 비교후, __eq__함수로 비교
    
    def __len__(self) :
        return len(self.name)
    
e1 = Employee('홍길동',30,'M','의적',3000,10)
e2 = Employee('홍길동',30,'M','의적',3500,10)
e3 = Employee('임꺽정',44,'M','의적',3000,10)
print(e1)
print(e1==e2)
print(e1==e3)

e_set = set()
e_set.add(e1)
e_set.add(e2)
e_set.add(e3)
print(e_set)

print(len(e1))

# %%
#소수 판별
inNum = int(input("소수 판별을 위한 숫자 입력 > "))
for i in range(2, inNum) :
    if inNum % i == 0 :
        #소수가 아님
        print("소수가 아닙니다.")
        break
else :
    #for문이 정상적으로 모두 실행되었을때
    print("소수입니다.") 