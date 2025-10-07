def verificar_pacotes(nome_pacote):
	try:
		import os
		import sys
		import importlib
		PACOTE = importlib.util.find_spec(nome_pacote)
		if PACOTE is not None:
			print("Pacote já está instalado.")
			os.system(f"pip install --upgrade {nome_pacote}")

		else:
			try:
				os.system(f"pip install {nome_pacote}")

			except Exception as e:
				print("Ocorreu um erro ao instalar o pacote: ", e)

	except Exception as e:
		print(e)
