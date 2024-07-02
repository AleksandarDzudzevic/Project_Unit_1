from PROJECT_1_deposit import deposit
from PROJECT_1_withdraw import withdraw
from PROJECT_1_porfolio_change import porfolio_change
from PROJECT_1_info_tab import about_us
from PROJECT_1_analysis import analysis
import time
'''from PROJECT_1_withdraw
from PROJECT_1_expense_porfolio
from PROJECT_1_porfolio_change
from PROJECT_1_analysis'''
end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
purple="\33[0;35m"
strong_yellow="\33[1;93m"

def sol_price()->float:
    '''

    :return: the price inputed
    '''
def main_menu():
    print(f'''{bold_cyan}                                                              
    88b           d88  88888888888  888b      88  88        88       
    888b         d888  88           8888b     88  88        88       
    88`8b       d8'88  88           88 `8b    88  88        88       
    88 `8b     d8' 88  88aaaaa      88  `8b   88  88        88  888  
    88  `8b   d8'  88  88"""""      88   `8b  88  88        88  888  
    88   `8b d8'   88  88           88    `8b 88  88        88       
    88    `888'    88  88           88     `8888  Y8a.    .a8P  888  
    88     `8'     88  88888888888  88      `888   `"Y8888Y"'   888  
                                                                     
                                                                   {end_code}  ''')
    print(f"Welcome to the main menu of {purple_bold}Inve{bold_cyan}SOL.py {end_code} press the number of the option you want:")
    print(f"{bold_green}1) DEPOSIT SOL💸")
    print(f"{red_underline}2) WITHDRAW SOL💸")
    print(f"{bold_cyan}3) PORFOLIO OVERVIEW% 💹 ")
    print(f"{strong_yellow}4) USE {purple_bold}Inve{bold_cyan}SOL.py PREMIUM {strong_yellow} the INVESTING_ANALYSIS{end_code}")
    print(f"{purple_bold}5) ABOUT Solana & Inve{bold_cyan}SOL.py💻💻💻")
    print(f"{red}0) TO EXIT THE PROGRAM")
    option=int(input())
    while option!=0:
        while not option in [1,2,3,4,5]:
            print(f'{red}WRONG INPUT TRY AGAIN{end_code}')
            print(f"Welcome to the main menu of {purple_bold}Inve{bold_cyan}SOL.py {end_code} press the number of the option you want:")
            print(f"{bold_green}1) DEPOSIT SOL💸")
            print(f"{red_underline}2) WITHDRAW SOL💸")
            print(f"{bold_cyan}3) PORFOLIO OVERVIEW% 💹 ")
            print(f"{strong_yellow}4) USE {purple_bold}Inve{bold_cyan}SOL.py PREMIUM {strong_yellow} the INVESTING_ANALYSIS{end_code}")
            print(f"{purple_bold}5) ABOUT Solana & Inve{bold_cyan}SOL.py💻💻💻")
            print(f"{red}0) TO EXIT THE PROGRAM")
            option=int(input())
            print(8*'\n')
        if option==1:
            print(deposit())
        if option==2:
            print(withdraw())
        if option==3:
            print(porfolio_change())
        if option==4:
            print(analysis())
        if option==5:
            print(about_us())
        print(f'{bold_green}RETURNING TO THE MENU')
        menu=input("Click any button when you want to return to the menu")
        for i in range(10):
            print("🟩",end='.')
            time.sleep(0.25)
        print(15*'\n')
        print(f"Welcome to the main menu of {purple_bold}Inve{bold_cyan}SOL.py {end_code} press the number of the option you want:")
        print(f"{bold_green}1) DEPOSIT SOL💸")
        print(f"{red_underline}2) WITHDRAW SOL💸")
        print(f"{bold_cyan}3) PORFOLIO OVERVIEW% 💹 ")
        print(f"{strong_yellow}4) USE {purple_bold}Inve{bold_cyan}SOL.py PREMIUM {strong_yellow} the INVESTING_ANALYSIS{end_code}")
        print(f"{purple_bold}5) ABOUT Solana & Inve{bold_cyan}SOL.py💻💻💻")
        print(f"{red}0) TO EXIT THE PROGRAM")
        option=int(input())
    print(f"{red}Thank you for using{bold_cyan} InveSOL.py{end_code} \n        {bold_green}Goodbye 👋👋👋 ")


