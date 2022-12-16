from datetime import date
from dicionarios import *

def validar_data():
  valida = False   
  while not valida: 
    dia = input('> Dia: ')
    mes = input('> Mês: ')
    ano = input('> Ano: ')
    ano_atual = date.today().year

    if (dia.isdigit() and mes.isdigit() and ano.isdigit()) != True:
      print('Data inválida!')
    else:
      if (int(mes) > 12) or (int(ano) == 0) or (int(ano) < ano_atual) or (int(dia) == 0) or (int(mes) == 0):
        print('Data inválida')
      else:
        if int(mes) == 2:
          if (int(ano) % 4 == 0) and (int(ano) % 100 != 0) or (int(ano) % 400 == 0):  # ano bissexto
            if int(dia) >= 30:
              print('Data inválida')
            else: 
              datavalida = f'{dia}/{mes}/{ano}'
              valida = True
          else:
            if int(dia) >= 29:
              print('Data inválida')
            else: 
              datavalida = f'{dia}/{mes}/{ano}'
              valida = True
        elif (int(dia) >= 32) and ((int(mes) == 1) or (int(mes) == 3) or (int(mes) == 5) or (int(mes) == 7) or (int(mes) == 8) or (int(mes) == 10) or (int(mes) == 12)):
          print('Data inválida')
        elif (int(dia) >= 31) and ((int(mes) == 4) or (int(mes) == 6) or (int(mes) == 9) or (int(mes) == 11)):
          print('Data inválida')
        else:
          datavalida = f'{dia}/{mes}/{ano}'
          valida = True
  return datavalida
  

def validar_data_nasc():
  valida = False   
  while not valida: 
    dia = input('> Dia: ')
    mes = input('> Mês: ')
    ano = input('> Ano: ')

    if (dia.isdigit() and mes.isdigit() and ano.isdigit()) != True:
      print('Data inválida!')
    else:
      if int(mes) > 12 or int(ano) == 0 or int(dia) == 0 or int(mes) == 0:
        print('Data inválida')
      else:
        if int(mes) == 2:
          if (int(ano) % 4 == 0) and (int(ano) % 100 != 0) or (int(ano) % 400 == 0):  # ano bissexto
            if int(dia) >= 30:
              print('Data inválida')
            else: 
              datavalida = f'{dia}/{mes}/{ano}'
              valida = True
          else: 
            if int(dia) >= 29:
              print('Data inválida')
            else:
              datavalida = f'{dia}/{mes}/{ano}'
              valida = True
        elif (int(dia) >= 32) and ((int(mes) == 1) or (int(mes) == 3) or (int(mes) == 5) or (int(mes) == 7) or (int(mes) == 8) or (int(mes) == 10) or (int(mes) == 12)):
          print('Data inválida')
        elif (int(dia) >= 31) and ((int(mes) == 4) or (int(mes) == 6) or (int(mes) == 9) or (int(mes) == 11)):
          print('Data inválida')
        else:
          datavalida = f'{dia}/{mes}/{ano}'
          valida = True
  return datavalida  
  

def validar_cpf(cpf):
  cpf = [int(char) for char in cpf if char.isdigit()]
  if len(cpf) != 11:
    return False
  if cpf == cpf [::-1]:
    return False

  for i in range(9, 11):
    valor = sum((cpf[num] * ((i + 1 ) - num) for num in range(0, i)))
    digito = ((valor * 10) % 11) % 10
    if digito != cpf[i]:
      return False
  return True
  

def validar_hora():
  valida = False
  while not valida:
    hora = input('> Horário [00h00]: ').strip()
    if ('h' not in hora) or (hora > '23h59') or ('7h30' < hora < '17h30'):
      print('Horário inválido')
    else:
      valida = True
  return hora     
  

def validar_telefone():
  valida = False
  while not valida:
    fone = input('> Telefone [(00) 00000-0000]: ').strip()
    fone = fone.replace('()', '')
    fone = fone.replace('-', '')
    fone = fone.replace(' ', '')
    if (len(fone) > 11) or (len(fone) < 11):
      print('Telefone inválido!')
    else: 
      valida = True
  return fone      


def validar_email():    
  valida = False
  while not valida:
    email = input('> E-mail: ').strip()  
    tam = len(email)   
    if (tam < 8) or ('@' and '.') not in email:
      print('E-mail inválido!')
    else:
      valida = True
  return email



def validar_code_animal(): 
  while True:
    codigo = input('> Crie um Código de 6 dígitos: ').strip()
    if len(codigo) > 6 or len(codigo) < 6:
      print('Código inválido!')
    elif codigo in animais:
      print('Código já cadastrado!')
    else: 
      return codigo



def validar_sexo():
  while True:
    sexo = input('> Sexo [M/F]: ')[0].strip().upper()
    if (sexo == 'M') or (sexo == 'F'):
      return sexo
      break      
    else:
      print('Sexo inválido!')