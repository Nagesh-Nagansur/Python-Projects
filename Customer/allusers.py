UserList=[]
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
        if user in UserList:
            UserList.remove(user)
            print(f"{user.name} removed ")
        else:
            print(f"{user.name} Not Exist")
    def AllUserList(self):
        print("--->> Users List <<---")
        for i ,j in enumerate(UserList,start=1):
            print(f'--> {i} {j.name}')
