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
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", \
         "setembro", "outubro", "novembro", "dezembro"]


def reconhecimento():
    with microphone as source: 
    	recognizer.adjust_for_ambient_noise(source)     #calibra o microfone
    	audio = recognizer.listen(source)				#escuta o microfone				
    
    retornoAudio = recognizer.recognize_google(audio,language='pt-BR') #interpreta o audio utilizando o idioma português brasileiro
    
    with open("outputs.txt","w") as arquivo:   #abre arquivo 'outuputs.txt' para modo escrita                                  
    	arquivo.write(retornoAudio) # escreve no arquivo  o retorno do audio
    
    print(retornoAudio)	#imprime na tela o retorno do audio
    
    


def autenticacao_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
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

def dia(text):
    text = text.lower()

service = autenticacao_google()
eventos(2, service)