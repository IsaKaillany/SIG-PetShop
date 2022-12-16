import os
import pickle
from validacoes import *
from dicionarios import *

servicos = {}
#### Recuperando os dados do arquivo ####
try:
    arq_servicos = open("servicos.dat", "rb")
    servicos = pickle.load(arq_servicos)
    arq_servicos.close()
except:
    arq_servicos = open("servicos.dat", "wb")
    arq_servicos.close()


def menu_servicos():
    os.system('cls')
    print('=============================================')
    print('=========== 🧼 S E R V I Ç O S ✂️  ===========')
    print('=============================================')
    print()
    print('\t1 - Cadastrar')
    print('\t2 - Buscar')
    print('\t3 - Atualizar')
    print('\t4 - Excluir')
    print('\t0 - Voltar ao menu')
    print()
    print('=============================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao


def tela_servicos():
    print('=============================================')
    print()
    print('\t1 - Banho')
    print('\t2 - Hidratação')
    print('\t3 - Tosa')
    print('\t4 - Desembaraçamento')
    print('\t5 - Tingimento dos pelos')
    print('\t6 - Escovação dos dentes')
    print('\t7 - Limpeza de ouvido')
    print('\t8 - Corte de unhas')
    print()
    print('=============================================')
    opcao = input('>>> Opção ').strip()
    print()
    return opcao


def cadastrar_servico():
    servico = tela_servicos()
    while True:
        cpf = input('> CPF: ').strip()
        if validar_cpf(cpf):
            break
        else:
            print('CPF inválido!')
    nome = input('> Nome do animal: ').strip().capitalize()
    print('> Escolha a data <')
    data = validar_data()
    print('> Horário de funcionamento: 7h30 - 17h30 <')
    hora = validar_hora()
    code = str(data.replace('/', '') + hora.replace('h', ''))
    print('> Anote seu código, por favor <')
    print('> Código do serviço:', code)
    servicos[code] = [cpf, nome, data, hora, int(servico)]

    #### Gravando os dados no arquivo ####
    arq_servicos = open("servicos.dat", "wb")
    pickle.dump(servicos, arq_servicos)
    arq_servicos.close()
    print()
    print('Cadastro Concluído!')
    input('Tecle ENTER para continuar!')


def buscar_servico():
    code = input('Informe o código do serviço: ').strip()
    if code in servicos:
        print('> CPF:', servicos[code][0])
        print('> Nome do animal:', servicos[code][1])
        print('> Data:', servicos[code][2])
        print('> Horário:', servicos[code][3])
        nome_servico = tupla_servicos[servicos[code][4]]
        print('> Serviço:', nome_servico)
    else:
        print('Código inválido!')
    print()
    input('Tecle ENTER para continuar!')


def tela1_atualizar_s():
    os.system('cls')
    print('=============================================')
    print('========= 🔄 A T U A L I Z A R 🔄 =========')
    print('=============================================')
    print()
    print('\t1 - Tudo')
    print('\t2 - CPF')
    print('\t3 - Nome do animal')
    print('\t4 - Data')
    print('\t5 - Horário')
    print('\t6 - Serviço')
    print()
    print('=============================================')
    resp = input('O que você quer modificar: ').strip()
    return resp


def tela2_atualizar_s(code, resp):
    if resp == '1':
        while True:
            cpf = input('> Novo CPF: ').strip()
            if validar_cpf(cpf):
                break
            else:
                print('CPF inválido!')
        nome = input('> Novo Nome do Animal: ').strip().capitalize()
        print('> Nova Data <')
        data = validar_data()
        print('> Horário de funcionamento: 7h30 - 17h30 <')
        hora = validar_hora()
        print()
        print('> Serviço <')
        opcao = tela_servicos()
        servico = int(opcao)
        servicos[code] = [cpf, nome, data, hora, servico]
    elif resp == '2':
        while True:
            cpf = input('> Novo CPF: ').strip()
            if validar_cpf(cpf):
                servicos[code][0] = cpf
                break
            else:
                print('CPF inválido!')
    elif resp == '3':
        servicos[code][1] = input(
            '> Novo Nome do Animal: ').strip().capitalize()
    elif resp == '4':
        print('> Nova Data <')
        servicos[code][2] = validar_data()
    elif resp == '5':
        print('> Horário de funcionamento: 7h30 - 17h30 <')
        servicos[code][3] = validar_hora()
    elif resp == '6':
        print()
        opcao = tela_servicos()
        servicos[code][4] = int(opcao)
    else:
        print('Opção inválida!')
    print()
    print('Atualização Concluída!')


def atualizar_servico():
    code = input('Informe o código do serviço: ').strip()
    if code in servicos:
        resp = tela1_atualizar_s()
        tela2_atualizar_s(code, resp)
    else:
        print('Código não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def excluir_servico():
    code = input('Informe o código do serviço: ').strip()
    if code in servicos:
        del servicos[code]
        print('Cadastro de serviço excluído com sucesso!')
    else:
        print('Código não encontrado!')
    print()
    input('Tecle ENTER para continuar!')


def modulo_servicos():
    opcao = menu_servicos()
    while opcao != '0':
        if opcao == '1':
            cadastrar_servico()
        elif opcao == '2':
            buscar_servico()
        elif opcao == '3':
            atualizar_servico()
        elif opcao == '4':
            excluir_servico()
        else:
            print('Opção inválida!')
        opcao = menu_servicos()
