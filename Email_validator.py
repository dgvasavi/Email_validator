
import re
user_input=str(input(print("Enter your Email ID :  \n")))
var1=re.findall("[^A-Z a-z 0-9 ^. / @]",user_input)
var2=user_input.split("@")

if len(user_input)>=6:
    if user_input[0].isalpha() and user_input.islower() == True:
        if user_input.count("@")==1:
            if var1==[]:
                if user_input.count(" ")==0:    # count space
                    if (user_input[-4]==".") or (user_input[-3]=="."):
                       if var2[0].isalnum()==True:
                           print("\n Valid Email ID")
                       else:
                           print("\n Worng Email ID")
                    else:
                       print("\n using wrong TLD (top level domain)")
                else:
                   print("\n Email contain spaces")
            else:
                 print("\n Email consists of other special symbols which are not allowed")
        else:
            print("\n More then one \"@\" occurred")
    else:
        print("\n Email not starting with alphabet or have upper case letters ")
else:
    print("\n Email is too short")