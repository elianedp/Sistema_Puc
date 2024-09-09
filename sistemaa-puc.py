

import json

# Função para salvar os dados em um arquivo JSON
def salvar_dados(dados, arquivo):
    with open(arquivo, "w") as f:
        json.dump(dados, f)

# Função para carregar os dados de um arquivo JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para incluir um novo registro na lista e salvar no arquivo
def incluir_registro(lista, registro, arquivo):
    lista.append(registro)
    salvar_dados(lista, arquivo)
    nome_registro = registro.get('nome', 'Registro')
    print(f"{nome_registro} adicionado com sucesso!")

# Função para listar registros de forma organizada
def listar_registros(lista):
    if not lista:
        print("Não há registros cadastrados.")
    else:
        print("\nLista de Registros:")
        for i, item in enumerate(lista, start=1):
            print(f"Registro {i}:")
            for chave, valor in item.items():
                print(f"  {chave}: {valor}")
            print("-" * 20)

# Função para editar um registro com base no índice fornecido
def editar_registro(lista, novo_registro, indice, arquivo):
    if indice < 0 or indice >= len(lista):
        print("Índice inválido. Tente novamente.")
        return

    lista[indice] = novo_registro
    salvar_dados(lista, arquivo)
    print("Registro editado com sucesso!")

# Função para excluir um registro usando tanto índice quanto código
def excluir_registro(lista_registros, chave, nome_arquivo):
    # Exibir registros antes da exclusão
    for i, registro in enumerate(lista_registros):
        print(f"{i} - Código: {registro['codigo']}, Nome: {registro['nome']}")

    # Tentar excluir pelo índice
    try:
        indice = int(chave)
        if 0 <= indice < len(lista_registros):
            del lista_registros[indice]
            print("Registro excluído com sucesso pelo índice!")
            salvar_dados(lista_registros, nome_arquivo)  # Salvar no arquivo JSON
            return
    except ValueError:
        pass

    # Tentar excluir pelo código
    for registro in lista_registros:
        if str(registro['codigo']) == str(chave):
            lista_registros.remove(registro)
            print("Registro excluído com sucesso pelo código!")
            salvar_dados(lista_registros, nome_arquivo)  # Salvar no arquivo JSON
            return

    print("Código ou índice não encontrado. Nenhum registro foi excluído.")

# Função para validar a opção do menu principal
def validar_opcao(opcao):
    opcoes_validas = ["1", "2", "3", "4", "5", "6"]
    return opcao in opcoes_validas

# Função para validar a operação do menu de operações
def validar_operacao(operacao):
    operacoes_validas = ["1", "2", "3", "4", "5"]
    return operacao in operacoes_validas

# Função para validar CPF (deve ter 11 dígitos e ser numérico)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Função principal para controlar o fluxo do sistema
def main():
    # Carregar os dados de arquivos JSON para listas específicas
    dados_estudantes = carregar_dados("dados_estudantes.json")
    dados_professores = carregar_dados("dados_professores.json")
    dados_disciplinas = carregar_dados("dados_disciplinas.json")
    dados_turmas = carregar_dados("dados_turmas.json")
    dados_matriculas = carregar_dados("dados_matriculas.json")

    # Loop principal do sistema
    while True:
        print("Menu Principal:")
        print("1. Estudantes")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "6":
            print("Saindo...")
            break

        if opcao_principal in ["1", "2", "3", "4", "5"]:
            print(f"\nOpção selecionada: {opcao_principal}")
            print("\nMenu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Editar")
            print("4. Excluir")
            print("5. Voltar ao menu principal")
            opcao_operacoes = input("Escolha uma operação: ")

            while not validar_operacao(opcao_operacoes):
                print("Operação inválida. Tente novamente.")
                opcao_operacoes = input("Escolha uma operação: ")

            if opcao_operacoes == "1":  # Incluir
                try:
                    if opcao_principal == "1":  # Estudantes
                        cpf = input("Digite o CPF (11 dígitos): ")
                        while not validar_cpf(cpf):
                            print("CPF inválido. Deve conter 11 dígitos numéricos.")
                            cpf = input("Digite o CPF (11 dígitos): ")

                        novo_registro = {
                            "codigo": int(input("Digite o código: ")),
                            "nome": input("Digite o nome do estudante: "),
                            "cpf": cpf
                        }
                        incluir_registro(dados_estudantes, novo_registro, "dados_estudantes.json")
                    elif opcao_principal == "2":  # Professores
                        cpf = input("Digite o CPF (11 dígitos): ")
                        while not validar_cpf(cpf):
                            print("CPF inválido. Deve conter 11 dígitos numéricos.")
                            cpf = input("Digite o CPF (11 dígitos): ")

                        novo_registro = {
                            "codigo": int(input("Digite o código: ")),
                            "nome": input("Digite o nome do professor: "),
                            "cpf": cpf
                        }
                        incluir_registro(dados_professores, novo_registro, "dados_professores.json")
                    elif opcao_principal == "3":  # Disciplinas
                        novo_registro = {
                            "codigo": int(input("Digite o código: ")),
                            "nome": input("Digite o nome da disciplina: ")
                        }
                        incluir_registro(dados_disciplinas, novo_registro, "dados_disciplinas.json")
                    elif opcao_principal == "4":  # Turmas
                        novo_registro = {
                            "codigo": int(input("Digite o código da turma: ")),
                            "nome_disciplina": input("Digite o nome da disciplina: ")
                        }
                        incluir_registro(dados_turmas, novo_registro, "dados_turmas.json")
                    elif opcao_principal == "5":  # Matrículas
                        novo_registro = {
                            "codigo_turma": input("Digite o nome da turma: "),
                            "codigo_estudante": int(input("Digite o código do estudante: "))
                        }
                        incluir_registro(dados_matriculas, novo_registro, "dados_matriculas.json")
                except ValueError:
                    print("Entrada inválida. Certifique-se de inserir números nos campos de código.")

            elif opcao_operacoes == "2":  # Listar
                if opcao_principal == "1":
                    listar_registros(dados_estudantes)
                elif opcao_principal == "2":
                    listar_registros(dados_professores)
                elif opcao_principal == "3":
                    listar_registros(dados_disciplinas)
                elif opcao_principal == "4":
                    listar_registros(dados_turmas)
                elif opcao_principal == "5":
                    listar_registros(dados_matriculas)

            elif opcao_operacoes == "3":  # Editar
                indice = int(input("Digite o número do registro a ser editado: ")) - 1
                if (opcao_principal == "1" and 0 <= indice < len(dados_estudantes)) or \
                   (opcao_principal == "2" and 0 <= indice < len(dados_professores)) or \
                   (opcao_principal == "3" and 0 <= indice < len(dados_disciplinas)) or \
                   (opcao_principal == "4" and 0 <= indice < len(dados_turmas)) or \
                   (opcao_principal == "5" and 0 <= indice < len(dados_matriculas)):
                    if opcao_principal == "1":  # Estudantes
                        novo_registro = {
                            "codigo": int(input("Digite o novo código: ")),
                            "nome": input("Digite o novo nome: "),
                            "cpf": input("Digite o novo CPF: ")
                        }
                        editar_registro(dados_estudantes, novo_registro, indice, "dados_estudantes.json")
                    elif opcao_principal == "2":  # Professores
                        novo_registro = {
                            "codigo": int(input("Digite o novo código: ")),
                            "nome": input("Digite o novo nome: "),
                            "cpf": input("Digite o novo CPF: ")
                        }
                        editar_registro(dados_professores, novo_registro, indice, "dados_professores.json")
                    elif opcao_principal == "3":  # Disciplinas
                        novo_registro = {
                            "codigo": int(input("Digite o novo código: ")),
                            "nome": input("Digite o novo nome: ")
                        }
                        editar_registro(dados_disciplinas, novo_registro, indice, "dados_disciplinas.json")
                    elif opcao_principal == "4":  # Turmas
                        novo_registro = {
                            "codigo": int(input("Digite o novo código da turma: ")),
                            "nome_disciplina": input("Digite o novo nome da disciplina: ")
                        }
                        editar_registro(dados_turmas, novo_registro, indice, "dados_turmas.json")
                    elif opcao_principal == "5":  # Matrículas
                        novo_registro = {
                            "codigo_turma": input("Digite o novo nome da turma: "),
                            "codigo_estudante": int(input("Digite o novo código do estudante: "))
                        }
                        editar_registro(dados_matriculas, novo_registro, indice, "dados_matriculas.json")

            elif opcao_operacoes == "4":  # Excluir
                entrada = input("Digite o índice ou o código do registro a ser excluído: ")
                if opcao_principal == "1":
                    excluir_registro(dados_estudantes, entrada, "dados_estudantes.json")
                elif opcao_principal == "2":
                    excluir_registro(dados_professores, entrada, "dados_professores.json")
                elif opcao_principal == "3":
                    excluir_registro(dados_disciplinas, entrada, "dados_disciplinas.json")
                elif opcao_principal == "4":
                    excluir_registro(dados_turmas, entrada, "dados_turmas.json")
                elif opcao_principal == "5":
                    excluir_registro(dados_matriculas, entrada, "dados_matriculas.json")

if __name__ == "__main__":
    main()
