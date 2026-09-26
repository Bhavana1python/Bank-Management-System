#BankExcept.py
from BankMenu import menu
from BankAccountOpen import AccountOpen
from BankPinGenerateUpdate import BPinGenerateUpdate
from BankDeposit import BDeposit
from BankWithDraw import BWithDraw
from BankViewCustomers import BViewCustomers
from BankSearchCustomer import BSearchCustomer
from BankCloseAccount import accountclose
while(True):
    menu()
    try:
        ch = int(input("Enter your choice: "))
        match (ch):
            case 1:
                AccountOpen().openaccount()
            case 2:
                BPinGenerateUpdate().pingenerate()
            case 3:
                BPinGenerateUpdate().pinupdate()
            case 4:
                BDeposit().deposit()
            case 5:
                BWithDraw().withdraw()
            case 6:
                BSearchCustomer().search()
            case 7:
                BViewCustomers().viewcustomer()
            case 8:
                BViewCustomers().viewcustomers()
            case 9:
                accountclose().closeacc()
            case 10:
                print("Thanks for using Bhavana's program")
                break
            case _:
                print("You entered an invalid choice---Try again")
        print("-" * 60)
        ch = input("Do you want to continue yes/no: ")
        if (ch.lower() == "no"):
            print("Thanks for using Bhavana's program")
            break
    except ValueError:
        print("Dont enter alphabets and special characters---Try again")

