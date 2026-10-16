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
print(f"Balance: {accounts_list[0].get_balance():.2f}")
a1.set_balance(-100)
print("                                   ")
print(f"Account {len(accounts_list)}")
print(f"Account Number: {accounts_list[0].get_account_number()}")
print(f"Balance: {accounts_list[0].get_balance():.2f}")

#What this code does is it creates a class called "BankAccount" with these attributes: "account_number", "balance", "set_account number", "set_balance", "get_account_number", "get_balance".
#The attribute "account_number" is for the account number of the bank account, for example "12345", while "balance" is the amount of money inside the bank account, for example 1000.
#The method "set_account_number" is a way to change the account number of the bank account to a specific number.
#The method "set_balance" is a method to change the balance of the bank account to a specific account. It does not let the balance be less than zero.
#The method "get_account_number" is used display the account nummber of the bank account. It is protected by a password to provide basic privacy.
#The method "get_balance" is function used to display the balance of the bank account.
#"accounts_list" is a list to determine what account is the object. For example a1 is the first bank account, hence it is Account 1.
#"a1" is a sample object that uses the "BankAccount" class. It's account number is "12345" and its balance is "1000". It is appended to the "accounts_list" so it can be idnetified as Accoun 1.
