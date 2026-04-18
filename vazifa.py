class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, pasport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot qaytaradi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan."
        return info

class Fan:
    """Fanlar haqida klass"""
    def __init__(self, nomi):
        self.nomi = nomi
    
    def get_name(self):
        return self.nomi

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, pasport, tyil, idraqam):
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    
    def fanga_yozil(self, fan_obyekti):
        """Talabaning fanlar ro'yxatiga fan qo'shadi"""
        self.fanlar.append(fan_obyekti)
        
    def remove_fan(self, fan_nomi):
        """Ro'yxatdan fanni o'chiradi"""
        topildi = False
        for fan in self.fanlar:
            if fan.nomi == fan_nomi:
                self.fanlar.remove(fan)
                topildi = True
                break
        
        if not topildi:
            return "Siz bu fanga yozilmagansiz"
            
    def get_info(self):
        """Talaba haqida ma'lumot (Polimorfizm)"""
        info = f"{self.ism} {self.familiya}. ID: {self.idraqam}. "
        info += f"Fanlar soni: {len(self.fanlar)}"
        return info
    
class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, pasport, tyil, daraja):
        super().__init__(ism, familiya, pasport, tyil)
        self.daraja = daraja
    
    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, Ilmiy darajasi: {self.daraja}"

class Foydalanuvchi(Shaxs):
    """Tizim foydalanuvchisi"""
    def __init__(self, ism, familiya, pasport, tyil, login):
        super().__init__(ism, familiya, pasport, tyil)
        self.login = login
    
    def get_info(self):
        return f"Foydalanuvchi: {self.login}, Ismi: {self.ism}"

class Admin(Foydalanuvchi):
    """Foydalanuvchidan voris olgan Admin klassi"""
    def __init__(self, ism, familiya, pasport, tyil, login):
        super().__init__(ism, familiya, pasport, tyil, login)
    
    def ban_user(self):
        """Faqat adminga xos yangi metod"""
        return "Foydalanuvchi bloklandi"
    
    def get_info(self):
        return f"ADMIN: {self.login} (To'liq huquqli)"