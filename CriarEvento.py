# CRIAR client_secret.json
# https://console.developers.google.com/start/api?id=calendar



from __future__ import  print_function
 data e hora da importação
import  os . caminho
importar  speech_recognition  como  sr  #importa biblioteca speech_recognition
importar  os                        #importa biblioteca do sistema operacional
importação  pytz
do  arquivo de importação oauth2client  , cliente , ferramentas 
importar  ATENDPLIB2
da  descoberta de importação apiclient  

reconhecedor  =  sr . Reconhecedor ()     #inicializa reconhecimento de voz
microfone  =  sr . Microfone ()     #inicializa microfone

tente :
     argparse de importação
    flags  =  argparse . ArgumentParser ( pais = [ ferramentas . Argparser ]). parse_args ()
exceto  ImportError :
    flags  =  None

claro  =  lambda : os . sistema ( 'cls' )

#variaveis Globais

ESCOPOS  = [ 'https://www.googleapis.com/auth/calendar.events' ]

dayS  = [ "segunda" , "terça" , "quarta" , "quinta" , "sexta" , "sabado" , "domingo" ]

APPLICATION_NAME  =  'Início rápido da API do Calendário Google Python'

MESES  = [ "janeiro" , "fevereiro" , "março" , "abril" , "maio" , "maio" , "junho" , "julho" , "agosto" , \
         "setembro" , "outubro" , "novembro" , "dezembro" ]

dayNUM  = [ "um" , "dois" , "três" , "quatro" , "cinco" , "seis" , "sete" , "oito" , "nove" , "dez" , \
          "onze" , "cochilar" , "treze" , "quatorze" , "quinze" , "dezesseis" , "dezessete" , \
              "dezoito" , "dezenove" , "vinte" , "vinte e um" , "vinte e dois" , "vinte e três" \
                  "vinte e quatro" , "vinte e cinco" , "vinte e seis" , "vinte e sete" , \
                      "vinte e oito" , "vinte e nove" , "trinta" , "trinta e um" ]

#reconhecimento de Voz
def  reconhecimento ():
    com  microfone  como  fonte :
    	reconhecedor . Adjust_for_ambient_noise ( fonte )      #calibra o microfone
    	audio  =  reconhecedor . listen ( fonte )				 #escuta o microfone				
    
    tente :
        retornoAudio  =  reconhecedor . reconhece_google ( áudio , idioma = 'pt-BR' ) #interpreta o áudio usando o idioma português brasileiro
    exceto :
        print ( "repita novamente ..." )
        retornoAudio  =  reconhecimento ()
            
    com  open ( "outputs.txt" , "w" ) como  arquivo :    #abre arquivo 'outuputs.txt' para modo de escrita                                  
    	arquivo . write ( retornoAudio ) # grava o arquivo de retorno de áudio
    
    return  retornoAudio

# autenticação de usuário    
def  autenticacao_google ():
    
    "" "Pega um usuário validado por credenciais
    
    Se nada foi armazenado, ou credenciais armazenadas para invalido
    o OAuth2 vai obter novas credenciais.
    Returna:
        Como credenciais selecionadas.
    "" "
    store  =  arquivo . Armazenamento ( 'storage.json' )
    credenciais  =  loja . get ()
    se  não  credenciais  ou  credenciais . inválido :
        fluxo  =  cliente . flow_from_clientsecrets ( 'client_secret.json' , SCOPES )
        fluxo . user_agent  =  APPLICATION_NAME
        se  sinalizadores :
            credenciais  =  ferramentas . run_flow ( fluxo , loja , sinalizadores )
        else : # Necessário apenas para compatibilidade com o Python 2.6
            credenciais  =  ferramentas . executar ( fluxo , armazenar )
        print ( 'Armazenando credenciais' )
     credenciais de retorno

#lista Eventos
def  eventos ( dia , serviço ):
    # Chame a API do Google Agenda
    date  =  datetime . data e hora . combinar ( dia , data e hora . datetime . min . tempo ())
    end_date  =  datetime . data e hora . combinar ( dia , data e hora . datetime . máx . tempo ())
    utc  =  pytz . UTC
    date_utc  =  data . astimezone ( utc )
    end_date_utc  =  end_date . astimezone ( utc )
    
    events_result  =  serviço . eventos (). list ( calendarId = 'primary' ,
                                          timeMin = date_utc . isoformato (),
                                          timeMax = end_date_utc . isoformato (),
                                          singleEvents = True ,
                                          orderBy = 'startTime' ). execute ()
    events  =  events_result . get ( 'itens' , [])

    se  não  eventos :
        print ( 'Não existem compromissos neste dia.' )
        input ( "Pressione uma tecla para continuar ..." )
    mais :
        claro ()
        lin ()
        print ( "Listando Eventos" )
        print ( "Inicio:" , data )
        print ( "Fim:" , final_data )
        para  evento  em  eventos :
            lin ()
            print ( "Titulo:" +  evento [ 'resumo' ])
            print ( "Data e Horário:" +  evento [ 'start' ]. get ( 'dateTime' ))
            lin ()
            print ( "" )

        editarEventos ( eventos , serviço )

#reconhece uma palabvra chave para eventos no mes
 dia da def ( texto ):
    
    texto  =  texto . mais baixo ()
    today  =  datetime . data . hoje ()

    se  texto . count ( "hoje" ) >  0 :
        volte  hoje
    
    dia  =  - 1
    day_of_week  =  - 1
    mês  =  - 1
    ano  =  hoje . ano
    
    para  palavra  no  texto . split ():
        se  palavra  em  MESES :
            mês  =  MESES . índice ( palavra ) +  1  # procura pelo nome do mês
         palavra  elif em  dias :
            DAY_OF_WEEK  =  dias . índice ( palavra ) # procura pelo nome do dia
         palavra elif . isdigit ():
            dia  =  int ( palavra )
        mais :
            para  nume  em  dayNUM :
                encontrado  =  palavra . encontrar ( nume )
                se  encontrado  >  0 :
                    tente :
                        dia  =  int ( palavra [: encontrada ])
                    exceto :
                        passar
    se  mês  <  hoje . month  and  month  ! =  - 1 : # condição para verificar o ano atual
        ano  =  ano + 1
    
    se  dia  <  hoje . dia  e  mês  ==  - 1  e  dia  ! =  - 1 : # condição para verificar mes
        mês  =  mês  +  1
        
    se  mês  ==  - 1  e  dia  ==  - 1  e  dia_de_semana  ! =  - 1 :
        current_day_of_week  =  hoje . dia da semana ()
        dif  =  DAY_OF_WEEK  -  current_day_of_week
        
        se  dif  <  0 :
            dif  + =  7
            se  texto . count ( "próximo" ) > =  1 :
                dif  + =  7
        retorne  hoje  +  data e hora . timedelta ( dif )
    
    retornar  data e hora . data ( mês = mês , dia = dia , ano = ano )


def  editarEventos ( eventos , serviço ):
    lin ()
    print ( 'Deseja editar algum evento' )
    print ( 'SIM / NÃO' )
    lin ()
    inicio  =  reconhecimento (). mais baixo ()
    if  inicio  ==  'sim' :
        lin ()
        print ( "Editando Eventos" )
        lin ()

        print ( "Escolha um titulo" )
        titulo  =  reconhecimento (). mais baixo ()
        print ( titulo . lower ())
        lin ()

        encontrado  =  False
        para  evento  em  eventos :
           if ( evento [ 'resumo' ]. lower () ==  titulo ):
               editar ( evento , serviço )
               encontrado  =  True

        if ( encontrado  ==  False ):
            lin ()
            print ( "Evento não encontrado!" )
            editarEventos ( eventos , serviço )


def  editar ( evento , serviço ):
    print ( "Escolha um novo titulo" )
    titulo  =  reconhecimento (). mais baixo ()
    print ( titulo . lower ())
    lin ()

    print ( "Escolha um nova data" )
    data  =  reconhecimento (). mais baixo ()
    imprimir ( dados )
    lin ()

    evento [ 'resumo' ] =  titulo
    
    updated_event  =  service . eventos (). update ( calendarId = 'primário' , eventId = evento [ 'id' ], corpo = evento ). execute ()
    input ( "Pressione uma tecla para continuar ..." )

#linha
def  lin ():
    print ( '-' * 30 )

def  criar ():
   
    print ( "Titulo:" )
    tit  =  reconhecimento (). capitalizar ()
    impressão ( tit )
    lin ()
    print ( "Endereço:" )
    ende  =  reconhecimento (). capitalizar ()
    imprimir ( ende )
    lin ()
    print ( "Descrição" )
    desc  =  reconhecimento (). capitalizar ()
    print ( desc )
    lin ()
    print ( "Data Inicio" )
    dateI  =  reconhecimento (). capitalizar ()
    print ( dateI )
    lin ()
    print ( 'Data Fim' )
    dateF  =  reconhecimento (). capitalizar ()
    print ( dateF )
    lin ()
    credenciais  =  autenticacao_google ()
    http  =  credenciais . autorizar ( httplib2 . Http ())
    serviço  =  descoberta . build ( 'calendário' , 'v3' , http = http )
   
    event  = {
      'resumo' : '{}' . formato ( tit ),
      'location' : '{}' . formato ( ende ),
      'descrição' : '{}' . formato ( desc ),
       'start' : {
        'dateTime' : '{} T11: 00: 00-01: 00' . formato ( dia ( dataI )),
        'timeZone' : 'Brasil / Leste' ,
      }
      'end' : {
        'dateTime' : '{} T11: 00: 00-12: 00' . formato ( dia ( dataI )),
        'timeZone' : 'Brasil / Leste' ,
      }
      'recorrência' : [
        'RRULE: FREQ = DIARIAMENTE; COUNT = 0'
      ],
      'participantes' : [
        { 'email' : 'lpage@example.com' },
        { 'email' : 'sbrin@example.com' },
      ],
      'lembretes' : {
        'useDefault' : False ,
        'substitui' : [
          { 'method' : 'email' , 'minutes' : 24  *  60 },
          { 'método' : 'pop-up' , 'minutos' : 10 },
        ],
      }
    }

    
    evento  =  serviço . eventos (). inserir ( calendarId = 'primário' , corpo = evento ). execute ()
    print ( 'Compromisso agendado:% s'  % ( evento . get ( 'htmlLink' ))))

  

autenticacao_google ()
lin ()
lin ()
print ( "Iniciando PLIINB" )
lin ()
print ( "" )
print ( "" )
lin ()
SERVICE  =  autenticacao_google ()
print ( "Bem vindo, PLIINB iniciado." )
lin ()
sair  =  False
enquanto  não  sair :
    claro ()
    print ( "" )
    print ( "" )
    lin ()
    print ( "Como posso ajudar?" )
    print ( "Escolha um comando" )
    lin ()
    print ( "ABRIR, SAIR" )
    lin ()
    inicio  =  reconhecimento (). mais baixo ()
    if  inicio  ==  'abrir' :        
        lin ()
        print ( "Essas são as opções disponíveis:" )
        lin ()
        print ( "Criar Evento diga (Criar)" )
        lin ()
        print ( "Consultar compromissos diga (consulta)" )
        lin ()
        print ( "Finalizar diga (Sair)" )
        lin ()
        texto  =  reconhecimento (). mais baixo ()
        print ( texto . lower (). capitalize ())
        se  texto  ==  'sair' :
            sair  =  True
        elif  text  ==  'criar' :
            criar ()
        elif  text  ==  'consulta' :
            print ( "Qual data deseja consultar?" )
            texto  =  reconhecimento (). mais baixo ()
            SERVICE  =  autenticacao_google ()
            impressão ( texto )
            lin ()
            eventos ( dia ( texto ), SERVIÇO )            
        lin ()
    elif  inicio  ==  'sair' :
        sair  =  True
        print ( "Fechando o Sistema" )
    mais :
        print ( "Comando não reconhecido" )
