class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.boshqich = 1

    def get_info(self):
        return f"Mening {self.familiya} {self.ism} . Men {self.boshqich} bosqich talabasiman"

    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_age(self,yil = 2024):
        return yil - self.tyil

    def set_bosqich(self,yangi_bosqich):
        self.boshqich = yangi_bosqich

    def update_bosqich(self):
        self.boshqich += 1

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi = fan_nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]
talaba1 = Talaba("Maxmud","Shanazarov",2008)
talaba2 = Talaba("Seyman","Rajabov",2008)
talaba3 = Talaba("Usmon","Rahimov",2008)
# talaba1.update_bosqich()
# print(talaba1.get_info())
Oliygoh = Fan("Matematika")
Oliygoh.add_student(talaba1)
Oliygoh.add_student(talaba2)
Oliygoh.add_student(talaba3)
print(Oliygoh.get_students())