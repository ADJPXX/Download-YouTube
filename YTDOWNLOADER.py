import pytubefix        #pip install pytubefix
import ffmpeg           #pip install ffmpeg-python


def lerstr(msg):
	while True:
		try:
			string = str(input(msg))
		except:
			pass
		else:
			return string


def lerint(msg):
	while True:
		try:
			inteiro = int(input(msg).strip())
		except:
			pass
		else:
			return inteiro


def clear():
	from os import system
	if system == "nt":
		system("clear")
	else:
		system("cls")


def listaresolucoes(video):
	RES = video.streams.filter(only_video=True).order_by('resolution').desc()

	resolucoes = []
	for resolucao in RES:
		if resolucao.resolution:
			resolucoes.append(resolucao.resolution)
	resolucoes = sorted(list(set(resolucoes)), key=lambda x: int(x.replace("p","")), reverse=True)
	return resolucoes


def escolherresolucao(opcoesderes):
	for i, opcao in enumerate(opcoesderes, start=1):
		print(f"[ {i} ] {opcao}")

	while True:
		op = lerint("Qual resolucao você quer baixar o vídeo? ")
		if 1 <= op <= len(opcoesderes):
			return opcoesderes[op - 1]
		else:
			print("Escolha uma opção correta.")


def baixarmp4(LINK):

	clear()
	try:
		import os
		import time
		YT = pytubefix.YouTube(LINK)

		PATH = "C:/Users/Adrie/Downloads" #COLOQUE O DIRETORIO DE DOWNLOAD AQUI

		RESOLUCOES = listaresolucoes(YT)
		RESOLUCAO_ESCOLHIDA = escolherresolucao(RESOLUCOES)

		YT_VIDEO = YT.streams.filter(only_video=True, mime_type="video/mp4", res=f"{RESOLUCAO_ESCOLHIDA}").order_by('bitrate').desc().first()
		YT_AUDIO = YT.streams.filter(only_audio=True, mime_type="audio/mp4").order_by('bitrate').desc().first()

		print(f"RESOLUÇÃO ESCOLHIDA PARA DOWNLOAD {RESOLUCAO_ESCOLHIDA}")

		VIDEO_FILE = YT_VIDEO.download(PATH, filename="video.mp4")
		AUDIO_FILE = YT_AUDIO.download(PATH, filename="audio.mp4")

		NOVO_TITULO = removercaracteresinvalidos(YT.title)

		video_input = ffmpeg.input(VIDEO_FILE)
		audio_input = ffmpeg.input(AUDIO_FILE)
		output_file = f"{PATH}/{NOVO_TITULO}.mp4"

		ffmpeg.output(video_input, audio_input, output_file, vcodec='hevc_nvenc', acodec='aac', preset='p7', strict='experimental').run(overwrite_output=True)

		clear()

		print("DOWNLOAD COMPLETO.\n")

		os.remove(f"{PATH}/video.mp4")
		os.remove(f"{PATH}/audio.mp4")

	except Exception as e:
		print(f"OCORREU UM ERRO! TENTE NOVAMENTE {str(e)}")


def removercaracteresinvalidos(nome):
	import re

	str(nome)
	TITULO = re.sub(r'[\\/*?:"<>|]', "", nome)
	return TITULO


def baixarmp3(LINK):
	clear()
	try:
		PATH = "C:/Users/Adrie/Downloads" #COLOQUE SEU DIRETORIO AQUI
		YT = pytubefix.YouTube(LINK)
		AUDIO = YT.streams.filter(only_audio=True).order_by('abr').desc().first()
		AUDIO.download(PATH, filename=f"{YT.title}.mp3")

		print("DOWNLOAD COMPLETO.")

	except Exception as e:
		print(f"OCORREU UM ERRO! TENTE NOVAMENTE {str(e)}")


def main():
	while True:
		op = lerint("O QUE VOCÊ DESEJA?\n[ 1 ]BAIXAR MP3 (APENAS ÁUDIO)\n[ 2 ]BAIXAR MP4 (ÁUDIO E VÍDEO --- APENAS A RESOLUÇÃO 360p ESTÁ DISPONÍVEL)\n[ 0 ]SAIR\nSUA ESCOLHA: ")
		if op == 0:
			clear()
			print("OBRIGADO POR O PROGRAMA")
			break

		elif op == 1:
			clear()
			while True:
				print("DIGITE 'SAIR' PARA PARAR O PROGRAMA")
				LINK = lerstr("DIGITE O LINK DO VÍDEO QUE VOCÊ QUER BAIXAR: ").strip()
				if LINK == "sair" or LINK == "SAIR" or LINK == "Sair":
					break

				baixarmp3(LINK)

		elif op == 2:
			clear()
			while True:
				print("DIGITE 'SAIR' PARA PARAR O PROGRAMA")
				LINK = lerstr("DIGITE O LINK DO VÍDEO QUE VOCÊ QUER BAIXAR: ").strip()
				if LINK == "sair" or LINK == "SAIR" or LINK == "Sair":
					break

				baixarmp4(LINK)


if __name__ == "__main__":
	main()

