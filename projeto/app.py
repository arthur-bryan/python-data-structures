from controllers import db
from controllers.sala import Sala
from time import sleep


def menu():
	funcao = int(input("""[+++ Morais Coworking - Gerenciamento de Salas +++]\n
						  \r[1] Cadastrar Sócio
						  \r[2] Realizar reserva de sala
						  \r[3] Remover reserva de sala
						  \r[4] Listar reservas do sócio
						  \r[5] Alterar nome do socio na reserva
						  \r[6] Alterar horário da reserva
						  \r[7] Listar salas disponíveis))
						  \r[0] Sair
						  \n\r--> """))
	return funcao

def main():
	try:
		funcao = menu()
	except ValueError:
		print("[!] Opção inválida!\n\n\n")
		sleep(1)
		main()
	else:
		if funcao >=0 and funcao <= 7:
			if funcao == 1:
				db.cadastrar_socio()
			elif funcao == 2:
				db.reservar_sala(socio)
			elif funcao == 3:
				db.remover_reserva(socio)
			elif funcao == 4:
				db.listar_reservas(socio)
			elif funcao == 5:
				db.alterar_nome(socio)
			elif funcao == 6:
				db.alterar_horario_reserva(socio)
			elif funcao == 7:
				db.listar_salas_disponiveis()
			else:
				print("[-] Saindo...")
				sleep(1)
				exit(0)
		else:
			print("[!] Opção inválida!\n\n\n")
			sleep(1)
			main()

if __name__ == '__main__':
	main()
