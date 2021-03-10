from aluno import Aluno


def cadastro_aluno():
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    aluno = Aluno(nome, matricula, endereco, cpf)
    return aluno

def mostrar_info(aluno):
    print(f"""\nInformações do aluno:
              \rNome: {aluno.nome}
              \rMatrícula: {aluno.matricula}
              \rEndereço: {aluno.endereco}
              \rCPF: {aluno.cpf}""")

def main():
    aluno = cadastro_aluno()
    mostrar_info(aluno)


if __name__ == "__main__":
    main()
