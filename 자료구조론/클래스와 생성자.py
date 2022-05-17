class Car:
    def __init__(self,color,speed = 0):
        self.color = color
        self.speed = speed
    def speedUp(self):
        self.speed +=10
    def speedDown(self):
        self.speed -=10
    def __str__(self):
        return 'color = %s, speed = %d'%(self.color,self.speed)


car1 = Car('black',0)
car2 = Car('red',120)
car3 = Car('yellow',30)
car4 = Car('blue',0)
car5 = Car('green')


print(car2.speed)
print(car3.speedUp())
print(car3.speed)
print(car2.speedDown())
print(car2.speed)
print(car2.speedDown())
print(car2.speed)


print(type(car3.color))
print(type(car3.speed))
print(car3)

## 상속
class SuperCar(Car):
    def __init__(self, colar, speed = 0, bTurbo =True):
        super().__init__(colar, speed)
        self.bTurbo = bTurbo
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
    def __str__(self):
        if self.bTurbo:
            return '[%s] [speed = %d] 터보모드' %(self.color, self.speed)
        else:
            return '[%s] [speed = %d] 일반모드' %(self.color, self.speed)

s1 = SuperCar('Gold',0,True)
s2 = SuperCar('White',0,False)

s1.speedUp()
s2.speedUp()
print('슈퍼카1:', s1)
print('슈퍼카2:', s2)
print(s2.setTurbo(),s2)
s2.speedUp()
print(s2)










