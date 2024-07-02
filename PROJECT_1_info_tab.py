end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
headline='\33[1;93m	'
def about_us()->str:
    '''

    :print: a message containing all the information about InveSOL, Solana, our decisions
    :return: confimation that that is the whole message
    '''

    print(f"{headline}ABOUT {bold_cyan}Inve{purple_bold}SOL.py{end_code}")
    print(4*'\n')
    print(f"{bold_green}InveSOL.py is a program built in PyCharm using Python 3.9.\n The main purpose is to help our client/s when investing into crypto currencies, by making all the data organized and easier to access.The program fully runs in the terminal and can perform multiple different actions in the same run. ")
    print(f"""{bold_cyan}Crypto choice
Like previously mentioned, Ms.Sato is open to explore crypto currency of developers choice, and we at InveSOL chose SOLANA.

{purple_bold}Solana{end_code}
Solana is a blockchain platform designed to host decentralized, scalable applications. Solana can process many more transactions per second and charges lower transaction fees than rival blockchains like Ethereum.

{purple_bold}Why SOLANA{end_code}
Very similar to why we chose Python, SOLANA's best qualities allign with what we at InveSOL are trying to achieve.

{purple_bold}FAST{end_code}
Compared to it's competitors, Solana performs it's transactions at much faster speed with amazing 400 millisecond block times. And as hardware gets faster, so does the network.

{purple_bold}CHEAP{end_code}
The avarage transaction fee sits at avarage of only $0.00025 with not a single one being more than 0.01 which makes it a perfect choice for both part-time and full-time crypto investors.

{purple_bold}SECURE{end_code}
With more than 2500 transatcions per second, and more than 100 BILLION successful transations,The Solana network is spread over thousands of independent nodes — which means that your transactions are always safe. The safety of your assets is the number ONE priority.

""")
    return("Finished")
