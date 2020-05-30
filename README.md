# PLIINB

Projeto Integrador - FATEC 2020 1º Sem - Banco de Dados

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#equipe--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#equipe--)**Equipe  💻**

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#dev-team)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#dev-team)**Dev Team**

-   Isidro A. A. Jr.
-   Israel Zanardi
-   Lucas Rodrigues
-   Natália Assis Romanini
-   Pedro Garcia

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#master)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#master)**Master**

-   Bruno G. D. Faria

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#o-que-%C3%A9-o-pliinb--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#o-que-%C3%A9-o-pliinb-)**O que é o PLIINB?  🔍**

Assistente Pessoal Virtual vinculado à API Google Calendar, no qual o usuário usará comandos de voz para acessar a Agenda Google através da API, executar os comandos de consultar, editar e visualizar compromissos da agenda. Além de consumir API do sexto semestre.

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#lista-de-comandos-poss%C3%ADveis)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#lista-de-comandos-poss%C3%ADveis)**Lista de comandos possíveis:**

-   Consultar agenda;
-   Ler compromissos do dia;
-   Incluir compromisso;
-   Editar compromisso;
-   Excluir compromisso;
-    Fechar agenda.

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#ferramentas-e-linguagens--%EF%B8%8F)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#ferramentas-e-linguagens-%EF%B8%8F)**Ferramentas e Linguagens**  🛠️

Ferramentas utilizadas para o desenvolvimento do projeto:

-   Python 3.6 (com Flask)
    
-   Spyder (IDE)
    
-  Agenda do Google (API Google Calendar)
-  StackEdit 
- Github <[https://github.com/BrunoGDF/PLIINB/](https://github.com/BrunoGDF/PLIINB/)
- Trello <[https://trello.com/b/WIAbDetV/pliinb](https://trello.com/b/WIAbDetV/pliinb)


    
    

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#criando--o-pliinb)Criando o PLIINB

Assistente Pessoal Virtual

## [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%A9-requisitos)Pré-requisitos

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Instalar os softwares:

```
-   Python 3.6 (com Flask); 
    
-   Spyder (IDE);
    
-   Agenda do Google (API Google Calendar);
    
-   Gerenciamento de pacotes pip;
    
-   Uma conta do Google com o Google Agenda ativado.


```

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#bibliotecas)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#installing)Bibliotecas

Bibliotecas necessárias para obter um ambiente de desenvolvimento em execução.

**Instalar as bibliotecas:**

```
pip install google-api-python-client
```

```
pip install google-auth-oauthlib
```

```
pip install google-auth
```

```
pip install SpeechRecognition
```

```
pip install gTTS
```

## [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#execu%C3%A7%C3%A3o-do-c%C3%B3digo)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Execução do Código

O código do PLIINB é composto por funções, a primeira função tem o papel de reconhecimento de voz.

Código do reconhecimento de voz: [https://github.com/BrunoGDF/PLIINB/blob/master/Entrega_2/audio.py](https://github.com/BrunoGDF/PLIINB/blob/master/Entrega_2/audio.py)


Flask: [https://github.com/BrunoGDF/PLIINB/blob/Sprint03/Ol%C3%A1%20mundo.py](https://github.com/BrunoGDF/PLIINB/blob/Sprint03/Ol%C3%A1%20mundo.py)

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Reconhecimento de voz

Iniciado o reconhecimento de voz, é identificado o idioma (Português), ao qual armazena o som em uma variável (retornoAudio). 

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Autenticação de Usuário

A próxima função faz a autenticação das credênciais direcionando o usuário para dar as permissões necessárias.

Autenticação do usuário na conta google através da API com login e senha.
```
LOGIN:           @gmail.com
SENHA: 
```


 Dadas as premissões, o código possui a função eventos que vai identificar a existência ou não de eventos na agenda.

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Acesso à agenda

A última função presente no código, nome (day) procura por palavras chave em uma frase dita ao reconhecimento para identificar a data solicitada pelo usuário, por exemplo: "Eventos no dia 10 de Junho", ele identifica na frase a data 10 de junho.

Comando: 
[https://github.com/BrunoGDF/PLIINB/blob/Sprint03/reconhecimentoDeVoz.py](https://github.com/BrunoGDF/PLIINB/blob/Sprint03/reconhecimentoDeVoz.py)


## [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#frameworks)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Frameworks

Utilizamos o Python 3.6 (com Flask) após uma pesquisa entre os frameworks Justpy e o Flask, para saber qual se adequaria melhor ao projeto, onde foi decidido que seria utilizado o Flask pois o justpy apresentou erro ao rodar.



## [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Próximos passos

 - [ ] Tela inicial do programa;
 - [ ]  Comando para incluir, editar e excluir compromissos na agenda.
 - [ ]  Comando para fechamento da agenda.
