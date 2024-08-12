import os
print('CADASTRO CASAS BAHIA\n')

dic ={}

dic['NOME'] = input('Nome: ')
os.system('cls')
dic['CPF'] = input('CPF: ')
os.system('cls')
dic['RG'] = input('RG: ')
os.system('cls')
dic['DATA DE NASCIMENTO'] = input('Data de Nascimento: ')
os.system('cls')
dic['SEXO'] = input('Sexo: ')
os.system('cls')
dic['SIGNO'] = input('Signo: ')
os.system('cls')
dic['MÃE'] = input('Nome da mãe: ')
os.system('cls')
dic['PAI'] = input('Nome do pai: ')
os.system('cls')
dic['EMAIL'] = input('email: ')
os.system('cls')
dic['SENHA'] = input('senha: ')

print(f'\n{dic}\n')

for i in dic:
    print('Cliente cadastrado com sucesso\n')
    print(f'{i} : {dic.get(i)}')