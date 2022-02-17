class Bank:
    __interest_rate = 12
    __bank_name = 'Bro Bank Pvt. Ltd.'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name    
        self.last_name = last_name
        self.age = age
        self.balance = 0

    def check_balance(self):
        print(f'Current balance is {self.balance}')       

    def deposit_balance(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

        else:
            print('Enter a valid amount.')
        self.check_balance()

    def withdraw_balance(self, amount):
        if amount < 0 or amount > self.balance:
            print('Enter a valid amount')
        else:
            self.balance = self.balance - amount
        
        self.check_balance()

    @classmethod
    def get_interest_rate(cls):
        print(f"Bank's current interest rate is {Bank.__interest_rate}")

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    @staticmethod
    def print_holiday():
        print('Umesh Regmi ko bday is on 17th Baisakh')
        print('Teej ko bida is on Bhadra 25')

while True:
    print('*************************************************')
    print(f'Welcome to {Bank.get_bank_name()}')
    choice = input('Enter 1 to open bank account \nEnter 2 to check balance \nEnter 3 to deposit balance \nEnter 4 withdraw balance \nEnter 5 to check interest rate \nEnter 6 to print holiday ')
    user = None
    if choice == '1' and user is None:
        first_name = input('Enter your first name ')
        last_name = input('Enter your last name ')
        age = input('Enter your age ')

        user = Bank(first_name, last_name, age)

        deposit = input('Enter 1 to deposit initial balance. Enter 0 to exit ')
        if deposit == '1':
            initil_depsoit = int(input('Enter the amount you want to deposit'))
            user.deposit_balance(initil_depsoit)
        else:
            continue
    
    elif user is not None:
        if choice == '2':
            user.check_balance()
        
        elif choice == '3':
            amount = int(input('Enter the deposit amount '))
            user.deposit_balance(amount)
        
        elif choice == '4':
            amount = int(input('Enter the withraw amount '))
            user.withdraw_balance(amount)
        
    elif choice == '5':
            Bank.get_interest_rate()
        
    elif choice == '6':
            Bank.print_holiday()
    
    else:
        print('Please open an account first')