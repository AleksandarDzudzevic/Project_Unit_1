"""
1) Welcome tab
2) Login/signup
3) Menu tab
4)Deposit/Withdraw
6)Add Hashing
7)Porfolio overlook all deposits,withdrawals,porfolio change
8)Invesol investing tool
9) Solana desription and why we chose SOL for our ledger
"""
from PROJECT_1_WelcomeTab import welcometab
from PROJECT_1_shortfunctions import goodbye_msg, login_tab_msg,error_msg,clearmsg
from PROJECT_1_log_reg import asciilogin,log_reg,asciisignup
from PROJECT_1_Menu_Tab import main_menu
from PROJECT_1_porfolio_change import porfolio_change
if welcometab()==0:
    print(goodbye_msg())
    exit()
else:
    print(50*'\n')
    print(asciilogin()+asciisignup())


    print(login_tab_msg())
    option=int(input())
    if option==1 or option==2:
        print(50*'\n')
        log_reg(option)
    else:
        print(error_msg(msg="Invalid_option_selection_input"))
        print("The program will close")
        exit()
    print(clearmsg())
    print((main_menu()))

