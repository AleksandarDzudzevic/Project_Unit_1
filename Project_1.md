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
#### Appendix for Criteria A
MEETING ONE WITH THE CLIENT AND AGREEMENTS FROM IT
![](https://github.com/AleksandarDzudzevic/Project_ideas-plans/blob/main/Project_1_meeting1.jpg)
MLA CITATIONS FOR THE PROPOSED SOLUTION TEXT (why python / why solana)

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
|4|Functional testing||||
|5|Functional testing||||
|6|Functional testing||||

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
|25|||||
|26|||||
|27|||||
