#A몬스터와 A속성이 만나면 "A+진화"
#A몬스터와 B속성이 만나면 "A는 B의 진화 돌이 아닙니다."
#poket = "피카츄"
#poket = "파이리"
#poket = "꼬부기"

#stone = "전기의 돌"
#stone = "불의 돌"
#stone = "물의 돌"
class base:
    def __init__(self,poket,type,stone): #불러오기/포켓몬,포켓몬타입,돌,진화 후
        self.poket = poket #진화 전 포켓몬
        self.element = type #포켓몬 타입
        print("%s 속성을 가진 %s가 등장했다."%(self.element,self.poket))
        self.stone = stone #돌
        print("필요한 건 %s"%(self.stone))
class upgrade:  # 포켓몬 속성과 돌의 속성이 같으면 출력 #포켓몬 + 포켓몬 ->안됨  # 포켓몬 + 돌 ->됨 or 안됨
    def zinha(self,other):
        def poketmon(self):
            return self.poket,self.stone
        def Raicu(self):
            print("%s는 %s와 합쳐져 라이츄로 진화되었습니다."%(self.poket,self.stone))
        def Rizamong(self):
            print("%s는 %s와 합쳐져 리자몽으로 진화되었습니다." % (self.poket, self.stone))
        def Gebucking(self):
            print("%s는 %s와 합쳐져 거북왕으로 진화되었습니다." % (self.poket, self.stone))
        def Pp(self):
            if self.poket in ("피카츄","파이리","꼬부기") and other.poket in ("피카츄","파이리","꼬부기"):
                print("%s와 %s는 결합 할 수 없습니다."%(self.poket,other.poket))
        def Ps(self):
            if self.poket in ("피카츄","파이리","꼬부기") and self.stone in ("전기의 돌","불의 돌","물의 돌"):
                print("%s와 %s는 결합 할 수 없습니다." % (self.poket, other.stone))