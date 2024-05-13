from vip import Vip
#Vip bilet için sanatçı class'ı
class Singerv4(Vip):
    chairs=[]
    chairs_remove=[]
    for i in range(50):
        chairs.append(i+1)
    def __init__(self, name, surname, age, chair, singer,color):
        super().__init__(name, surname, age, chair, singer,color)

    
