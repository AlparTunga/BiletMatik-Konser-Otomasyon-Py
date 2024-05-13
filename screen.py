from Sanatci1stand import Singer
from sanatci1vip import Singerv
from sanatci2stand import Singer2
from sanatci2vip import Singerv2
from sanatci3stand import Singer3
from sanatci3vip import Singerv3
from sanatci4stand import Singer4
from sanatci4vip import Singerv4
from sanatci5stand import Singer5
from sanatci5vip import Singerv5
from vip import Vip
#Bilet alma, iptal etme gibi işlemlerin yapıldığı arayüz class'ı
class Screen:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def singer1():
        print("1-Bilet al\n2-Bilet iptal")
        choice=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
        if choice==1:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("Almak istediğiniz bilet türünü giriniz:"))
            
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Manga"
                person=Singer(name,surname,age,singer)
                person.age_control()
                person.person_ticket()
                person.person_()
            
            elif choice2==2:
                Singerv.removechairs()
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Manga"
                person=Singerv(name,surname,age,chair,singer,"Black")
                person.age_controlv()
                person.chair_control()
                person.chair_delete()
                
        elif choice==2:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("İptal etmek istediğiniz bilet türünü giriniz:"))
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Manga"
                person=Singer(name,surname,age,singer)
                person.delete_person()
                
            elif choice2==2:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Manga"
                person=Singerv(name,surname,age,chair,singer,"Black")
                person.delete_ticket()

    @staticmethod
    def singer2():
        print("1-Bilet al\n2-Bilet iptal")
        choice=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
        if choice==1:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("Almak istediğiniz bilet türünü giriniz:"))
            
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="The Weekend"
                person=Singer2(name,surname,age,singer)
                person.age_control()
                person.person_ticket()
                person.person_()
            
            elif choice2==2:
                Singerv2.removechairs()
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="The Weekend"
                person=Singerv2(name,surname,age,chair,singer,"Black")
                person.age_controlv()
                person.chair_control()
                person.chair_delete()
                
        elif choice==2:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("İptal etmek istediğiniz bilet türünü giriniz:"))
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="The Weekend"
                person=Singer2(name,surname,age,singer)
                person.delete_person()
                
            elif choice2==2:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="The Weekend"
                person=Singerv2(name,surname,age,chair,singer,"Black")
                person.delete_ticket()

    @staticmethod
    def singer3():
        print("1-Bilet al\n2-Bilet iptal")
        choice=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
        if choice==1:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("Almak istediğiniz bilet türünü giriniz:"))
            
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Fatma Turgut"
                person=Singer3(name,surname,age,singer)
                person.age_control()
                person.person_ticket()
                person.person_()
            
            elif choice2==2:
                Singerv3.removechairs()
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Fatma Turgut"
                person=Singerv3(name,surname,age,chair,singer,"Black")
                person.age_controlv()
                person.chair_control()
                person.chair_delete()
                
        elif choice==2:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("İptal etmek istediğiniz bilet türünü giriniz:"))
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Fatma Turgut"
                person=Singer3(name,surname,age,singer)
                person.delete_person()
                
            elif choice2==2:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Fatma Turgut"
                person=Singerv3(name,surname,age,chair,singer,"Black")
                person.delete_ticket()

    @staticmethod
    def singer4():
        print("1-Bilet al\n2-Bilet iptal")
        choice=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
        if choice==1:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("Almak istediğiniz bilet türünü giriniz:"))
            
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Ezhel"
                person=Singer4(name,surname,age,singer)
                person.age_control()
                person.person_ticket()
                person.person_()
            
            elif choice2==2:
                Singer4.removechairs()
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Ezhel"
                person=Singerv4(name,surname,age,chair,singer,"Black")
                person.age_controlv()
                person.chair_control()
                person.chair_delete()
            
                
        elif choice==2:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("İptal etmek istediğiniz bilet türünü giriniz:"))
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="Ezhel"
                person=Singer4(name,surname,age,singer)
                person.delete_person()
                
            elif choice2==2:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="Ezhel"
                person=Singerv4(name,surname,age,chair,singer,"Black")
                person.delete_ticket()

    @staticmethod
    def singer5():
        print("1-Bilet al\n2-Bilet iptal")
        choice=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
        if choice==1:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("Almak istediğiniz bilet türünü giriniz:"))
            
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="LilZey"
                person=Singer5(name,surname,age,singer)
                person.age_control()
                person.person_ticket()
                person.person_()
            
            elif choice2==2:
                Singer5.removechairs()
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="LilZey"
                person=Singerv5(name,surname,age,chair,singer,"Black")
                person.age_controlv()
                person.chair_control()
                person.chair_delete()
                
        elif choice==2:
            print("1-Ayakta Bilet\n2-Vip bilet")
            choice2=int(input("İptal etmek istediğiniz bilet türünü giriniz:"))
            if choice2==1:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                singer="LilZey"
                person=Singer5(name,surname,age,singer)
                person.delete_person()
                
            elif choice2==2:
                name=input("Adınız:")
                surname=(input("Soyadınız:"))
                age=int(input("Yaşınız:"))
                chair=int(input("koltuk no:"))
                singer="LilZey"
                person=Singerv5(name,surname,age,chair,singer,"Black")
                person.delete_ticket()