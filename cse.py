account_balance=785000
pin=9876

user_pin=int(input("enter your pin:"))
if user_pin==pin:
   print("Please choose your language")
   print("1. English")
   print("2. Hindi")

   choice=int(input("\nplease choose an option(1-2):"))
   if choice==1:
        print("\nPlease choose an account")
        print("1. Salary account")
        print("2. Saving account")

        choice=int(input("\nPlease select an option(1-2):"))
        if choice==1:
          print("not available")
        elif choice==2:
         print("welcome to saving account")
         print("\nPlease choose an function to proceed")
         print("1. check balance")
         print("2. withdraw money")

         choice=int(input("\nPlease choose an option(1-2)"))
         if choice==1:
          print(f"\n your current balance is:{account_balance}")
         if choice==2:
          amount=int(input("Enter amount to withdraw"))

          if amount<=account_balance:
            account_balance-=amount
            print("collect the withdraw balance:{withdraw}")
            print(f"remaining balance:{account_balance}") 
          else:
            print("Insufficient balance,please contackbank if there is any mis understanding") 
   else:
    print("not available, sorry for the inconvinience")
else:
  print("Incorrect pin. try again")

print("thank you for using our atm. Have a nice day")  
     
