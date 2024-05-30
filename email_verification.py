# faisalaslam218@gmail.com
# abc@g.com
# Condition 1- lenght must be >=6
# Condition 2- All letters must in small case
# Condition 3- All letters must in small case
# Condition 4- Only one @ symbol in mail
# Condition 5- '.' last sy 3 or 4th possition py ho
# Condition 6-  first letter must be alphabet
email_input = input('Please enter your mail : ')
if (len(email_input) > 6):
    if (email_input.islower()):
        if(email_input.find('@') != -1):
            if(email_input.count('@') == 1):
                if(email_input[0].isalpha):
                    if(email_input[-3] == '.' or email_input[-4] == '.'):
                        print(f'Your Email is Verfied \n Email : {email_input} \n Status: Pass')
                    else:
                        print('Invalid Email')
                else:
                    print('First letter must be alphabet')
            else:
                print('Only one @ symbol allowed')
        else:
            print('No @ symbol in your email')
    else:
        print('All letters must be in small case')
else:
  print('Length must be greater than 6')