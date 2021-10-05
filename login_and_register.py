import getpass
import os
class Account:
    def __init__(self, ism=None, login=None, parol=None, yosh=None, file="acount.txt", file_login="login.txt", qaysi_qatorligi=0):
        self.ism = ism
        self.login = login
        self.parol = parol
        self.yosh = yosh
        self.file = file
        self.file_login = file_login
        self.qaysi_qatorligi = qaysi_qatorligi

    def register_or_login(self):
        a = input("Which do you want (Register or login)\n").strip().lower()
        while a != "register" and a != "login":
            os.system("cls")
            print("Invalid syntax")
            a = input("Which do you want (Register or login)\n").strip().lower()
        if a == "register":
            self.register()
        elif a == "login":
            self.log_in()

    def register(self):
        name = input("Ismingizni kiting :").strip().capitalize()
        while not name:
            os.system("cls")
            name = input("You have entered blank please enter your name again\n").strip().capitalize()
            os.system("cls")
        print(f"name : {name}")
        loginn = input("loginingizni kiting :").strip()
        while self.mavjud(loginn):
            loginn = input("Bunday foydalanuvchi mavjud iltimos boshqa login kiriting :")

        os.system("cls")
        while not loginn:
            os.system("cls")
            print(f"name : {name}")
            loginn = input("You have entered blank please enter your login again\n").strip()
            os.system("cls")
        print(f"name : {name}")
        print(f"loginn : {loginn}")
        parol = getpass.getpass("parolingizni kiting :").strip()
        os.system("cls")
        while not parol:
            os.system("cls")
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            parol = getpass.getpass("You have entered blank please enter your parol again\n").strip()
        print(f"name : {name}")
        print(f"loginn : {loginn}")
        parol2 = getpass.getpass("parolingizni kiting :").strip()
        os.system("cls")
        if parol != parol2:
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            print("Invalid Syntax")
            os.system("cls")
            parol = getpass.getpass("parolingizni kiting :").strip()
            parol2 = getpass.getpass("parolingizni kiting :").strip()
            while not parol or not parol2 or parol != parol2:
                os.system("cls")
                print("Invalid Syntax")
                parol = getpass.getpass("parolingizni kiting :").strip()
                parol2 = getpass.getpass("parolingizni kiting :").strip()
                os.system("cls")
        print(f"name : {name}")
        print(f"login : {loginn}")
        print(f"parol : {parol}")
        yoosh = input("yoshingizni son bilan kiting :").strip()
        os.system("cls")
        while not yoosh or not yoosh.isdigit():
            os.system("cls")
            print(f"name : {name}")
            print(f"login : {loginn}")
            print(f"parol : {parol}")
            yoosh = input("You have entered blank or you have entered string please enter your age again\n").strip()
        print(f"name : {name}")
        print(f"login : {loginn}")
        print(f"parol : {parol}")
        print(f"yosh : {yoosh}")
        self.ism = name
        self.login = loginn
        self.yosh = yoosh
        self.parol = parol
        self.faylga_yozish()
        self.login_file()
        print("You have succesfully registered")

    def login_file(self):
        a = self.login
        file = open(self.file_login, "a")
        file.write("\n" + a)
        file.close()

    def faylga_yozish(self):
        a = f"\nism={self.ism},login={self.login},parol={self.parol},yosh={self.yosh}"
        file = open(self.file, "a")
        file.write(a)
        file.close()

    def mavjud(self, new_login):
        papka = open(self.file_login)
        popka = papka.read()
        popka = popka.split("\n")
        if new_login in popka:
            return True

    def log_in(self):
        name = input("Ismingizni kiting :").strip().capitalize()
        while not name:
            os.system("cls")
            name = input("You have entered blank please enter your name again\n").strip().capitalize()
            os.system("cls")
        print(f"name : {name}")
        loginn = input("loginingizni kiting :").strip()
        while not loginn:
            os.system("cls")
            print(f"name : {name}")
            loginn = input("You have entered blank please enter your login again\n").strip()
            os.system("cls")
        print(f"name : {name}")
        print(f"loginn : {loginn}")
        parol = getpass.getpass("parolingizni kiting :").strip()
        os.system("cls")
        while not parol:
            os.system("cls")
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            parol = getpass.getpass("You have entered blank please enter your parol again\n").strip()  # fas
        print(f"name : {name}")
        print(f"loginn : {loginn}")
        parol2 = getpass.getpass("parolingizni kiting :").strip()  # a
        os.system("cls")
        if parol != parol2:
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            print("Invalid Syntax")
            os.system("cls")
            parol = getpass.getpass("parolingizni kiting :").strip()
            parol2 = getpass.getpass("parolingizni kiting :").strip()
            while not parol or not parol2 or parol != parol2:
                os.system("cls")
                print("Invalid Syntax")
                parol = getpass.getpass("parolingizni kiting :").strip()
                parol2 = getpass.getpass("parolingizni kiting :").strip()
                os.system("cls")
        print(f"name : {name}")
        print(f"login : {loginn}")
        print(f"parol : {parol}")
        yoosh = input("yoshingizni son bilan kiting :").strip()
        os.system("cls")
        while not yoosh or not yoosh.isdigit():
            os.system("cls")
            print(f"name : {name}")
            print(f"login : {loginn}")
            print(f"parol : {parol}")
            yoosh = input("You have entered blank or you have entered string please enter your age again\n").strip()
        print(f"name : {name}")
        print(f"login : {loginn}")
        print(f"parol : {parol}")
        print(f"yosh : {yoosh}")
        self.ism = name
        self.login = loginn
        self.yosh = yoosh
        self.parol = parol
        self.mavjud_bomasa()
        self.ozgartirish_mavjud_bosa()


    def tekshirish(self):
        a = open("acount.txt")
        b = a.read().split("\n")
        a.close()
        a = f"ism={self.ism},login={self.login},parol={self.parol},yosh={self.yosh}"
        for c in range(len(b)):
            if a in b[c]:
                self.qaysi_qatorligi = c
                return True
    def ozgartirish_mavjud_bosa(self):
        if self.tekshirish():
            print("Loginingizga xush keligsiz")
            ha_yoq = input("loginingizni ozgartirishni hohlaysizmi(h/y)").strip().lower()
            while not ha_yoq:
                os.system("cls")
                ha_yoq = input("Bosh login kiritdingiz iltimos boshqatdan kiriting(h/y)").strip().lower()
            if ha_yoq == "h" or ha_yoq == "ha":
                name = input("Ismingizni kiting :").strip().capitalize()
                while not name:
                    os.system("cls")
                    name = input("You have entered blank please enter your name again\n").strip().capitalize()
                    os.system("cls")
                print(f"name : {name}")
                loginn = input("loginingizni kiting :").strip()
                while self.mavjud(loginn):
                    loginn = input("Bunday foydalanuvchi mavjud iltimos boshqa login kiriting :")

                os.system("cls")
                while not loginn:
                    os.system("cls")
                    print(f"name : {name}")
                    loginn = input("You have entered blank please enter your login again\n").strip()
                    os.system("cls")
                print(f"name : {name}")
                print(f"loginn : {loginn}")
                parol = getpass.getpass("parolingizni kiting :").strip()
                os.system("cls")
                while not parol:
                    os.system("cls")
                    print(f"name : {name}")
                    print(f"loginn : {loginn}")
                    parol = getpass.getpass("You have entered blank please enter your parol again\n").strip()  # fas
                print(f"name : {name}")
                print(f"loginn : {loginn}")
                parol2 = getpass.getpass("parolingizni kiting :").strip()  # a
                os.system("cls")
                if parol != parol2:
                    print(f"name : {name}")
                    print(f"loginn : {loginn}")
                    print("Invalid Syntax")
                    os.system("cls")
                    parol = getpass.getpass("parolingizni kiting :").strip()
                    parol2 = getpass.getpass("parolingizni kiting :").strip()
                    while not parol or not parol2 or parol != parol2:
                        os.system("cls")
                        print("Invalid Syntax")
                        parol = getpass.getpass("parolingizni kiting :").strip()
                        parol2 = getpass.getpass("parolingizni kiting :").strip()
                        os.system("cls")
                print(f"name : {name}")
                print(f"login : {loginn}")
                print(f"parol : {parol}")
                yoosh = input("yoshingizni son bilan kiting :").strip()
                os.system("cls")
                while not yoosh or not yoosh.isdigit():
                    os.system("cls")
                    print(f"name : {name}")
                    print(f"login : {loginn}")
                    print(f"parol : {parol}")
                    yoosh = input("You have entered blank or you have entered string please enter your age again\n").strip()
                print(f"name : {name}")
                print(f"login : {loginn}")
                print(f"parol : {parol}")
                print(f"yosh : {yoosh}")
                self.ism = name
                self.login = loginn
                self.yosh = yoosh
                self.parol = parol
                a = open("acount.txt")
                b = a.read().split("\n")
                b[self.qaysi_qatorligi] = f"ism={self.ism},login={self.login},parol={self.parol},yosh={self.yosh}"
                a = open("acount.txt", "w")
                a.write("\n".join(b))
                a.close()
            else:
                print("Korishguncha")
                exit()
    def mavjud_bomasa(self):
        while not self.tekshirish():
            print("This account has not in server please try again")
            name = input("Ismingizni kiting :").strip().capitalize()
            while not name:
                os.system("cls")
                name = input("You have entered blank please enter your name again\n").strip().capitalize()
                os.system("cls")
            print(f"name : {name}")
            loginn = input("loginingizni kiting :").strip()
            while not loginn:
                os.system("cls")
                print(f"name : {name}")
                loginn = input("You have entered blank please enter your login again\n").strip()
                os.system("cls")
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            parol = getpass.getpass("parolingizni kiting :").strip()
            os.system("cls")
            while not parol:
                os.system("cls")
                print(f"name : {name}")
                print(f"loginn : {loginn}")
                parol = getpass.getpass("You have entered blank please enter your parol again\n").strip()  # fas
            print(f"name : {name}")
            print(f"loginn : {loginn}")
            parol2 = getpass.getpass("parolingizni kiting :").strip()  # a
            os.system("cls")
            if parol != parol2:
                print(f"name : {name}")
                print(f"loginn : {loginn}")
                print("Invalid Syntax")
                os.system("cls")
                parol = getpass.getpass("parolingizni kiting :").strip()
                parol2 = getpass.getpass("parolingizni kiting :").strip()
                while not parol or not parol2 or parol != parol2:
                    os.system("cls")
                    print("Invalid Syntax")
                    parol = getpass.getpass("parolingizni kiting :").strip()
                    parol2 = getpass.getpass("parolingizni kiting :").strip()
                    os.system("cls")
            print(f"name : {name}")
            print(f"login : {loginn}")
            print(f"parol : {parol}")
            yoosh = input("yoshingizni son bilan kiting :").strip()
            os.system("cls")
            while not yoosh or not yoosh.isdigit():
                os.system("cls")
                print(f"name : {name}")
                print(f"login : {loginn}")
                print(f"parol : {parol}")
                yoosh = input("You have entered blank or you have entered string please enter your age again\n").strip()
            print(f"name : {name}")
            print(f"login : {loginn}")
            print(f"parol : {parol}")
            print(f"yosh : {yoosh}")
            self.ism = name
            self.login = loginn
            self.yosh = yoosh
            self.parol = parol

user = Account()
user.register_or_login()