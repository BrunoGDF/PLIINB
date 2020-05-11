import speech_recognition as sr #importa biblioteca speech_recognition
from gtts import gTTS           #importa biblioteca gTTS
import os                       #importa biblioteca do sistema operacional 

recognizer = sr.Recognizer()    #inicializa reconhecimento de voz
microphone = sr.Microphone()    #inicializa microphone

with microphone as source: 
	recognizer.adjust_for_ambient_noise(source)     #calibra o microfone
	audio = recognizer.listen(source)				#escuta o microfone				

retornoAudio = recognizer.recognize_google(audio,language='pt-BR') #interpreta o audio utilizando o idioma português brasileiro

with open("outputs.txt","w") as arquivo:   #abre arquivo 'outuputs.txt' para modo escrita                                  
	arquivo.write(retornoAudio) # escreve no arquivo  o retorno do audio

print(retornoAudio)	#imprime na tela o retorno do audio

file = open("outputs.txt", "r").read().replace("\n", " ")  #abre arquivo 'outuputs.txt'para leitura e retira as quebras de linha

speech = gTTS(text = str(file), lang = 'pt-BR', slow = False)  #transforma o texto em audio
speech.save("audio.mp3") #salva o arquivo no formato audio.mp3

os.system("start audio.mp3") #reproduz o arquivo audio.mp3

print('fim do programa')