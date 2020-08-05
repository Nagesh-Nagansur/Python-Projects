from allusers import AllUsers
from users import User


rakesh=User('rakesh',debit=2000,item='Suger')
nagesh=User('nagesh',credit=5000,item='None')
vinayak=User('vinayak',debit=2750,item='rice')
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
allusers.AllUserList()
allusers.RemoveUser(nagesh)
