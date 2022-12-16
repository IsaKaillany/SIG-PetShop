import os
from dicionarios import *
from animais import *
from servicos import *
from proprietarios import *

def menu_relatorios():
    os.system('cls')
    print('===================================')
    print('==== 🧾 R E L A T Ó R I O S 🧾 ====')
    print('===================================')
    print()
    print('\t1 - Proprietários')
    print('\t2 - Animais')
    print('\t3 - Serviços prestados')
    print('\t0 - Voltar ao menu')
    print()
    print('=======================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao


def relatorios_prop():
    for i in proprietarios:
        print('=' * 30)
        print('Nome:', proprietarios[i][0])
        print('E-mail:', proprietarios[i][1])
        print('Telefone:', proprietarios[i][2])
        print('Nome do Animal:', proprietarios[i][3])
        print('=' * 30)
        print()
    input('Tecle ENTER para continuar!')


def relatorios_animais():
    for i in animais:
        print('='*30)
        print('Nome:', animais[i][0])
        print('Tipo:', animais[i][1])
        print('Nascimento:', animais[i][2])
        print('Raça:', animais[i][3])
        print('Sexo:', animais[i][4])
        print('='*30)
        print()
    input('Tecle ENTER para continuar!')


def relatorios_servico():
    for i in servicos:
        print('='*30)
        print('Nome do Animal:', servicos[i][1])
        print('Data:', servicos[i][2])
        print('Horário:', servicos[i][3])
        nome_servico = tupla_servicos[servicos[i][4]]
        print('Serviço:', nome_servico)
        print('='*30)
        print()
    input('Tecle ENTER para continuar!')


def modulo_relatorios():
    opcao = menu_relatorios()
    while opcao != '0':
        if opcao == '1':
            relatorios_prop()
        elif opcao == '2':
            relatorios_animais()
        elif opcao == '3':
            relatorios_servico()
        else:
            print('Opção inválida!')
        opcao = menu_relatorios()