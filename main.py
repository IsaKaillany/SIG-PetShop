import os
import pickle
from validacoes import *
from animais import *
from dicionarios import *
from servicos import *
from proprietarios import *
from relatorios import *

def menu_principal():
    os.system('cls')
    print('=============================================')
    print('======== M E N U   P R I N C I P A L ========')
    print('=============================================')
    print()
    print('\t1 - Serviços')
    print('\t2 - Proprietários')
    print('\t3 - Animais')
    print('\t4 - Relatórios')
    print('\t5 - Informações sobre o programa')
    print('\t0 - Finalizar Programa')
    print()
    print('=============================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao

#####################
#### INFORMAÇÕES ####
#####################


def modulo_info():
    os.system('cls')
    print('=============================================')
    print('================ E Q U I P E ================')
    print('=============================================')
    print()
    print('> Felipe Souza Benício da Silva ')
    print('> Matrícula: 20220043343')
    print()
    print('> Isa Kaillany Soares Pereira')
    print('> Matrícula: 20220043568')
    print()
    print('=============================================')
    print('============== O B J E T I V O ==============')
    print('=============================================')
    print()
    print('''     O presente projeto tem como objetivo 
     apresentar um sistema de agendamento 
     de consultas para um Pet-Shop.
    ''')
    print('=============================================\n')

#### Navegação do programa ####
opcao = menu_principal()
while opcao != '0':
    if opcao == '1':
        modulo_servicos()
    elif opcao == '2':
        modulo_proprietario()
    elif opcao == '3':
        modulo_animais()
    elif opcao == '4':
        modulo_relatorios()
    elif opcao == '5':
        modulo_info()
    else:
        print('==== Opção inválida ====')
    input("Tecle ENTER para continuar!")
    opcao = menu_principal()

print('=====================')
print('Obrigado pelo acesso.')
print('\tVolte Sempre!')
print('=====================')
