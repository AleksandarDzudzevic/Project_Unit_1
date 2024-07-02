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
    with open("../passwords.csv", "r") as file:
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
    file = open("../passwords.csv", "a")
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
