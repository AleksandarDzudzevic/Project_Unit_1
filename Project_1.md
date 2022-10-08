# Crypto Wallet
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/solana-sol.gif)
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/InveSOLlogo.png)
# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all her transaction using an outdated method of a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. Ms. Sato would also apriciate if the ledger could help her with investing by warning her if the price is unusualy high or low and if she should sell or buy. The ledger is developed in order to help investors like Ms.Sato switch from old to newer and easir ways to track their investments and get acces to different analytics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.


## Proposed Solution

I will design and make a digital and easy to use crypto ledger for a client who is local crypto investor. The digital ledger will consist of nine different programs with a total of about 583 lines and 3 databases storing following data(1. ultra encrypted passwords and usernames,2.deposits,3.withdrawals) and are all connected to the main program, which makes it easier to debug and will help developers identify potentional bugs in a very short amount of time. It is constructed using Python 3.9 on PyCharm platform and it runs on M1 MacBook(2020) base model. The main reason why we chose this laptop model instead of the better one which was available to us, becuase we at InveSOL believe that everyone should be able to invest easily, fast and safely using our program. It will take around 15-20 hours to make the version 1, after which it will be evaluated according to the success criteria stated by the client. 

Why Python? : The reason why we chose Python as the language that we will use for this is simple. It perfectly alligns with our values and main benefits of our program. It is beginner-friendly (one of the reasons why we added the InveSOL analisys so that even the beginners can invest at a high level). It is fast, just like our program which tries to make the execution time as fast as possible(ex. most while loops are replaced by a faster option (for)).
   
 Sky is the limit!!! Just like python which has so many features and cool options, InveSOL.py team aims to make InveSOL app that will constantly develop and get new features which will help more SOLANA investors reach their goals.(1)

## Crypto choice
Like previously mentioned, Ms.Sato is open to explore crypto currency of developers choice, and we at InveSOL chose SOLANA.
 ### Solana 
Solana is a blockchain platform designed to host decentralized, scalable applications. Solana can process many more transactions per second and charges lower transaction fees than rival blockchains like Ethereum.
#### Why SOLANA
Very similar to why we chose Python, SOLANA's best qualities allign with what we at InveSOL are trying to achieve. 
###### FAST
Compared to it's competitors, Solana performs it's transactions at much faster speed with amazing 400 millisecond block times. And as hardware gets faster, so does the network.
###### CHEAP 
The avarage transaction fee sits at avarage of only $0.00025 with not a single one being more than 0.01 which makes it a perfect choice for both part-time and full-time crypto investors.
###### SECURE
With more than 2500 transatcions per second, and more than 100 BILLION successful transations,The Solana network is spread over thousands of independent nodes — which means that your transactions are always safe. The safety of your assets is the number ONE priority.
(2)
## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal). 
2. The electronic ledger display the basic description of the cryptocurrency selected. 
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger has login and sign up option, allowing privacy of information for each user. The database containing passwords will be encrypted using advanced hashing, which is why InveSOL is a perfect choice for you if you value security of your data and crypto.
5. The electronic ledger asks the real time price of the coin and then the electronic ledger shows the porfolio value change by using colored and user friendly method of (%) calculating and displaying the : value of current porfolio|(total amount invested(deposits)- expenses in usd$(withdrawls))x100% using the price change from the last SOL price input.
6. The electronic ledger allows user to see their deposit and withdrawal history, allowing them to have all relevant information needed at one place.
7. The ledger analysis the porfolio change and withdrawal and deposit history, and then gives some of the following suggestions: Warning for spending crypto while its price is one of the lowest ever inputed, or saying that its a good time to exchange it to real money. (basically DCA with a conclusion)
## Appendix for Criteria A
MEETING ONE WITH THE CLIENT AND AGREEMENTS FROM IT
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/Project_1_meeting1.jpg)
MLA CITATIONS FOR THE PROPOSED SOLUTION TEXT (Why Python?(1) / Why Solana?(2))

1)

Arora, Shivam. “Why Learn Python? Reasons and Benefits of Learning Python.” Simplilearn.com, Simplilearn, 8 Sept. 2022, https://www.simplilearn.com/why-learn-python-a-guide-to-unlock-your-python-career-article. 

2)
“Scalable Blockchain Infrastructure: Billions of Transactions &amp; Counting: Solana: Build Crypto Apps That Scale.” Solana, https://solana.com/. 
# Criteria B: Design

## System Diagram
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/Project_1_fig_1_v1.jpg)
## Flow Diagrams

## Test plan
| Task No |        Test type            |          Specific type               |        Planned outcome|       Procedure          |           Outcome           |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
|1|   Non-Functional testing|Performance testing|Identify possible changes in code which would make it faster and which would lower the loading time|Analysed all functions of the program and focused on those which take more than 0.2 sec to perform and further analysed them| The outcome was that the procedure was a success, I got rid of 2 while loops and changed them into for loops which a bit faster 
|2|   Non-Functional testing|Usability testing|without interfering, see if there is anything which would make the test user struggle(uncleat messages?instructions) and work. on that|Test user 001 used the program and shared its concerns| 2 unclear messages where changed and one print color as well in order to highlight the importance of the message that it stated
|3|   Non-Functional testing|Usability testing|Same as test(2) just hopefully other suugestions since it is a differnet person testing it this time|Test user 002 used the program and shared its concerns| Added a link for the current SOLANA price to every messages which asks for the real-time price
|4|Functional testing|Unit Testing(deposit/withdraw)|See if there is something that can be improved and something that is not working in deposit/withdrawal part of the program and if there is, fix it|Start the program and specificly run the deposit/withdrawal part and depo/withdrawal overview option and see if everything is correct| Found that there was a mistake in the fromula used for porfolio overview for the porfolio change option, and fixed it so now it works properly
|5|Functional testing|Integration testing|connect two new options to the main program and see if everything works properly|Connect the programs which contain these two features and call them in the main tab program which is connected to thwe main|Everything worked properly, no problems appeared 
|6|Functional testing|System testing|Test the whole program now that it is finally finished and everything should work properly|Because of the feature of the program to return to the menu tab, testing of every feature will be done in the same run|Everything worked well no problems occured

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Success Criteria                                       | Come to the agreement with the client about success criteria in order to start working                  | 45min         | Sep 23                 | A         |
| 2     | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 25min         | Sep 26                | B         |
| 3    |Meeting client's representative Dr.Ruben to discuss possible additions and changes to the program| Having all the information needed in order to start working on the program         (Meeting info can be found on the repository) |  25min        | Sep 29                 | A |    
|4   |  Welcome tab unit(session 1) |Make a functional and well-organized welcome tab  |73min|Sep 29 |C
|5  | Welcome tab unit(session 2) |Working on the wireframe of the program in order to have a clear and colorful welcome and login tab|45min|Sep 29 |C
|6   |  Working on the signup and login option(session 1) |Have a functional login and signup system |30min|Sep 30 |C
|7   |  Working on the signup and login option(session 2) |Make a functional hashing function in order to keep data of user/s safe and secure  |40min|Sep 30 |C
|8   |  Main Menu Tab (session 1)| Have a main menu wireframe and setup everything needed for session 2 and the techinical part of menu|60min |Oct 1 |C
|9   |  Main Menu Tab (session 2) |Make a functioning deposit option |45min|Oct 1 |C
|10 |   Main Menu Tab (session 3) |Make a functioning withdrawal option |32min|Oct 1/Oct 2|C
|11  |  Porfolio overview Tab (session 1) |Have all the messages and also withdrawal and deposit history option working properly  |40min|Oct 2 |C
|12  |  Add the proposed solution(session 1) |Work on the proposed solution text and explain the following: why MacBook Air if it could limit the program complexity and scalibilty? Why Python? Why Solana? |15min|Oct 2 |A
|13|Porfolio overview Tab(session 2)|Have the colored display of the porfolio change working properly, and make all the database information useful|65min|Oct 3|C
|14|Add the proposed solution (session 2)|Finish the proposed solution, answer all the question mentioned above|25min|Oct 3|A
|15|Add resources used to gather information|Att citations for websites used for the project|5min|Oct 3|A
|16|Porfolio overview Tab(session 3)|Have a funcitonal analysis of the current profolio change displayed in %|35min|Oct 4|C
|17|Making a program option so it can run until the user inputs the exit option|Have an optionj to use multiple tools in one run until user presses 0 to exit|30min|Oct 4|C
|18|Information on Solana and InveSOL.py (session 1)|Write basic desription explaining our choises at InveSOL and a short introduction to Solana crypto|10min|Oct 6|C
|19|InveSOL analysis Tab (session 1)|Have a first version of the function which will take and module the needed data in order to analyse and give output data which is relavanted to the investing decisions|40min|Oct 6|C
|20|InveSol analysis Tab (session 2)|Finish the last feature of Invesol v1 and plug it in the main program|30min|Oct 7|C
|21|Testing (session 1)|Analyze 3 non-functional testings (1 performance and 2 usability testings) performed by test users and make notes which will help will later code modifications|30min|Oct 7|B
|22|Finishing touch (session 1)|Improve user instructions by using suggestions from non-functional testings performed by test users earlier today|15 min|Oct7|C
|23|Testing (session 2)|Analyze 3 functional testings(1 Unit Testing(menu_tab),1 Integration Testing(integrating final part of the priogram and pluging everything into the main), and 1 full System testing) and take notes which will later on help with final code modification|20min|Oct 8|B
|24|Finishing touch (session 2)|Implement notes taken from (23) functional tests and officially finish InveSol.py v1|30min|Oct 8|C
|25|Flow diagrams |Add three flow diagrams that represent different parts of the program|40min|Oct 9|B
|26|Add code parts that solved problems that client had|Have three unique code functions that represent solutions to some parts of the criteria stated by client|10 min|Oct 9|C
|27|||||











# Criteria C: Development
## Functions from the program & problems which they solved

### Client asked for stable and secure login system (Added the register option)
```.py
import hmac
from PROJECT_1_porfolio_change import porfolio_change
end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
def asciilogin()->str:
    '''

    :return: ascii art that is added to login page
    '''
    return(f'''{bold_green}   
        dMP    .aMMMb  .aMMMMP dMP dMMMMb 
       dMP    dMP"dMP dMP"    amr dMP dMP 
      dMP    dMP dMP dMP MMP"dMP dMP dMP  
     dMP    dMP.aMP dMP.dMP dMP dMP dMP   
    dMMMMMP VMMMP"  VMMMP" dMP dMP dMP    
                                     {end_code} ''')
def asciisignup()->str:
    '''

    :return: ascii art that is added to login page
    '''
    return(f''' {blue}
        .dMMMb  dMP .aMMMMP dMMMMb       dMP dMP dMMMMb 
      dMP" VP amr dMP"    dMP dMP      dMP dMP dMP.dMP 
      VMMMb  dMP dMP MMP"dMP dMP      dMP dMP dMMMMP"  
    dP .dMP dMP dMP.dMP dMP dMP      dMP.aMP dMP       
    VMMMP" dMP  VMMMP" dMP dMP       VMMMP" dMP        
                                               {end_code}    ''')
def login(user:str,password:str)->str:
    """

    :param user:
    :param password:
    :return: true or false
    """
    with open("passwords.csv","r") as file:
        database=file.readlines()
    output=(f"{red_underline}Error.Not an existing user.exe {end_code}")
    for line in database: #Checks every user
        #get rid of \n
        clear_line=line.strip()
        separated_line=clear_line.split(",")
        if user==separated_line[0]:
            print("this is the separated line 1    ",separated_line[1])
            print("USer found")
            print(password)
        if user==separated_line[0] and password==separated_line[1]:
            output=True
    return output

def register2():
    """

    :return: nothing, we will input data in the function and once it is entered correctly it will put it in the database
    """
    #open  the file made in mode append : a
    #this means, add to end of the file

    new_user = input("Enter a username")
    new_pass = input("Enter the password")
    pass_check=input("ReEnter the password ")
    while not new_pass==pass_check:
        print(f"{red_underline}ERROR.password_inputs_don't_match, try again{end_code}")
        new_user = input("Enter a username")
        new_pass = input("Enter the password")
        pass_check=input("ReEnter the password ")
    hash_pass=hmac.new(''.encode(),new_pass.encode(), 'sha512').hexdigest()
    file = open("passwords.csv","a")
    file.write(f"{new_user},{hash_pass}\n")
def log_reg(option:int):
    """
    This function is responsible for the whole login process and the selection of the action in the program
    :return:
    """
    if option==2:#User chose signnup option and after he successfully makes an ccount,

        print(asciisignup())       # he/she will be redirected to the login page
        print(7*'\n')
        register2()
        print(f"{bold_green}registered successfully✅✅✅, login to open the program")
        option=1


    if option==1:
        print(asciilogin())
        print(7*'\n')
        user=input(f"{purple_bold}Enter the username:")
        password=input(f"Enter the password{end_code}")
        hashed_pass=hmac.new(''.encode(),password.encode(), 'sha512').hexdigest()
        while not login(user,hashed_pass)==True:
            print(f"{red_underline}LOGIN WAS UNSUCCESSFUL, TRY AGAIN".center(50,"❌"))
            user=input(f"{purple_bold}|Enter the username")
            password=input(f"|Enter the password{end_code}")
            hashed_pass=hmac.new(''.encode(),password.encode(), 'sha512').hexdigest()
            if login(user,hashed_pass)==True:
                break
        if login(user,hashed_pass)==True:
            print(f"{bold_green}LOGIN WAS SUCCESSFUL{end_code}".center(50,"✅"))
```
### At the meeting 1 with the client representative Dr. Ruben developers found out that security is the no.1 priority of Ms. Sato (Last thing in the meeting notes found in the appendix of criteria A) 
```.py
  if option==1:
        print(asciilogin())
        print(7*'\n')
        user=input(f"{purple_bold}Enter the username:")
        password=input(f"Enter the password{end_code}")
        --->hashed_pass=hmac.new(''.encode(),password.encode(), 'sha512').hexdigest()
        while not login(user,hashed_pass)==True:
            print(f"{red_underline}LOGIN WAS UNSUCCESSFUL, TRY AGAIN".center(50,"❌"))
            user=input(f"{purple_bold}|Enter the username")
            password=input(f"|Enter the password{end_code}")
            ----->hashed_pass=hmac.new(''.encode(),password.encode(), 'sha512').hexdigest()
            if login(user,hashed_pass)==True:
                break
        if login(user,hashed_pass)==True:
            print(f"{bold_green}LOGIN WAS SUCCESSFUL{end_code}".center(50,"✅"))
```
the super encryption is pointed using ----->
#### Example of encrypted passwords
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/Project_1_hashing.png)
### Success criteria (5) and (6) stated a need for an option that allows user to see deposit/withdrawal history and porfolio change, and we at InveSOL did just that
```.py
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
    with open("Deposits.csv", "r") as file:
        dp_logs = file.readlines()
    with open("Withdrawals.csv", "r") as file:
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
        for dp in dp_logs:
            values=dp.split(',')
            print(f"{bold_green}Deposit No.{index}:{values[0]} SOL BOUGHT FOR {values[1]} YEN on {(values[2]+' '+values[3]).strip()} {end_code}")
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
        sol_price=float(input("Enter the current price of 1SOL in YEN(link below)"))
        print('https://www.coingecko.com/ja/%E3%82%B3%E3%82%A4%E3%83%B3/%E3%82%BD%E3%83%A9%E3%83%8A/jpy')
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

```
## Appendix
MLA citation of websites used for the code
“HMAC - Keyed-Hashing for Message Authentication¶.” Hmac - Keyed-Hashing for Message Authentication - Python 3.10.7 Documentation, https://docs.python.org/3/library/hmac.html. + Alesandro's help setting it up
