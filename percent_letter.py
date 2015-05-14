user_string = input("Which string would you like to use? ")
user_num = input("What about the number? ")

try:
    our_num = int(user_num)
except:
    our_num = float(user_num)

if '.' not in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])
