end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
from datetime import datetime,date

def deposit()->str:
    '''
    will add it to the porfolio value
    :return: Visual confirmation of the amount depostied
    '''
    print(3*'\n')
    print(f"{bold_green}Enter the price  of 1 SOL in YEN (link below)")
    print('https://www.coingecko.com/ja/%E3%82%B3%E3%82%A4%E3%83%B3/%E3%82%BD%E3%83%A9%E3%83%8A/jpy')
    price=float(input())
    print(f"{purple_bold} Current price of 1 SOL is {price} \n")
    print(f"{bold_green}HOW MUCH YEN WOULD YOU LIKE TO DEPOSIT\n")
    amount=float(input())
    sol_amount=(amount/price).__round__(4)
    print(f"The amount that will be deposited is->{bold_cyan} {sol_amount} SOL{end_code}\n")
    file = open("../Deposits.csv", "a")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    file.write(f"{sol_amount},{amount},{current_time},{d1}\n")
    return (f"{bold_cyan}{sol_amount} SOL{end_code} deposited on {red}{current_time}{end_code} on {red}{d1}\n")




