import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['.',',','!','?','#','-','$','@','*']
print('\t Password Generator \n')


password_list =[]
n_letters = int(input('How many letters do you want? '))    #-----> Number of letters in the password
n_numbers = int(input('How many numbers do you want? '))    #-----> Number of numbers in the password
n_symbols = int(input('How many simple characters ? '))      #-----> Number of symbols in the password

for l in range(1,n_letters + 1):
    char= random.choice(letters)
    password_list +=char

for n in range(1,n_numbers + 1):
    number = random.choice(numbers)
    password_list +=number

for s in range(1,n_symbols + 1):
    symbol = random.choice(symbols)
    password_list += symbol

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password +=char

print()
print('The generated password: ', password)