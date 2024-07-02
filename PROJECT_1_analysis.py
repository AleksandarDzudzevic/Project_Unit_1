import time
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
headline='\33[1;93m	'
def analysis()->str:
    '''

    :return: This function will analyze deposit and withdraw information and tells the user if its good tim to invest or not
    '''
    print(f"{bold_cyan}Welcome to InveSOL.py pro analysis please wait for the program to load")
    menu=input("Click any button when you want to start the program")
    for i in range(10):
        print("🟩",end='.')
        time.sleep(0.25)
    print(8*'\n')
    print('https://www.coingecko.com/ja/%E3%82%B3%E3%82%A4%E3%83%B3/%E3%82%BD%E3%83%A9%E3%83%8A/jpy')
    sol_price=float(input(f"{strong_yellow}Enter the current price of 1 SOL(link below)"))
    print(3*'\n')
    with open("../Deposits.csv", "r") as file:
        dp_logs = file.readlines()
    with open("../Withdrawals.csv", "r") as file:
        wd_logs = file.readlines()
    i=0
    j=0
    dp_yen=0
    wd_yen=0
    for dp in dp_logs:
        values=dp.split(',')
        dp_yen+=float(values[1])/float(values[0])
        i+=1
    for wd in wd_logs:
        values2=wd.split(',')
        wd_yen+=float(values2[1])/float(values2[0])
        j+=1
    if sol_price>dp_yen/i:
        print(f"{red}Not a great time to deposit, the current price is higher than the avarage of previous deposits by{bold_cyan} {((sol_price/(dp_yen/i)-1)*100).__round__(4)}% ")
        if sol_price>wd_yen/j:
            print(f"{bold_green}Instead maybe it is not a bad time withdraw with the current price being higher than avarage withdrawal price BY{bold_cyan} {((sol_price/(wd_yen/j)-1)*100).__round__(4)}%{end_code}so withdraw some of the funds and wait until price dops to buy in again")
        print(5*'\n')
    if sol_price<dp_yen/i:
        print(f"{bold_green}Good time to deposit, the current price is lower than the avarage of previous deposits by{bold_cyan} {((((dp_yen/i)/sol_price)-1)*100).__round__(4)}% ")
        print(5*'\n')

