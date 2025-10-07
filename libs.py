def verificar_pacotes(nome_pacote):
	try:
		import os
		import sys
		import importlib

		PACOTE = importlib.util.find_spec(nome_pacote)

		if PACOTE is not None:
			os.system("cls")
			print(f'[✓] O pacote "{nome_pacote}" já está instalado.\nVou verificar as atualizações e se necessario atualizar.')
			os.system(f'pip install --upgrade {nome_pacote}')

		else:
			try:
				os.system("cls")
				print(f"[+]Instalando o pacote {nome_pacote}...")
				os.system(f"pip install {nome_pacote}")

			except Exception as e:
				os.system("cls")
				print("Ocorreu um erro ao instalar o pacote: ", e)

	except Exception as e:
		print(e)
