from colorama import Fore,Back,Style
UserList=[]
class User:
    def __init__(self,name,item,credit=0,debit=0):
        try:
            self.itemlist=[]
            self.creditlist=[]
            self.debitlist=[]
            self.itemlist.append(item)
            self.debitlist.append(debit)
            self.creditlist.append(credit)

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

                if self.balance<0:
                    print(f"debited Rs:{debit} You will get {abs(self.balance)}")
                elif self.balance>=0:
                    print(f"debited Rs:{debit} You gave {abs(self.balance)}")
            elif debit==0:
                self.balance+=credit
                self.debitlist.append(debit)
                self.creditlist.append(credit)
                self.itemlist.append(item)

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
        combo=list(zip(self.itemlist,self.debitlist,self.creditlist))
        if self.balance <=0:
            print(' '+Fore.GREEN+f"Name:-{self.name.upper()}                         You will get "+Fore.RED+f'{abs(self.balance)}')
            print(Fore.BLUE+'<<<------------------------------------------------>>>')
        else:
            print(' '+Fore.GREEN+f"Name:-{self.name.upper()}                         You will give "+Fore.GREEN+f'{abs(self.balance)}')
        print(Style.BRIGHT+Fore.YELLOW+"Item------->Debit------>Credit     ")
        for i,d,c in combo:
            print(f"{i}------>{d}------>{c}")
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


class AllUsers:

    def AddUser(self,user):
        if user in UserList:
            print('Already Exist')
        else:
            UserList.append(user)
            print(f"{user.name} Added")

    def CheckTotalIncommigBalance(self):
        self.TotalIncomming=0
        for incom in UserList:
            if incom.balance<0:
                self.TotalIncomming+=abs(incom.balance)
            else:
                pass
        print(f"TotalIncomming:-{self.TotalIncomming}")

    def CheckTotalOutGoiingBalance(self):
        self.TotalOutGoing=0
        for outgo in UserList:
            if outgo.balance>=0:
                self.TotalOutGoing+=abs(outgo.balance)
            else:
                pass
        print(f"TotalOutGoing:-{self.TotalOutGoing}")

    def RemoveUser(self,user):
        Alluserlist.remove(user)

    def AllUserList(self):
        print("--->> Users List <<---")
        for i ,j in enumerate(UserList,start=1):
            print(f'--> {i} {j.name}')
    def OverallBalance(self):
        self.OverallBalance=self.TotalOutGoing-self.TotalIncomming
        if self.OverallBalance>=0:
            print(f'I will pay {self.OverallBalance}')
        else:
            print(f'I will get {abs(self.OverallBalance)}')

rakesh=User('rakesh',debit=2000,item='Suger')
nagesh=User('naegsh',credit=5000,item='None')
vinayak=User('vinayak',debit=2750,item='Bagar')
swati=User('Swati',debit=3240,item='Penuts')


allusers=AllUsers()
allusers.AddUser(vinayak)
allusers.AddUser(swati)
allusers.AddUser(rakesh)
allusers.AddUser(nagesh)

rakesh.UpdateData(item='None',debit=1500)
rakesh.UpdateData(item='Tea Powder',debit=2000)
rakesh.UpdateData(item='None',credit=3000)
rakesh.Data()
nagesh.UpdateData(item='Salt',debit=50)
nagesh.UpdateData(item='jaggery',debit=400)
nagesh.UpdateData(item='Ruchi Gold',debit=90)
nagesh.Data()


allusers.CheckTotalIncommigBalance()
allusers.CheckTotalOutGoiingBalance()
allusers.OverallBalance()
allusers.AllUserList()
