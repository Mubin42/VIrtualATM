#Code Elements
class Bank:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f'''UserName: {self.name}
Age: {self.age}
Email: {self.email}''')



class ATM(Bank):
    def __init__(self,name, age, email):
        super().__init__(name,age,email)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount

    def view(self):
        super().display_info()
        print("Balance is: ", self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Amount is Greater than Your Balance")
        else:
            self.balance = self.balance - amount




#UI elements
name = str(input("Input Name: "))
age = int(input("Input Age: "))
mail = str(input("Input Mail: "))
user = ATM(name, age, mail)

while(True):
    mode = input(f'''---------------------
Hello {name}
Type "view" to Display Information
Type "add" to Deposit Money
Type "wr" to Withdraw Money
Type "q" to Quit
----------------------------''')

    if(mode == "q"):
        break

    elif(mode == "view"):
        user.view()

    elif(mode == "add"):
        x = int(input("How much would you like to Deposit: "))
        user.deposit(x)

    elif(mode == "wr"):
        y = int(input("How much would you like to Withdraw: "))
        user.withdraw(y)


