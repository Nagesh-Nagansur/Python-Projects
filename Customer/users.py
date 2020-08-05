from colorama import Fore,Back,Style
import datetime as d



class User:
    'This is for creating a user checking his balance User data'
    def __init__(self,name,item,credit=0,debit=0):
        try:


            self.Date=d.datetime.now().strftime("%d-%m-%y               ")
            self.datetimelist=[]
            self.itemlist=[]
            self.creditlist=[]
            self.debitlist=[]
            self.itemlist.append(item)
            self.debitlist.append(debit)
            self.creditlist.append(credit)
            self.datetimelist.append(self.Date)

            self.name = name
            self.credit = credit
            self.debit = debit
            self.balance=0
            if credit==0:
                self.balance-=debit
            elif debit==0:
                self.balance+=credit
        except AttributeError:
            print('AttributeError')

        except ValueError:
            print('ValueError')

        except TypeError:
            print('Enter the currect value')


    def UpdateData(self,item,credit=0,debit=0):
        try:
            self.Date=d.datetime.now().strftime("%d-%m-%y                 ")
            if credit==0 and debit==0:
                if self.balance<0:
                    print(f"You will get {self.balance}")
                elif self.balance>=0:
                    print(f"You gave {self.balance}")

            elif credit==0:
                self.balance-=debit
                self.debitlist.append(debit)
                self.creditlist.append(credit)
                self.itemlist.append(item)
                self.datetimelist.append(self.Date)

                if self.balance<0:
                    print(f"debited Rs:{debit} You will get {abs(self.balance)}")
                elif self.balance>=0:
                    print(f"debited Rs:{debit} You gave {abs(self.balance)}")
            elif debit==0:
                self.balance+=credit
                self.debitlist.append(debit)
                self.creditlist.append(credit)
                self.itemlist.append(item)
                self.datetimelist.append(self.Date)

                if self.balance<0:
                    print(f"credited Rs:{credit} You will get {abs(self.balance)}")
                elif self.balance>=0:
                    print(f"credited Rs:{credit} You gave {abs(self.balance)}")
        except AttributeError:
            print('AttributeError')

        except ValueError:
            print('ValueError')

        except TypeError:
            print('Enter the currect valuee')

        except Exception:
            print('Unkonwn Exception Occured')

    def Data(self):
        combo=list(zip(self.itemlist,self.debitlist,self.creditlist,self.datetimelist))
        if self.balance <=0:
            print(' '+Fore.GREEN+f"Name:-{self.name.upper()}                         You will get "+Fore.RED+f'{abs(self.balance)}')
            print(f"Date of creation {self.Date}")
            print(Fore.BLUE+'<<<------------------------------------------------>>>')
        else:
            print(' '+Fore.GREEN+f"Name:-{self.name.upper()}                         You will give "+Fore.GREEN+f'{abs(self.balance)}')
        print(Style.BRIGHT+Fore.YELLOW+"Item------->Debit------>Credit--------->Date Time  ")
        for i,d,c,da in combo:
            print(f"{i}------>{d}------>{c}--------->{da}")
        print(Fore.CYAN+'<<<------------------------------------------------>>>')
        print(f"Total Credit-->{sum(self.creditlist)}")
        print(f"Total Debit-->{sum(self.debitlist)}")
        print(Fore.CYAN+'<<<------------------------------------------------>>>')
        print(Fore.BLACK+Style.NORMAL)
    def CheckBalance(self):
        if self.balance<0:
            print(f"{self.name} You will get {abs(self.balance)}")
        elif self.balance>=0:
            print(f"{self.name} You gave {self.balance} from you")
