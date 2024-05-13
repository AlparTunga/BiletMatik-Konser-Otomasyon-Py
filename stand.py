from Tickets import Tickets
class Normal(Tickets):
    ticketno=[]
    for i in range(250):
        ticketno.append(i+1)
    def __init__(self, name, surname, age, songer):
        super().__init__(name, surname, age, songer)
        
        
    def person_(self):
        #Ayaktaki dinleyicilerin sayısını arttırır.
            self.ticketno.pop()
            return self.ticketno

    def person_ticket(self):
         a=max(self.ticketno)
         return a


    def delete_person(self,bilet):
        #Bilet iptal edildiğinde ayaktakı dinleyicilerin sayısını azaltır ve boş bilet sayısını arttırır.
        if bilet not in self.ticketno:
            if bilet<=250:
                self.ticketno.append(bilet)
                self.ticketno.sort()
                return "{} nolu Bilet iptal edilmiştir".format(bilet)
        else:
            return "{} nolu  Bilet iptal edilemez".format(bilet)
        
        
        
        

