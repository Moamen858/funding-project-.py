import P1
option=input("1-Register\n2-Login.\nOption: ")
if(int(option)==1):
    P1.user_register()
elif (int(option)==2):
    P1.user_login()
else:
    print("invalid option")
