from Tickets import Tickets

class Vip(Tickets):
    chairs=[]
    chairs_remove=[]
    for i in range(50):
        chairs.append(i+1)
    
    def __init__(self,name,surname,age,chair,singer,color):
        super().__init__(name,surname,age,singer)
        self.color=color
        self.chair=chair
    
    def age_controlv(self):
        if self.age>=18:
            if self.color=="Black" :
                    print(f"{self.vipprice}TL")
                    print("Alkol serbest, Ücretsiz alkol. Siyah bilet.")
        else:
            print("18 yaşından küçükler VIP bilet alamaz lütfen normal bilet almayı deneyiniz.") 
        
    def chair_control(self):
    #Koltuğun doluluğunu kontrol eder
        if self.age>=18:
            a=self.chairs.count(self.chair)
            if a==1:
                print(f"{self.chair} numaralı koltuk biletini alabilirsiniz.")
        
        
            
            
        
    def chair_delete(self):
                self.chairs.remove(self.chair)
                self.chairs_remove.append(self.chair)
        
            
    def delete_ticket(self):
    #İptal edilen biletin koltuk numarasını boş koltuklara ekler
                self.chairs_remove.remove(self.chair)
                self.chairs.append(self.chair)
           
    @classmethod
    def removechairs(cls):
    #Boş koltukları yazdırır.
        if len(cls.chairs_remove)==0:
            print("18 yaşından küçükseniz lütfen normal bilet almayı deneyiniz.") 
            print("Bütün koltuklar boş.")
        else:
            print("18 yaşından küçükseniz lütfen normal bilet almayı deneyiniz.") 
            print(f"{cls.chairs_remove} numaralı koltuklar dolu farklı bir koltuk almayı deneyiniz.")            
                
            
     


        
              
            
    