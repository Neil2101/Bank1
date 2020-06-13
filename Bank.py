class Bank:
  balance = 0
  name = ''

  def __init__(self,balance,name):
    self.balance = balance
    self.name = name

  def getName(self):
    return self.name

  def getBalance(self):
    return self.balance

  def setName(self,name):
    self.name = name

  def setBalance(self,balance):
    self.balance = balance

  def deposit(self,add):
    self.balance += add

  def withdraw(self,decrease):
    self.balance -= decrease
"""
account1 = Bank(100,'Neil')
account2 = Bank(100,'Lucas')
account3 = Bank(100,'Raghav')
account4 = Bank(100,'Abror')
account5 = Bank(100,'Leymar')
account6 = Bank(100,'Atharv')
account7 = Bank(100,'Selin')


k = [account1,account2,account3,account4,account5,account6,account7]
def menu():
  try:
    accountSelection = int(input('What account do you want? 1 is '+account1.getName()+' 2 is '+account2.getName()+' 3 is '+account3.getName()+' 4 is '+account4.getName()+' 5 is '+account5.getName()+' 6 is '+account6.getName()+' 7 is '+account7.getName()+'. Answer: '))
    account = k[accountSelection-1]
    print('Hello, '+str(account.getName())+', Your Balance is: '+str(account.getBalance())+'.')
    while 1==1:
      a = input('You can type \n1 for getting your balance \n2 for getting your name \n3 for depositing  \n4 for withdrawing \n5 for resetting your name \n6 for using another user\nExIt to exit\n')
      if a == '1':
        print(account.getBalance())
      elif a == '2':
        print(account.getName())
      elif a == '3':
        x = int(input('How much do you want to deposit? Answer: ' ))
        account.deposit(x)
        print('Your New Balance is: ' + str(account.getBalance()))
      elif a == '4':
        x = int(input('How much do you want to withdraw? Answer: ' ))
        if x < int(account.getBalance()):
          account.withdraw(x)
          print('Your New Balance is: ' + str(account.getBalance()))
        else:
          print('Sorry, you don\'t have that much money.' )
      elif a == '5':
        x = input('what\'s the name? ')
        account.setName(x)
      elif a == '694782386@#$%**%&@*':
        x = int(input('What\'s the balance? '))
        account.setBalance(x)
      elif a == '6':
        menu()
      elif a == '7':
        #What I have so far
        x = int(input('What\'s the balance? Answer: '))
        y = input('What\'s the name? Answer: ')
        k.append(Bank(x,y))
        menu()
      elif a == 'ExIt':
        break
        break
        break
        break
      else:
        pass
  except KeyboardInterrupt:
    print('Bye!!!')
    menu()
  except:
    print('sorry, something went wrong...')
    menu()

menu()
