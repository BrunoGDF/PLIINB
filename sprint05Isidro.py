# CRIAR client_secret.json
# https://console.developers.google.com/start/api?id=calendar



from __future__ import print_function
import datetime
import os.path
import speech_recognition as sr #importa biblioteca speech_recognition
import os                       #importa biblioteca do sistema operacional 
import webbrowser
from oauth2client import file ,client, tools
import httplib2
from apiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle



recognizer = sr.Recognizer()    #inicializa reconhecimento de voz
microphone = sr.Microphone()    #inicializa microphone

try: 
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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
    
    """Pega um usuario validado pelo credentials
    
    Se nada foi armazenado, ou o credentials armazenado for invalido
    o OAuth2 vai obter novas credentials.

    Returna:
        As credentials obtidas.
    """
    store = file.Storage('storage.json')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Armazenando credenciais')
        
        return credentials

#lista Eventos
def listarEventos(text):
       
    # Call the Calendar API
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=SCOPES)
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))
    credentials = pickle.load(open("token.pkl", "rb"))
    service = discovery.build("calendar", "v3", credentials=credentials)
    calendarlist = service.calendarList().list().execute()
    calendar_id = calendarlist['items'][0]['id']
    
    query = text
    events = service.events().list(calendarId=calendar_id, q=query, singleEvents='True' ,orderBy='startTime').execute()
    events = events.get('items', [])
    i=1
    for event in events:    
            start = event['start'].get('dateTime')
            print(i, event['summary'])      
            print(start)
            for attendees in event['attendees']:
                print(attendees['displayName'] + " ( "  +attendees['email']+ ")" )
            i += 1
            print('_____________________________________')
    i=1
    
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


def editarEventos(events, service):
    lin()
    print('Deseja editar algum evento')
    print('SIM  /  NÃO')
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

    print("Escolha um nova data")
    data = reconhecimento().lower()
    print(data)
    lin()

    event['summary'] = titulo
    
    event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    input("Pressione uma tecla para continuar...")

#linha
def lin():
    print('-'*30)

def criar():
   
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
    print("Hora Inicio")
    horaI = reconhecimento()
    converter(horaI)
    print(horaI)
    lin()
    print('Hora Fim')
    horaF = reconhecimento()
    converter(horaF)
    print(horaF)
    lin()
    credentials = autenticacao_google()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
   
    GMT_OFF = '-03:00'
    event = {
      'summary': '{}'.format(tit),
      'location': '{}'.format(ende),
      'description': '{}'.format(desc),
       'start': {
        'dateTime': '{}T{}%s'.format(day(dateI), horaI) %GMT_OFF,
        'timeZone': 'Brazil/East',
      },
      'end': {
        'dateTime': '{}T{}%s'.format(day(dateI), horaF) %GMT_OFF,
        'timeZone': 'Brazil/East',
        },
      },
    

    
    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Compromisso agendado: %s' % (event.get('htmlLink')))

def converter(date_time): 
    format = '%I:%M' # o formato
    datetime_str = datetime.datetime.strptime(date_time, format) 
    
    
    return datetime_str 

def web():
      
    ouvindo = reconhecimento().lower()
    print(ouvindo)
    if ouvindo == 'página':
        webbrowser.open('https://www.google.com')
    else:
        print("ERRO")
    
    return web
    
def deletar():
    
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
    credentials = autenticacao_google()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
   
    event = {
      'summary': '{}'.format(tit),
      'location': '{}'.format(ende),
      'description': '{}'.format(desc),
       'start': {
        'dateTime': '{}T09:00:00-07:00'.format(day(dateI)),
        'timeZone': 'Brazil/East',
      },
      'end': {
        'dateTime': '{}T09:00:00-07:00'.format(day(dateI)),
        'timeZone': 'Brazil/East',
        },
      },
    

    event = service.events().delete(calendarId='primary', eventId='eventId').execute()
    print ('Compromisso Deletado: %s' % (event.get('htmlLink')))
    


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
        print("Deletar Evento diga (Deletar)")
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
            criar()
        elif text == 'deletar':
            deletar()
        elif text == 'consulta':
            print("Qual data deseja consultar ?")
            text = reconhecimento().lower()
            print(text)
            lin()
            listarEventos(day(text))            
        lin()
    elif inicio == 'sair':
        sair = True
        print("Fechando o Sistema")
    else:
        print("Comando não reconhecido")

