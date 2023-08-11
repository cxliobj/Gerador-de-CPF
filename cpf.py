import random

def getLastDigits(cpf, number):
    resto = number % 11
    if (resto == 0 or resto == 1):
        cpf += "0"
    else: 
        cpf += str(11-resto)
    
    return cpf

cpf = ""

i=0
while (i<9):
    numb = random.randint(0, 9)
    cpf += str(numb)
    i+=1

i=0
L=0
while (i<9):
    L += (10-i) * int(cpf[i])
    i += 1

cpf = getLastDigits(cpf, L)

i=1
M=0
while (i<10):
    M += (11-i) * int(cpf[i])
    i += 1
    
cpf = getLastDigits(cpf, M)

print(cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11])
