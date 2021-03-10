from evento import Evento
from queue import Queue
from time import sleep
from random import randint, choice

eventos = ['Colisão', 'Atualização da Tela', 'Particulas',
           'Lógica do Jogo', 'Inteligência Artificial', 'Simulação Física',
           'Teclado', 'Mouse', 'Internet']

def gerar_eventos():
	fila_de_eventos = Queue()
	for _, i in enumerate(range(randint(1, 20))):
		evento = Evento(choice(eventos))
		evento.set_priority()
		print(f"[{_+1}] Evento gerado: {evento}.")
		sleep(0.2)
		fila_de_eventos.insert(evento)
	print(f"[+] ----- > Gerados: {len(fila_de_eventos)} eventos.\n\n")
	sleep(0.5)
	return fila_de_eventos

def organizar_por_prioridade(eventos):
	fila_ordenada = Queue()
	for i in range(3):
		for elemento in eventos.data:
			if elemento.get_priority() == (0, i):
				fila_ordenada.insert(elemento)
	for i in range(3):
		for elemento in eventos.data:
			if elemento.get_priority() == (1, i):
				fila_ordenada.insert(elemento)
	for i in range(3):
		for elemento in eventos.data:
			if elemento.get_priority() == (2, i):
				fila_ordenada.insert(elemento)
	return fila_ordenada

rodadas_de_eventos = 4
for i in range(rodadas_de_eventos):
	eventos_gerados = gerar_eventos()
	fila_ordenada = organizar_por_prioridade(eventos_gerados)
	for evento in range(len(fila_ordenada)):
		removido = fila_ordenada.remove()
		print(f"[-]----------O evento {removido} foi processado!")
		sleep(0.2)
	print("[-] ----> Os eventos foram processados!\n\n")
	print("--------------------------------------------------------------------------")
	sleep(0.5)

