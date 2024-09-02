class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"Ismi : {self.ism} , Familiyasi : {self.familiya}\n"
        info += f"Tug'ilgan yili : {self.tyil} , Passport raqami : {self.passport} "
        return info
    def get_age(self,hozirgi_yil):
        return f"{hozirgi_yil - self.tyil} yoshda"
# inson1 = Shaxs("Maxmud","Shanazarov","AD7796376",2008)
# print(inson1.get_info())
# print(inson1.get_age(2024))

class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.boshqich = 1
        self.manzil = manzil
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.boshqich

    def get_info(self):
        info = f"Ism : {self.ism} , Familiya : {self.familiya}\nBosqich : {self.boshqich} , IDraqami : {self.idraqam}"
        return info

class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati {self.tuman}\ntumani {self.kocha} ko'chasi {self.uy}-uy"
        return manzil



inson1_manzil = Manzil("19","Marifatchilar","Urganch","Xorazm",)
inson1 = Talaba("Maxmud","Shanazarov","AD7796376",2008,"NO00000001",inson1_manzil )
print(inson1.get_info())