
class Tickets:
    
    def __init__(self,name,surname,age,singer):
        self.name=name
        self.surname=surname
        self.age=age
        self.singer=singer
        self.discount=0.30
        self.price=200
        self.vipprice=1500
        
        
        

    def age_control(self):
          if self.age<=18:
                    return " Alkol yasak Kırmızı bilet"+" İndirimli Ücret:"+f"{ self.price - self.price * self.discount}TL"
                    
          elif self.age >18:
              
                return " Alkol serbest. Yeşil bilet"
    # Bileti alacak kişinin yaşının girişe ve alkol almaya uygun olup olmadığını kontrol eder.
    
      
    

