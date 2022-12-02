class Person :
    def __init__(self, age, name, sex) :
        self.age = age
        self.name = name
        self.sex = sex  

    def introduce(self) :
        print(f"{self.age}살 {self.name}입니다.")

class Car :
    
    def __init__(self) :
        print("자동차 생성")
    
p1 = Person(20, "홍길동", "남") # 복사본 하나 생성
p2 = Person(22, "홍길순", "여") # 복사본 하나 생성

p1.introduce()
p2.introduce()

# df = DataFrame("파일경로", 옵션1, 옵션2)
