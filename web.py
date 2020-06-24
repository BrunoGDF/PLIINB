import speech_recognition as sr #importa biblioteca speech_recognition
import webbrowser



recognizer = sr.Recognizer()    #inicializa reconhecimento de voz
microphone = sr.Microphone()    #inicializa microphone



#reconhecimento de Voz
def reconhecimento():
    with microphone as source: 
    	recognizer.adjust_for_ambient_noise(source)     #calibra o microfone
    	audio = recognizer.listen(source)				#escuta o microfone				
    
    try:
        retornoAudio = recognizer.recognize_google(audio,language='pt-BR') #interpreta o audio utilizando o idioma português brasileiro
    except:
        print("repita novamente...")
        retornoAudio = reconhecimento()
            
    with open("outputs.txt","w") as arquivo:   #abre arquivo 'outuputs.txt' para modo escrita                                  
    	arquivo.write(retornoAudio) # escreve no arquivo  o retorno do audio
    
    return retornoAudio



def web():
      
    ouvindo = reconhecimento().lower()
    print(ouvindo)
    if ouvindo == 'página':
        webbrowser.open('https://www.google.com')
    else:
        print("ERRO")
    
    return web
    
