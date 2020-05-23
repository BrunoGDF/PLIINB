from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import speech_recognition as sr #importa biblioteca speech_recognition
from gtts import gTTS           #importa biblioteca gTTS
import os                       #importa biblioteca do sistema operacional 

recognizer = sr.Recognizer()    #inicializa reconhecimento de voz
microphone = sr.Microphone()    #inicializa microphone

#variaveis Globais
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
dayS = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", \
         "setembro", "outubro", "novembro", "dezembro"]
dayNUM = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", \
          "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", \
              "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e três" \
                  "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete", \
                      "vinte e oito", "vinte e nove", "trinta", "trinta e um"]

#reconhecimento de Voz
def reconhecimento():
    with microphone as source: 
    	recognizer.adjust_for_ambient_noise(source)     #calibra o microfone
    	audio = recognizer.listen(source)				#escuta o microfone				
    
    retornoAudio = recognizer.recognize_google(audio,language='pt-BR') #interpreta o audio utilizando o idioma português brasileiro
    
    with open("outputs.txt","w") as arquivo:   #abre arquivo 'outuputs.txt' para modo escrita                                  
    	arquivo.write(retornoAudio) # escreve no arquivo  o retorno do audio
    
    return retornoAudio
    
#autenticação de Usuário    
def autenticacao_google():
    
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
   
    return service

#lista Eventos
def eventos(n, service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

#reconhece uma palabvra chave para eventos no mes
def day(text):
    text = text.lower()
    hoje = datetime.date.today()

    if text.count("hoje") > 0:
        return hoje
    
    day = -1
    day_of_week = -1
    month = -1
    year = hoje.year
    
    for word in text.split():
        if word in MESES:
            month = MESES.index(word) + 1 # procura pelo nome do mês
        elif word in dayS:
            day_of_week = dayS.index(word) # procura pelo nome do day
        elif word.isdigit():
            day = int(word)
        else:
            for nume in dayNUM:
                found = word.find(nume)
                if found > 0:
                    try :
                        day = int(word[:found])
                    except:
                        pass
    if month < hoje.month and month != -1: # condição para verificar year atual
        year = year+1
    
    if day < hoje.day and month == -1 and day != -1: #condição para verificar mes
        month = month + 1
        
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = hoje.weekday()
        dif = day_of_week - current_day_of_week
        
        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7
        return hoje + datetime.timedelta(dif)
    
    return datetime.date(month=month, day=day, year=year)

text = reconhecimento().lower()
print(reconhecimento())
print(day(text))
