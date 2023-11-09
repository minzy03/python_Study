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
     
player1 = SoccerPlayer('손흥민', 'MF', 10)
print(player1.name)
print(player1.positon)
print(player1.backNumber)