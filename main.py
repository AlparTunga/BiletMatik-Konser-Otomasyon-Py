import sys
from PyQt5 import QtWidgets
from setui import Ui_MainWindow
from sanatci1vip import Singerv
from Sanatci1stand import Singer
from sanatci2vip import Singerv2
from sanatci2stand import Singer2
from sanatci3vip import Singerv3
from sanatci3stand import Singer3
from sanatci4vip import Singerv4
from sanatci5vip import Singerv5
from sanatci5stand import Singer5
from sanatci4stand import Singer4

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.satin_al.clicked.connect(self.satin_al)
        self.ui.sanatci_bir_radio.toggled.connect(self.Tiklama)
        self.ui.sanatci_iki.toggled.connect(self.Tiklama)
        self.ui.sanatci_uc_radio.toggled.connect(self.Tiklama)
        self.ui.sanatci_dort_radio.toggled.connect(self.Tiklama)
        self.ui.sanatci_bes_radio.toggled.connect(self.Tiklama)
        self.ui.vip_radio.toggled.connect(self.Tiklama)
        self.ui.normal_radio.toggled.connect(self.Tiklama)
        self.ui.iptal_et.clicked.connect(self.Iptal_et)
            
       
        
    def satin_al(self):
        name=self.ui.name_line.text()
        surname=self.ui.surname_line.text()
        age=(self.ui.age_line.text())
        vip_chair=self.ui.vip_koltuk.text()
        sanatci_bir=self.ui.sanatci_bir_radio.text()
        sanatci_iki=self.ui.sanatci_iki.text()
        sanatci_uc=self.ui.sanatci_uc_radio.text()
        sanatci_dort=self.ui.sanatci_dort_radio.text()
        sanatci_bes=self.ui.sanatci_bes_radio.text()
        bilet_vip=self.ui.vip_radio.text()
        bilet_normal=self.ui.normal_radio.text()
        sanatci=" "
        bilet=" "
        b=self.ui.sanatcilar_groupbax.findChildren(QtWidgets.QRadioButton)
        tur=self.ui.bilet_groupbox.findChildren(QtWidgets.QRadioButton)
        for i in b:
            if i.isChecked():
                sanatci=i.text()
        for a in tur:
            if a.isChecked():
                bilet=a.text()
        try:
            age=int(age)
            vip_chair=int(vip_chair)
            if sanatci==sanatci_bir:
                if bilet==bilet_vip:
                    if age>=18:
                        
                        musteri=Singerv(name,surname,age,vip_chair,sanatci,"Black")
                        if vip_chair in Singerv.chairs:
                            musteri.chair_delete()
                            a=Singerv.chairs_remove
                            ucret=musteri.vipprice
                            self.ui.lbl_uyari.setText("{} numaralı koltuk satıldı Alkol ücretsiz Siyah bilet".format(str(vip_chair)))
                            self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                            self.ui.dolu_vip_lbl.setText("Dolu koltıklar:{}".format (str(a)))
                        else:
                            self.ui.lbl_uyari.setText("{} numaralı koltuk doludur satilamaz".format(str(vip_chair)))                                
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler vip bilet alamaz")
                if bilet==bilet_normal:
                    if age>=13:
                        musteri=Singer(name,surname,age,sanatci_bir)
                        bilet_no=musteri.person_ticket()
                        ucret=musteri.price
                        a=musteri.age_control()
                        musteri.person_()
                        self.ui.lbl_uyari.setText("{} Numaralı bilet satildi {}".format(bilet_no,a))
                        self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bilet alamaz")
                        
            if sanatci==sanatci_iki:
                if bilet==bilet_vip:
                    if age>=18:   
                        musteri=Singerv2(name,surname,age,vip_chair,sanatci,"Black")
                        if vip_chair in Singerv2.chairs:
                            musteri.chair_delete()
                            a=Singerv2.chairs_remove
                            ucret=musteri.vipprice
                            self.ui.lbl_uyari.setText("{} numaralı koltuk satıldı Alkol ücretsiz Siyah bilet".format(str(vip_chair)))
                            self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                            self.ui.dolu_vip_lbl.setText("Dolu koltıklar:{}".format (str(a)))
                        else:
                            self.ui.lbl_uyari.setText("{} numaralı koltuk doludur satilamaz".format(str(vip_chair)))                                
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler vip bilet alamaz")
                if bilet==bilet_normal:
                    if age>=13:
                        musteri=Singer2(name,surname,age,sanatci_bir)
                        bilet_no=musteri.person_ticket()
                        ucret=musteri.price
                        a=musteri.age_control()
                        musteri.person_()
                        self.ui.lbl_uyari.setText("{} Numaralı bilet satildi {}".format(bilet_no,a))
                        self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bilet alamaz")
            if sanatci==sanatci_uc:
                if bilet==bilet_vip:
                    if age>=18:   
                        musteri=Singerv3(name,surname,age,vip_chair,sanatci,"Black")
                        if vip_chair in Singerv3.chairs:
                            musteri.chair_delete()
                            ucret=musteri.vipprice
                            a=Singerv3.chairs_remove
                            self.ui.lbl_uyari.setText("{} numaralı koltuk satıldı Alkol ücretsiz Siyah bilet".format(str(vip_chair)))
                            self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                            self.ui.dolu_vip_lbl.setText("Dolu koltıklar:{}".format (str(a)))
                        else:
                            self.ui.lbl_uyari.setText("{} numaralı koltuk doludur satilamaz".format(str(vip_chair)))                                
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler vip bilet alamaz")
                if bilet==bilet_normal:
                    if age>=13:
                        musteri=Singer3(name,surname,age,sanatci_bir)
                        bilet_no=musteri.person_ticket()
                        ucret=musteri.price
                        a=musteri.age_control()
                        musteri.person_()
                        self.ui.lbl_uyari.setText("{} Numaralı bilet satildi {}".format(bilet_no,a))
                        self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bilet alamaz")
            if sanatci==sanatci_dort:
                if bilet==bilet_vip:
                    if age>=18:    
                        musteri=Singerv4(name,surname,age,vip_chair,sanatci,"Black")
                        if vip_chair in Singerv4.chairs:
                            musteri.chair_delete()
                            a=Singerv4.chairs_remove
                            ucret=musteri.vipprice
                            self.ui.lbl_uyari.setText("{} numaralı koltuk satıldı Alkol ücretsiz Siyah bilet".format(str(vip_chair)))
                            self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                            self.ui.dolu_vip_lbl.setText("Dolu koltıklar:{}".format (str(a)))
                        else:
                            self.ui.lbl_uyari.setText("{} numaralı koltuk doludur satilamaz".format(str(vip_chair)))                                
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler vip bilet alamaz")
                if bilet==bilet_normal:
                    if age>=13:
                        musteri=Singer4(name,surname,age,sanatci_bir)
                        bilet_no=musteri.person_ticket()
                        ucret=musteri.price
                        a=musteri.age_control()
                        musteri.person_()
                        self.ui.lbl_uyari.setText("{} Numaralı bilet satildi {}".format(bilet_no,a))
                        self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bilet alamaz")
            if sanatci==sanatci_bes:
                if bilet==bilet_vip:
                    if age>=18:   
                        musteri=Singerv5(name,surname,age,vip_chair,sanatci,"Black")
                        if vip_chair in Singerv5.chairs:
                            musteri.chair_delete()
                            ucret=musteri.vipprice
                            a=Singerv5.chairs_remove
                            self.ui.lbl_uyari.setText("{} numaralı koltuk satıldı Alkol ücretsiz Siyah bilet".format(str(vip_chair)))
                            self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                            self.ui.dolu_vip_lbl.setText("Dolu koltıklar:{}".format (str(a)))
                            
                        else:
                            self.ui.lbl_uyari.setText("{} numaralı koltuk doludur satilamaz".format(str(vip_chair)))                                
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler vip bilet alamaz")
                if bilet==bilet_normal:
                    if age>=13:
                        musteri=Singer5(name,surname,age,sanatci_bir)
                        bilet_no=musteri.person_ticket()
                        ucret=musteri.price
                        a=musteri.age_control()
                        musteri.person_()
                        self.ui.lbl_uyari.setText("{} Numaralı bilet satildi {}".format(bilet_no,a))
                        self.ui.ucret_lbl.setText("Ücret: {} TL".format(ucret))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bilet alamaz")
        except ValueError:
            self.ui.lbl_uyari.setText("Lütfen doğru bilgi giriniz")

    def Tiklama(self):
        sanatci_bir=self.ui.sanatci_bir_radio.text()
        sanatci_iki=self.ui.sanatci_iki.text()
        sanatci_uc=self.ui.sanatci_uc_radio.text()
        sanatci_dort=self.ui.sanatci_dort_radio.text()
        sanatci_bes=self.ui.sanatci_bes_radio.text()
        bilet_vip=self.ui.vip_radio.text()
        normal=self.ui.normal_radio.text()
        item=self.ui.sanatcilar_groupbax.findChildren(QtWidgets.QRadioButton)
        items=self.ui.bilet_groupbox.findChildren(QtWidgets.QRadioButton)
        sanatci=" "
        bilet=" "
        for rb in item:
            if rb.isChecked():
                sanatci=rb.text()
        for cb in items:
            if cb.isChecked():
                bilet=cb.text()
        if sanatci==sanatci_bir:
            a=Singerv.chairs_remove
            if bilet==bilet_vip:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:{}".format(str(a)))
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
            elif bilet==normal:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:")
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
                
        elif sanatci==sanatci_iki:
            a=Singerv2.chairs_remove
            if bilet==bilet_vip:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:{}".format(str(a)))
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
            elif bilet==normal:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:")
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
        elif sanatci==sanatci_uc:
            a=Singerv3.chairs_remove
            if bilet==bilet_vip:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:{}".format(str(a)))
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
            elif bilet==normal:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:")
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
        elif sanatci==sanatci_dort:
            a=Singerv4.chairs_remove
            if bilet==bilet_vip:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:{}".format(str(a)))
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
            elif bilet==normal:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:")
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
        elif sanatci==sanatci_bes:
            a=Singerv5.chairs_remove
            if bilet==bilet_vip:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:{}".format(str(a)))
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
            elif bilet==normal:
                self.ui.dolu_vip_lbl.setText("Dolu Koltuklar:")
                self.ui.ucret_lbl.setText("Ücret:")
                self.ui.lbl_uyari.setText(" ")
    def Iptal_et(self):
        name=self.ui.name_line.text()
        surname=self.ui.surname_line.text()
        age=(self.ui.age_line.text())
        vip_chair=self.ui.vip_koltuk.text()
        sanatci_bir=self.ui.sanatci_bir_radio.text()
        sanatci_iki=self.ui.sanatci_iki.text()
        sanatci_uc=self.ui.sanatci_uc_radio.text()
        sanatci_dort=self.ui.sanatci_dort_radio.text()
        sanatci_bes=self.ui.sanatci_bes_radio.text()
        bilet_vip=self.ui.vip_radio.text()
        bilet_normal=self.ui.normal_radio.text()
        normal_chair=self.ui.koltuk_iptal_txt.text()
        sanatci=" "
        bilet=" "
        b=self.ui.sanatcilar_groupbax.findChildren(QtWidgets.QRadioButton)
        tur=self.ui.bilet_groupbox.findChildren(QtWidgets.QRadioButton)
        for i in b:
            if i.isChecked():
                sanatci=i.text()
        for a in tur:
            if a.isChecked():
                bilet=a.text()
        try:
            age=int(age)
            vip_chair=int(vip_chair)
            if sanatci==sanatci_bir:
                if bilet==bilet_vip:
                    if age>=18:
                        musteri=Singerv(name,surname,age,vip_chair,sanatci_bir,"Black")
                        if vip_chair in Singerv.chairs_remove:
                            musteri.delete_ticket()
                            self.ui.lbl_uyari.setText("Bilet iptal edildi")
                        else:
                            self.ui.lbl_uyari.setText("Bilet iptal edilemez")
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler bu işlemi gerçekleştiremez")
                elif bilet==bilet_normal:
                    if age>13:
                            normal_chair=int(normal_chair)
                            musteri=Singer(name,surname,age,sanatci_bir)
                            b=musteri.delete_person(normal_chair)
                            self.ui.lbl_uyari.setText("{}".format(b))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bu işlemi gerçekleştiremez")
            elif sanatci==sanatci_iki:
                if bilet==bilet_vip:
                    if age>=18:
                        musteri=Singerv2(name,surname,age,vip_chair,sanatci_bir,"Black")
                        if vip_chair in Singerv2.chairs_remove:
                            musteri.delete_ticket()
                            self.ui.lbl_uyari.setText("Bilet iptal edildi")
                        else:
                            self.ui.lbl_uyari.setText("Bilet iptal edilemez")
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler bu İşlemi gerçekleştiremez")
                elif bilet==bilet_normal:
                    if age>13:
                            normal_chair=int(normal_chair)
                            musteri=Singer2(name,surname,age,sanatci_bir)
                            b=musteri.delete_person(normal_chair)
                            self.ui.lbl_uyari.setText("{}".format(b))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bu işlemi gerçekleştiremez")
            if sanatci==sanatci_uc:
                if bilet==bilet_vip:
                    if age>=18:
                        musteri=Singerv3(name,surname,age,vip_chair,sanatci_bir,"Black")
                        if vip_chair in Singerv3.chairs_remove:
                            musteri.delete_ticket()
                            self.ui.lbl_uyari.setText("Bilet iptal edildi")
                        else:
                            self.ui.lbl_uyari.setText("Bilet iptal edilemez")
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler bu İşlemi gerçekleştiremez")
                elif bilet==bilet_normal:
                    if age>13:
                            normal_chair=int(normal_chair)
                            musteri=Singer3(name,surname,age,sanatci_bir)
                            b=musteri.delete_person(normal_chair)
                            self.ui.lbl_uyari.setText("{}".format(b))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bu işlemi gerçekleştiremez")
            if sanatci==sanatci_dort:
                if bilet==bilet_vip:
                    if age>=18:
                        musteri=Singerv4(name,surname,age,vip_chair,sanatci_bir,"Black")
                        if vip_chair in Singerv4.chairs_remove:
                            musteri.delete_ticket()
                            self.ui.lbl_uyari.setText("Bilet iptal edildi")
                        else:
                            self.ui.lbl_uyari.setText("Bilet iptal edilemez")
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler bu İşlemi gerçekleştiremez")
                elif bilet==bilet_normal:
                    if age>13:
                            normal_chair=int(normal_chair)
                            musteri=Singer4(name,surname,age,sanatci_bir)
                            b=musteri.delete_person(normal_chair)
                            self.ui.lbl_uyari.setText("{}".format(b))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bu işlemi gerçekleştiremez")                
            if sanatci==sanatci_bes:
                if bilet==bilet_vip:
                    if age>=18:
                        musteri=Singerv5(name,surname,age,vip_chair,sanatci_bir,"Black")
                        if vip_chair in Singerv5.chairs_remove:
                            musteri.delete_ticket()
                            self.ui.lbl_uyari.setText("Bilet iptal edildi")
                        else:
                            self.ui.lbl_uyari.setText("Bilet iptal edilemez")
                    else:
                        self.ui.lbl_uyari.setText("18 yaşından küçükler bu İşlemi gerçekleştiremez")
                elif bilet==bilet_normal:
                    if age>13:
                            normal_chair=int(normal_chair)
                            musteri=Singer5(name,surname,age,sanatci_bir)
                            b=musteri.delete_person(normal_chair)
                            self.ui.lbl_uyari.setText("{}".format(b))
                    else:
                        self.ui.lbl_uyari.setText("13 yaşından küçükler bu işlemi gerçekleştiremez")
        except ValueError:
            self.ui.lbl_uyari.setText("Lütfen doğru bilgi giriniz")
            
                

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Pencere()
    win.show()
    sys.exit(app.exec_())

app()
    
       
            


