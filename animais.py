import os
import pickle
from validacoes import *
from dicionarios import *

animais = {}
#### Recuperando os dados do arquivo ####
try:
    arq_animais = open("animais.dat", "rb")
    animais = pickle.load(arq_animais)
    arq_animais.close()
except:
    arq_animais = open("animais.dat", "wb")
    arq_animais.close()

def menu_animais():
    os.system('cls')
    print('=============================================')
    print('============ 🐾 A N I M A I S 🐾 ============')
    print('=============================================')
    print()
    print('\t1 - Cadastrar Dados')
    print('\t2 - Buscar Cadastro')
    print('\t3 - Atualizar Cadastro')
    print('\t4 - Excluir Cadastro')
    print('\t0 - Voltar ao menu')
    print()
    print('=============================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao


def cadastrar_animal():
    nome = input('> Nome: ').strip().capitalize()
    tipo = input('> Tipo de Animal: ').strip().capitalize()
    print('> Data de nascimento <')
    data = validar_data_nasc()
    raca = input('> Raça do animal: ').strip().capitalize()
    sexo = validar_sexo()
    codigo = validar_code_animal()
    animais[codigo] = [nome, tipo, data, raca, sexo]

    #### Gravando os dados no arquivo ####
    arq_animais = open("animais.dat", "wb")
    pickle.dump(animais, arq_animais)
    arq_animais.close()
    print()
    print('Cadastro Concluído!')
    input('Tecle ENTER para continuar!')


def buscar_animal():
    codigo = input('Informe o código do animal: ').strip()
    if codigo in animais:
        print('> Nome:', animais[codigo][0])
        print('> Tipo de Animal:', animais[codigo][1])
        print('> Data de Nascimento:', animais[codigo][2])
        print('> Raça do animal:', animais[codigo][3])
        print('> Sexo:', animais[codigo][4])
        print('> Código do animal:', codigo)
    else:
        print('Código não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def tela1_atualizar_a():
    os.system('cls')
    print('=============================================')
    print('========= 🔄 A T U A L I Z A R 🔄 =========')
    print('=============================================')
    print()
    print('\t1 - Tudo')
    print('\t2 - Nome')
    print('\t3 - Tipo de Animal')
    print('\t4 - Data de Nascimento')
    print('\t5 - Raça')
    print('\t6 - Sexo')
    print()
    print('=============================================')
    resp = input('O que você quer modificar: ').strip()
    return resp


def tela2_atualizar_a(codigo, resp):
    if resp == '1':
        print()
        nome = input('> Novo Nome: ').strip().capitalize()
        tipo = input('> Novo Tipo de Animal: ').strip().capitalize()
        print('> Nova Data de Nascimento <')
        data = validar_data_nasc()
        raca = input('> Nova Raça: ').strip().capitalize()
        sexo = validar_sexo()
        animais[codigo] = [nome, tipo, data, raca, sexo]
    elif resp == '2':
        animais[codigo][0] = input('> Novo Nome: ').strip().capitalize()
    elif resp == '3':
        animais[codigo][1] = input(
            '> Novo Tipo de Animal: ').strip().capitalize()
    elif resp == '4':
        print('> Nova Data de Nascimento <')
        animais[codigo][2] = validar_data_nasc()
    elif resp == '5':
        animais[codigo][3] = input('> Nova Raça: ').strip().capitalize()
    elif resp == '6':
        animais[codigo][4] = validar_sexo()
    else:
        print('Opção inválida!')
    print('Atualização Concluída!')


def atualizar_animal():
    codigo = input('Código do animal a atualizar: ').strip()
    if codigo in animais:
        resp = tela1_atualizar_a()
        tela2_atualizar_a(codigo, resp)
    else:
        print('Código não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def excluir_animal():
    codigo = input('Código do animal a excluir: ').strip()
    if codigo in animais:
        del animais[codigo]
        print('Cadastro de animal excluído com sucesso!')
    else:
        print('Código não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def modulo_animais():
    opcao = menu_animais()
    while opcao != '0':
        if opcao == '1':
            cadastrar_animal()
        elif opcao == '2':
            buscar_animal()
        elif opcao == '3':
            atualizar_animal()
        elif opcao == '4':
            excluir_animal()
        else:
            print('Opção inválida!')
        opcao = menu_animais()





