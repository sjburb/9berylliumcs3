class BankAccount:
    def __init__(self, account_number, balance): #These are the attributes of the class.
        self.__account_number = account_number
        self.__balance = balance
    
    def set_account_number(self, account_number): #This method allows you to set the account number of the bank account.
        self.__account_number = account_number
    
    def set_balance(self, newbalance): #This method allows you to set the balance of the bank account. It checks if the new balance is negative and prevents it from being updated if it is.
        print(f"Update balance to {newbalance}")
        if newbalance < 0:
            print("Balance cannot be negative. Balance not updated.")
        else:
            self.__balance = newbalance
    
    def get_account_number(self): #This method allows you to get the account number of the bank account.
        return self.__account_number
        password = "password123"
        enterPassword = input("Enter your password: ")
        if enterPassword == password:
            return self.__account_number
        else:
            print("Incorrect password. Access denied.")
            return None

    def get_balance(self): #This prints the balance of the account.
        return self.__balance

accounts_list = [] #This list is to print what number the object is in the list.

a1 = BankAccount("12345", 1000)
accounts_list.append(a1)

print(f"Account {len(accounts_list)}")
print(f"Account Number: {accounts_list[0].get_account_number()}")
print(f"Balance: {accounts_list[0].get_balance()}")
a1.set_balance(-100)
print("                                   ")
print(f"Account {len(accounts_list)}")
print(f"Account Number: {accounts_list[0].get_account_number()}")
print(f"Balance: {accounts_list[0].get_balance()}")
