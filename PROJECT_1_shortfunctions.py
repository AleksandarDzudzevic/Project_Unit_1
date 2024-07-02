end_code = "\033[00m"
red = "\33[0;31m"
green = "\033[0;32m"
bold_green = "\033[1;32m"
bold_cyan = "\33[1;36m"
red_underline = "\33[4;31m"
purple_bold = "\33[1;35m"
blue="\33[1;34m	"
def goodbye_msg()->str:
    """
    :return: a goodbye message and thank user for using the program
    """
    return(f"{red}Thank you for using{bold_cyan} InveSOL.py{end_code} \n        {bold_green}Goodbye 👋👋👋 ")
def login_tab_msg()->str:
    '''

    :return: directions about what to do
    '''
    msg=""
    msg+=(f"{bold_green}Welcome to LOGIN/SIGNUP page {end_code}".center(100,"-"))
    msg+="\n"
    msg+="\n"
    msg+=(f"     {purple_bold}1) If you already have an account click 1 to login \n")
    msg+=((f"{blue}2) If you don't have an account click 2 to register \n{end_code}").center(50,"="))
    return msg
def error_msg(msg:str)->str:
    '''

    :param msg:
    :return: Error in the red color
    '''
    return(f"{red_underline}ERROR:{msg}")

def clearmsg():
    return(10*"\n")

