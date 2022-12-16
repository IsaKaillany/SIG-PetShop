import os
import pickle
from validacoes import *
from dicionarios import *

proprietarios = {}
#### Recuperando os dados do arquivo ####
try:
    arq_prop = open("proprietarios.dat", "rb")
    proprietarios = pickle.load(arq_prop)
    arq_prop.close()
except:
    arq_prop = open("proprietarios.dat", "wb")
    arq_prop.close()

def menu_proprietarios():
    os.system('cls')
    print('=============================================')
    print('======= 🧍 P R O P R I E T Á R I O S 🧍 =======')
    print('=============================================')
    print()
    print('\t1 - Cadastrar dados')
    print('\t2 - Buscar dados')
    print('\t3 - Atualizar dados')
    print('\t4 - Excluir dados')
    print('\t0 - Voltar ao menu')
    print()
    print('=============================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao


def cadastrar_proprietario():
    nome = input('> Nome: ').strip().capitalize()
    email = validar_email()
    fone = validar_telefone()
    animal = input('> Nome do animal: ').strip().capitalize()
    # CPF
    while True:
        cpf = input('> CPF: ').strip()
        if(validar_cpf(cpf)):
            if cpf not in proprietarios:
                proprietarios[cpf] = [nome, email, fone, animal]
                print('Cadastro Concluído!')
                break
            elif (cpf in proprietarios):
                print('CPF já registrado, tente novamente!')
        else:
            print('CPF inválido!')

    #### Gravando os dados no arquivo ####
    arq_prop = open("proprietarios.dat", "wb")
    pickle.dump(proprietarios, arq_prop)
    arq_prop.close()
    print()
    input('Tecle ENTER para continuar!')


def buscar_proprietario():
    cpf = input('Informe o CPF, por favor: ').strip()
    if cpf in proprietarios:
        print('> Nome:', proprietarios[cpf][0])
        print('> E-mail:', proprietarios[cpf][1])
        print('> CPF:', cpf)
        print('> Telefone:', proprietarios[cpf][2])
        print('> Nome do animal:', proprietarios[cpf][3])
    else:
        print('CPF não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def tela1_atualizar_p():
    os.system('cls')
    print('=============================================')
    print('========= 🔄 A T U A L I Z A R 🔄 =========')
    print('=============================================')
    print()
    print('\t1 - Tudo')
    print('\t2 - Nome')
    print('\t3 - E-mail')
    print('\t4 - Telefone')
    print('\t5 - Nome do Animal')
    print()
    print('=============================================')
    resp = input('O que você quer modificar: ').strip()
    return resp


def tela2_atualizar_p(cpf, resp):
    if resp == '1':
        print()
        nome = input('> Novo Nome: ').strip().capitalize()
        email = validar_email()
        fone = validar_telefone()
        animal = input('> Novo Nome do Animal: ').strip().capitalize()
        proprietarios[cpf] = [nome, email, fone, animal]
    elif resp == '2':
        proprietarios[cpf][0] = input('> Novo Nome: ').strip().capitalize()
    elif resp == '3':
        proprietarios[cpf][1] = validar_email()
    elif resp == '4':
        proprietarios[cpf][2] = validar_telefone()
    elif resp == '5':
        proprietarios[cpf][3] = input(
            '> Novo Nome do Animal: ').strip().capitalize()
    else:
        print('Opção inválida!')
    print('Atualização Concluída!')


def atualizar_proprietario():
    cpf = input('CPF do proprietário a atualizar: ').strip()
    if cpf in proprietarios:
        resp = tela1_atualizar_p()
        tela2_atualizar_p(cpf, resp)
    else:
        print('CPF não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def excluir_proprietario():
    cpf = input('CPF do proprietário a excluir: ').strip()
    if cpf in proprietarios:
        del proprietarios[cpf]
        print('Cadastro de proprietário excluído com sucesso!')
    else:
        print('CPF não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def modulo_proprietario():
    opcao = menu_proprietarios()
    while opcao != '0':
        if opcao == '1':
            cadastrar_proprietario()
        elif opcao == '2':
            buscar_proprietario()
        elif opcao == '3':
            atualizar_proprietario()
        elif opcao == '4':
            excluir_proprietario()
        else:
            print('Opção inválida!')
        opcao = menu_proprietarios()




