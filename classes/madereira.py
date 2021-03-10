from moldura import Moldura



def comprar_moldura():
	base = float(input("Base (cm): "))
	altura = float(input("Altura (cm): "))
	espessura = float(input("Espessura (cm): "))
	tipo = int(input("Tipo de madeira (1/2/3): "))
	moldura = Moldura(base, altura, espessura, tipo)
	print(f"Uma moldura com área {moldura.area}/m² custa R$ {moldura.valor:.2f}.")


def main():
	comprar_moldura()


if __name__ == '__main__':
	main()
