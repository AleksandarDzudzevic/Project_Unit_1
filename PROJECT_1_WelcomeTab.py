def welcometab() -> int:
    """

    :return: int which represents the option the person wanted
    """

    # This validates if user's input is intiger
    def validate_int_input(msg: str) -> int:
        end_code = "\033[00m"
        red = "\33[0;31m"

        number = msg
        if not number.isdigit():
            number = input(f"{red}Error.input{end_code}")
            return 0
        return 1

    end_code = "\033[00m"
    red = "\33[0;31m"
    redbackground="\33[41m"
    strongpurple='\33[1;95m	'
    green = "\033[0;32m"
    bold_green = "\033[1;32m"
    bold_cyan = "\33[1;36m"
    red_underline = "\33[4;31m"
    purple_bold = "\33[1;35m"
    print(5*"\n")
    print(18*"❌",f"{red_underline}Bye boring ledgers📒",18*"❌")
    print(8*"💹",f"{bold_cyan}Hello to InveSOL, an easy to use digital crypto ledger💻",8*"💹")
    print(f"""{bold_cyan} 
            =============================================================================={end_code}{strongpurple}
            88888                                   .oooooo..o   .oooooooo.  88888      
            `888'                                   d8P'    `Y8  d8P'  `Y8b  `888'        
             888  ooo. .oo.   oooo    ooo  .ooooo.  Y88bo.      888      888  888         
             888  `888P"Y88b   `88.  .8'  d88' `88b  `"Y8888o.  888      888  888         
             888   888   888    `88..8'   888ooo888      `"Y88b 888      888  888         
             888   888   888     `888'    888    .o oo     .d8P `88b    d88'  888       o 
            o888o o888o o888o     `8'     `Y8bod8P' 8""88888P'   `Y8bood8P'  o888ooooood8{end_code}                                                                              
            {bold_cyan}============================================================================{end_code}                                                                              """)
    print(f"{red_underline}{bold_cyan}Welcome to InveSol{end_code}".center(80, "-"))
    print(f"{bold_cyan}Invest your SOLANA{strongpurple} EASY FAST SAFE{end_code}".center(80))
    print(f"{green}Enter 1 if you want to start the program {end_code}".center(80, "_"))
    print(f"{red}Enter 0 if you want to exit the program {end_code}".center(80, "_"))
    option = input()
    intcheck = validate_int_input(option)  # Gives us 1 or 0 but also checks if input is valid
    if intcheck and int(option)==1:
        return 1
    if intcheck and int(option) == 0:
        return 0
    else:
        print(f'{redbackground}INPUT.ERROR_IS_INVALID PROGRAM WILL CLOSE :(')
        exit()
