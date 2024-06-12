#Questionário sobre a pessoa a ser atendida
import re
import json
from datetime import datetime
import os

def validar_nome(nome):
    # Verifica se o nome possui apenas letras e espaços
    return all(char.isalpha() or char.isspace() for char in nome)

def validar_data(data):
     # Verifica se a data está no formato dd/mm/aaaa e se os valores são válidos
    if re.match(r'\d{2}/\d{2}/\d{4}', data):
        dia, mes, ano = map(int, data.split('/'))
        ano_atual = datetime.now().year
        
        # Verifica a quantidade máxima de dias de acordo com o mês
        dias_maximos = {
            1: 31, # Janeiro
            2: 29 if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else 28, # Fevereiro
            3: 31,  # Março
            4: 30,  # Abril
            5: 31,  # Maio
            6: 30,  # Junho
            7: 31,  # Julho
            8: 31,  # Agosto
            9: 30,  # Setembro
            10: 31,  # Outubro
            11: 30,  # Novembro
            12: 31   # Dezembro
        }

        return 1 <= dia <= dias_maximos.get(mes, 0) and 1 <= mes <= 12 and ano <= ano_atual
    else:
        return False

def validar_telefone(telefone):
    # Verifica se o telefone está no formato correto (00) 00000-0000
    return re.match(r'\(\d{2}\) \d{5}-\d{4}', telefone)

def validar_email(email):
     # Verifica se o email está em um formato válido
    return re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)

def validar_resposta_sim_nao(resposta):
    # Verifica se a resposta é 'sim' ou 'nao'
    return resposta.lower() in ['sim', 'nao']

def dados():
    paciente = {}
    paciente['Nome'] = input("Por favor, escreva o nome do paciente: ")
    while not validar_nome(paciente['Nome']):
        print("Nome inválido. Por favor, insira um nome válido.")
        paciente['Nome'] = input("Por favor, escreva o nome do paciente: ")

    paciente['Data de Nascimento'] = input("Qual a data de nascimento? Insira no formato dd/mm/aaaa ")
    while not validar_data(paciente['Data de Nascimento']):
        print("Data de nascimento inválida. Por favor, insira a data no formato correto.")
        paciente['Data de Nascimento'] = input("Qual a data de nascimento? Insira no formato dd/mm/aaaa ")

    paciente['Telefone'] = input("Digite um telefone para contato no formato (00) 00000-0000: ")
    while not validar_telefone(paciente['Telefone']):
        print("Telefone inválido. Por favor, insira o telefone no formato correto.")
        paciente['Telefone'] = input("Digite um telefone para contato no formato (00) 00000-0000: ")

    paciente['Email'] = input("Digite o e-mail: ")
    while not validar_email(paciente['Email']):
        print("Email inválido. Por favor, insira um email válido.")
        paciente['Email'] = input("Digite o e-mail: ")

    paciente['Responsável'] = input("Responsável (Se for você mesmo, escreva seu nome): ")
    while not validar_nome(paciente['Responsável']):
        print("Nome de responsável inválido. Por favor, insira um nome válido.")
        paciente['Responsável'] = input("Responsável (Se for você mesmo, escreva seu nome): ")

    return paciente

def questionario_anamnese():
    anamnese = {}
    anamnese['Hipertenso'] = input("Você é hipertenso? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Hipertenso']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Hipertenso'] = input("Você é hipertenso? (sim ou nao): ").strip()      
    if anamnese['Hipertenso'].lower() == 'sim':
        anamnese['Remédio para hipertensão'] = input("Qual remédio você utiliza? ")

    anamnese['Diabético'] = input("Você é diabético? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Diabético']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Diabético'] = input("Você é diabético? (sim ou nao): ").strip()
    if anamnese['Diabético'].lower() == 'sim':
        anamnese['Remédio para diabetes'] = input("Qual remédio você usa para diabetes? ")

    anamnese['Cardíaco'] = input("Você tem algum problema cardíaco? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Cardíaco']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Cardíaco'] = input("Você tem algum problema cardíaco? (sim ou nao): ").strip()
    if anamnese['Cardíaco'].lower() == 'sim':
        anamnese['Remédio para cardíaco'] = input("Qual remédio você usa para seu problema cardíaco? ")

    anamnese['Alergia'] = input("Você é alérgico a alguma medicação? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Alergia']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Alergia'] = input("Você é alérgico a alguma medicação? (sim ou nao): ").strip()
    if anamnese['Alergia'].lower() == 'sim':
        anamnese['Remedio que dá alergia'] = input("A que remédio você é alérgico? ")

    anamnese['Doença'] = input("Você tem alguma doença? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Doença']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Doença'] = input("Você tem alguma doença? (sim ou nao): ").strip()
    if anamnese['Doença'].lower() == 'sim':
        anamnese['Qual doença'] = input("Qual doença você tem? ")

    anamnese['Fumante'] = input("Você é fumante? (sim ou nao): ").strip().lower()
    while not validar_resposta_sim_nao(anamnese['Fumante']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Fumante'] = input("Você é fumante? (sim ou nao): ").strip().lower()

    anamnese['Cirurgia recente'] = input("Você teve alguma cirurgia recente? (sim ou nao): ").strip()
    while not validar_resposta_sim_nao(anamnese['Cirurgia recente']):
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
        anamnese['Cirurgia recente'] = input("Você teve alguma cirurgia recente? (sim ou nao): ").strip()
    if anamnese['Cirurgia recente'].lower() =='sim':
        anamnese['Cirurgia recente'] = input("Informe o nome da cirurgia: ")

    return anamnese

def fazer_procedimentos():
    procedimentos = [
        "Restauração", "Extração", "Ortodontia", "Prótese", "Limpeza", 
        "Faceta", "Lipo de papada", "Frenectomia", "Bichectomia", 
        "Gengivoplastia", "Botox", "Clareamento"
    ]

    procedimentos_feitos = {}

    for procedimento in procedimentos:
        realizar = input(f"Você deseja realizar o procedimento de {procedimento}? (sim ou nao): ").strip()
        if realizar.lower() == 'sim':
            if procedimento in ["Restauração", "Extração", "Ortodontia", "Prótese"]:
                dente = input(f"Especifique o dente a ser operado para o procedimento de {procedimento} (11-18, 21-28, 31-38 ou 41-48): ")
                procedimentos_feitos[procedimento] = dente
            else:
                procedimentos_feitos[procedimento] = "Geral"

    return procedimentos_feitos

def salvar_dados(paciente, anamnese, procedimentos_realizados):
    # Cria um dicionário contendo os dados do paciente, anamnese e procedimentos realizados
    dados_completos = {
        "Paciente": paciente,
        "Anamnese": anamnese,
        "Procedimentos Realizados": procedimentos_realizados
    }
    
    # Verifica se o arquivo JSON existe
    if os.path.exists('dados_pacientes.json'):
        # Se o arquivo existir, abre-o para leitura
        with open('dados_pacientes.json', 'r', encoding='utf-8') as file:
            # Carrega os dados existentes do arquivo
            dados_existentes = json.load(file)
        # Adiciona os novos dados à lista existente de dados  
        dados_existentes.append(dados_completos)
    else:
        # Se o arquivo não existir, cria uma lista contendo apenas os novos dados
        dados_existentes = [dados_completos]

    with open('dados_pacientes.json', 'w', encoding='utf-8') as file:
        # Escreve os dados no arquivo
        json.dump(dados_existentes, file, ensure_ascii=False, indent=4)

# Coleta dos dados do paciente
paciente = dados()

# Coleta das respostas do questionário de anamnese
anamnese = questionario_anamnese()

# Coleta dos procedimentos a serem realizados
procedimentos_realizados = fazer_procedimentos()

# Salva os dados coletados
salvar_dados(paciente, anamnese, procedimentos_realizados)
print("Dados do paciente salvos com sucesso.")
