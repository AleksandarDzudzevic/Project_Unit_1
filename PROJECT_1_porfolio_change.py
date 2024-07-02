end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
storng_purple='\33[1;95m'
def porfolio_msg()->str:
    return("""
██████   ██████  ██████  ███████  ██████  ██      ██  ██████     
██   ██ ██    ██ ██   ██ ██      ██    ██ ██      ██ ██    ██ ██ 
██████  ██    ██ ██████  █████   ██    ██ ██      ██ ██    ██    
██      ██    ██ ██   ██ ██      ██    ██ ██      ██ ██    ██ ██ 
██       ██████  ██   ██ ██       ██████  ███████ ██  ██████     
                                                                 
                                                               
""")
def porfolio_change()->str:
    """

    :return: overview of the porfolio change, or if the user chooses option1) list of withdrawals and deposits return just a message that informs that the program is finished
    """
    porfolio_msg()
    with open("../Deposits.csv", "r") as file:
        dp_logs = file.readlines()
    with open("../Withdrawals.csv", "r") as file:
        wd_logs = file.readlines()
    print(f"{bold_cyan}WELCOME TO YOUR PORFOLIO{end_code}")
    print(f"{bold_green}CLICK{red} 1){bold_green}in order to see deposit history{end_code}")
    print(f"{bold_green}CLICK{red} 2){bold_green}in order to see withdrawal history{end_code}")
    print(f"{bold_green}CLICK {red}3){bold_green} in order to see current porfolio change")
    option=int(input())
    if option==1:
        print(8*'\n')
        total_dp=0
        print(f"""{bold_green}
       __                      _ __      
  ____/ /__  ____  ____  _____(_) /______
 / __  / _ \/ __ \/ __ \/ ___/ / __/ ___/
/ /_/ /  __/ /_/ / /_/ (__  ) / /_(__  ) 
\__,_/\___/ .___/\____/____/_/\__/____/  
         /_/                             
""")

        index=1
        22
            index+=1
        for dp in dp_logs:
            values=dp.split(',')
            total_dp+=float(values[0])
        print(f"{storng_purple}TOTAL DEPOSIT AMOUNT IS {total_dp}")

    if option==2:
        print(8*'\n')
        total_wd=0
        print(f"""{red}
           _ __  __        __                          __    
 _      __(_) /_/ /_  ____/ /________ __      ______ _/ /____
| | /| / / / __/ __ \/ __  / ___/ __ `/ | /| / / __ `/ / ___/
| |/ |/ / / /_/ / / / /_/ / /  / /_/ /| |/ |/ / /_/ / (__  ) 
|__/|__/_/\__/_/ /_/\__,_/_/   \__,_/ |__/|__/\__,_/_/____/  
        """)
        index=1
        for wd in wd_logs:
            values2=wd.split(',')
            print(f"{red}Withdrawal No.{index}: {values2[0]} SOL SOLD AT {values2[1]} YEN on {(values2[2]+' '+values2[3]).strip()}  {end_code}")#strip removes all \n -> no more empty rows
            index+=1
        for wd in wd_logs:
            values2=wd.split(',')
            total_wd+=float(values2[0])
        print(f"{storng_purple}TOTAL WITHDRAWN AMOUNT IS {total_wd}")

    if option==3:
        print('https://www.coingecko.com/ja/%E3%82%B3%E3%82%A4%E3%83%B3/%E3%82%BD%E3%83%A9%E3%83%8A/jpy')
        sol_price=float(input("Enter the current price of 1SOL in YEN(link below)"))
        print(5*'\n')
        total_dp=0
        total_wd=0
        dp_yen=0
        wd_yen=0
        print(f"""{bold_cyan}
                      ____      ___               __                         
    ____  ____  _____/ __/___  / (_)___     _____/ /_  ____ _____  ____ ____ 
   / __ \/ __ \/ ___/ /_/ __ \/ / / __ \   / ___/ __ \/ __ `/ __ \/ __ `/ _ |
  / /_/ / /_/ / /  / __/ /_/ / / / /_/ /  / /__/ / / / /_/ / / / / /_/ /  __/
 / .___/\____/_/  /_/  \____/_/_/\____/   \___/_/ /_/\__,_/_/ /_/\__, /\___/ 
/_/                                                             /____/       
""")
        for dp in dp_logs:
            values=dp.split(',')
            total_dp+=float(values[0])
            dp_yen+=float(values[1])
        for wd in wd_logs:
            values2=wd.split(',')
            total_wd+=float(values2[0])
            wd_yen+=float(values2[1])
        if (((total_dp-total_wd)*sol_price)/(dp_yen-wd_yen))>=1:
            print(f"Your Porfolio is UP by  {bold_green}{((((total_dp-total_wd)*sol_price)/(dp_yen-wd_yen))*100-100).__round__(3)}%")
            print(f"YOU ARE AMAZING AT INVESTING!!!! KEEP IT UP!!!! \n TO THE MOOOON!!!!!!")
        if (((total_dp-total_wd)*sol_price)/(dp_yen-wd_yen))<1:
            print(f"Your Porfolio is DOWN by {red}{((((total_dp+total_wd)*sol_price)/(dp_yen-wd_yen)*100)-100).__round__(3)} %")
            print("IT IS OK YOU WILL GET BETTER AT INVESTING")

    return(f"{purple_bold}THIS WAS YOUR PORFOLIO ANALYSIS< YHANK YOU FOR USING InveSOL.py ")
