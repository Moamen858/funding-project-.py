
import re

email=input("please enter email: \n")
regex=re.compile('^[a-zA-z0-9_]+@[a-zA-Z0-9]+\.[a-z]{2,3}$')
if (re.match(regex,email)):
    print("perfect match")
else:
    print("invalid")

    


        
