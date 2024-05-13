from vip import Vip

class Singerv5(Vip):
    chairs=[]
    chairs_remove=[]
    for i in range(50):
        chairs.append(i+1)
    def __init__(self, name, surname, age, chair, singer,color):
        super().__init__(name, surname, age, chair, singer,color)

    
