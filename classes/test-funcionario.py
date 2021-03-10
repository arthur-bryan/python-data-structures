from funcionario import Funcionario
from datetime import datetime



def cadastrar_funcionario():
	print(" ------ Cadastro de funcionário ------")
	nome = input("Nome: ")
	departamento = input("Departamento: ")
	salario = float(input("Salário: "))
	data_entrada = datetime.now().strftime('%d/%m/%Y')
	rg = input("RG: ")
	funcionario = Funcionario(nome, departamento, salario, data_entrada, rg)
	return funcionario


def main():
	print("\n\n\nExecutando main() - testando métodos da classe Funcionario\n")
	funcionario = cadastrar_funcionario()
	print(funcionario.get_salario())
	funcionario.set_salario(6300)
	print(funcionario.get_salario())
	funcionario.receber_aumento('15')
	print(funcionario.get_salario())
	print(funcionario.calcular_ganho_anual())
	print(funcionario.data_entrada)
	funcionario.mudar_departamento('ADM', 'TI')
	print(funcionario.departamento)

if __name__ == '__main__':
	main()
