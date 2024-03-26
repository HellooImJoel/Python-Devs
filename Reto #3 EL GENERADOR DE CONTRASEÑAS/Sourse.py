import random



def PasswordGenerator(length=8):
    
    lower_alphabet = "abcdefghijklmnopqrsuvtñwzx"
    upper_alphabet = lower_alphabet.upper()
    numbers = "1234567890"
    simbols = "!#$%&/()=?¿]{¡[}"
    password = ""

    for i in range(length):
        password += random.choice(lower_alphabet+upper_alphabet+numbers+simbols)
    return password



print(PasswordGenerator())
print(PasswordGenerator(8))
print(PasswordGenerator(16))
print(PasswordGenerator(22))





