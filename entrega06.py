# CRIAR client_secret.json
# https://console.developers.google.com/start/api?id=calendar

from __future__ import print_function
import datetime
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import speech_recognition as sr #importa biblioteca speech_recognition
import os                       #importa biblioteca do sistema operacional 
import pytz

recognizer = sr.Recognizer()    #inicializa reconhecimento de voz
microphone = sr.Microphone()    #inicializa microphone


clear = lambda: os.system('cls')

#variaveis Globais

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

dayS = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

APPLICATION_NAME = 'Google Calendar API Python Quickstart'

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
    
    try:
        retornoAudio = recognizer.recognize_google(audio,language='pt-BR') #interpreta o audio utilizando o idioma português brasileiro
    except:
        print("repita novamente...")
        retornoAudio = reconhecimento()
            
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
def eventos(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date_utc = date.astimezone(utc)
    end_date_utc = end_date.astimezone(utc)
    
    events_result = service.events().list(calendarId='primary', 
                                          timeMin=date_utc.isoformat(),
                                          timeMax=end_date_utc.isoformat(),
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('Não existem compromissos neste dia.')
        input("Pressione uma tecla para continuar...")
    else:
        clear()
        lin()
        print("Listando Eventos ")
        print("Inicio:", date)
        print("Fim:", end_date)
        for event in events:
            lin()
            print("Titulo:"+ event['summary'])
            print("Data e Horário: "+ event['start'].get('dateTime'))
            lin()
            print("")

        editarEventos(events, service)

#reconhece uma palabvra chave para eventos no mes
def day(text):
    
    text = text.lower()
    today = datetime.date.today()

    if text.count("hoje") > 0:
        return today
    
    day = -1
    day_of_week = -1
    month = -1
    year = today.year
    
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
    if month < today.month and month != -1: # condição para verificar year atual
        year = year+1
    
    if day < today.day and month == -1 and day != -1: #condição para verificar mes
        month = month + 1
        
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week
        
        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7
        return today + datetime.timedelta(dif)
    
    return datetime.date(month=month, day=day, year=year)

def hours(text):
    horas = text.split(' ')
    return horas[0]+':00:00'


def editarEventos(events, service):
    lin()
    print('Deseja editar algum evento')
    print('SIM / NÃO')
    lin()
    inicio = reconhecimento().lower()
    if inicio == 'sim':
        lin()
        print("Editando Eventos")
        lin()

        print("Escolha um titulo")
        titulo = reconhecimento().lower()
        print(titulo.lower())
        lin()

        encontrado = False
        for event in events:
           if (event['summary'].lower() == titulo):
               editar(event, service)
               encontrado = True

        if (encontrado == False):
            lin()
            print("Evento não encontrado!")
            editarEventos(events, service)


def editar(event, service):
    print("Escolha um novo titulo")
    titulo = reconhecimento().lower()
    print(titulo.lower())
    lin()

    print("Data Inicio")
    dateI = reconhecimento().capitalize()
    print(dateI)

    print('Data Fim')
    dateF = reconhecimento().capitalize()
    print(dateF)
    lin()

    print('Hora inicio')
    horaInicio = reconhecimento().capitalize()
    print(horaInicio)
    lin()
    print('Hora Fim')
    horaFim = reconhecimento().capitalize()
    print(horaFim)
    lin()

    event['summary'] = titulo
    event['start'] = {
                        'dateTime': '{}'.format(day(dateI)) + 'T'+ hours(horaInicio),
                        'timeZone': 'Brazil/East',
                    }

    event['end'] = {
                    'dateTime': '{}'.format(day(dateF)) + 'T'+ hours(horaFim),
                    'timeZone': 'Brazil/East',
                   }


    
    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

    print('Evento Atualizado...', updated_event['updated'])
    input("Pressione uma tecla para continuar...")

#linha
def lin():
    print('-'*30)

def criar(service):
   
    print("Titulo:")
    tit = reconhecimento().capitalize()
    print(tit)
    lin()
    print("Endereço:")
    ende = reconhecimento().capitalize()
    print(ende)
    lin()
    print("Descrição")
    desc = reconhecimento().capitalize()
    print(desc)
    lin()
    print("Data Inicio")
    dateI = reconhecimento().capitalize()
    print(dateI)
    lin()
    print('Data Fim')
    dateF = reconhecimento().capitalize()
    print(dateF)
    lin()

    print("Hora inicio")
    horaInicio = reconhecimento().capitalize()
    print(horaInicio)
    lin()
    print('Hora Fim')
    horaFim = reconhecimento().capitalize()
    print(horaFim)
    lin()
   
    event = {
      'summary': '{}'.format(tit),
      'location': '{}'.format(ende),
      'description': '{}'.format(desc),
       'start': {
        'dateTime': '{}'.format(day(dateI)) + 'T'+ hours(horaInicio),
        'timeZone': 'Brazil/East',
      },
      'end': {
        'dateTime': '{}'.format(day(dateF)) + 'T'+ hours(horaFim),
        'timeZone': 'Brazil/East',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Compromisso agendado: %s' % (event.get('htmlLink')))

  

autenticacao_google()
lin()
lin()
print("Iniciando PLIINB")
lin()
print("")
print("")
lin()
SERVICE = autenticacao_google()
print("Bem vindo, PLIINB iniciado.")
lin()
sair = False
while not sair:
    clear()
    print("")
    print("")
    lin()
    print("Como posso ajudar ?")
    print("Escolha um comando")
    lin()
    print("ABRIR, SAIR")
    lin()
    inicio = reconhecimento().lower()
    if inicio == 'abrir':        
        lin()
        print("Essas são as Opções disponíveis: ")
        lin()
        print("Criar Evento diga (Criar)")
        lin()
        print("Consultar compromissos diga (consulta)")
        lin()
        print("Finalizar diga (Sair)")
        lin()
        text = reconhecimento().lower()
        print(text.lower().capitalize())
        if text == 'sair':
            sair = True
        elif text == 'criar':
            criar(SERVICE)
        elif text == 'consulta':
            print("Qual data deseja consultar ?")
            text = reconhecimento().lower()
            SERVICE = autenticacao_google()
            print(text)
            lin()
            eventos(day(text), SERVICE)            
        lin()
    elif inicio == 'sair':
        sair = True
        print("Fechando o Sistema")
    else:
        print("Comando não reconhecido")