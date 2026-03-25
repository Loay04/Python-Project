import os
import time
dollar=""" ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||"""
money={
    "Welcome in money covert....\n\n":dollar,
    "USD":1.0,
    "EUR":0.85,
    "SYR":15000,
    "EGB":30.8,
    "RMB":6.5
}
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear") 
def show():
    print("Welcome in moeny convert... ")
    for i in money:
        print(f"{i} : {money[i]}")
def price():
    clear()
    show()
    while True:
        convert_from=input("Choose a currency from convert: ").upper()
        amount = float(input("Entre the amount: "))
        if input(f"/nYou ented {amount} {convert_from}. Confirm(Y/N) ").upper() != "Y":
            price()
        clear()
        show()
        convert_to=input("Choose a currency to convert to: ").upper()
        time.sleep(2)
        print(f"Preparing the deal from {convert_from} to {convert_to}.....Please wait\n")
        time.sleep(1)
        if (convert_from not in money or convert_to not in money):
            print("We do not currency to convert to ")
            time.sleep(1)
            if input("Do you want to perform another conversion? (Y/N)").upper() == "Y":
               price()
            else:
               break
        new_rate = money[convert_to] * amount/money[convert_from]
        print(f"{amount} {convert_from} is equal to {round(new_rate,2)} {convert_to}\n")
        print(f"{amount * 100} {convert_from} is equal to {new_rate * 100} {convert_to}/n")
        if input("DO you accept this transaction? (Y/N): ").upper() == "Y":
            print("Transaction successfully.\n")
        else:
            print("Transaction cancelled.\n")
        if input("Do you want to perform another conversion? (Y/N):").upper() == "Y":
            price()
        else:
            print("Thanks for using us application.....")
            break
price()
