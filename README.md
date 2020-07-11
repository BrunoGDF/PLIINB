# PLIINB

Projeto Integrador - FATEC 2020 1º Sem - Banco de Dados

# [](https://github.com/BrunoGDF/PLIINB#equipe--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#equipe--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#equipe--)**Equipe  💻**

### [](https://github.com/BrunoGDF/PLIINB#dev-team)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#dev-team)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#dev-team)**Dev Team**

-   Isidro A. A. Jr.
-   Israel Zanardi
-   Lucas Rodrigues
-   Natália Assis Romanini
-   Pedro Garcia

### [](https://github.com/BrunoGDF/PLIINB#master)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#master)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#master)**Master**

-   Bruno G. D. Faria

# [](https://github.com/BrunoGDF/PLIINB#o-que-%C3%A9-o-pliinb--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#o-que-%C3%A9-o-pliinb--)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#o-que-%C3%A9-o-pliinb-)**O que é o PLIINB?  🔍**

Assistente Pessoal Virtual vinculado à API Google Calendar, no qual o usuário usará comandos de voz para acessar a Agenda Google através da API, executar os comandos de consultar, editar e visualizar compromissos da agenda. Além de consumir API do sexto semestre.

### [](https://github.com/BrunoGDF/PLIINB#lista-de-comandos-poss%C3%ADveis)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#lista-de-comandos-poss%C3%ADveis)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#lista-de-comandos-poss%C3%ADveis)**Lista de comandos possíveis:**

-   Consultar agenda;
-   Ler compromissos do dia;
-   Incluir compromisso;
-   Editar compromisso;
-   Excluir compromisso;
-   Fechar agenda.

# [](https://github.com/BrunoGDF/PLIINB#ferramentas-e-linguagens--%EF%B8%8F)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#ferramentas-e-linguagens--%EF%B8%8F)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#ferramentas-e-linguagens-%EF%B8%8F)**Ferramentas e Linguagens**  🛠️

Ferramentas utilizadas para o desenvolvimento do projeto:

-   Python 3.6 (com Flask)
    
-   Spyder (IDE)
    
-   Agenda do Google (API Google Calendar)
    
-   Trello
    
-   StackEdit
    
-   Github <[https://github.com/BrunoGDF/PLIINB/](https://github.com/BrunoGDF/PLIINB/)
    

# [](https://github.com/BrunoGDF/PLIINB#criando-o-pliinb)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#criando--o-pliinb)Criando o PLIINB



Assistente Pessoal Virtual



## [](https://github.com/BrunoGDF/PLIINB#pr%C3%A9-requisitos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%A9-requisitos)Pré-requisitos

### [](https://github.com/BrunoGDF/PLIINB#instalar-os-softwares)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Instalar os softwares:

```
-   Python 3.6 (com Flask); 
    
-   Spyder (IDE);
    
-   Agenda do Google (API Google Calendar);
    
-   Gerenciamento de pacotes pip;

-   Dispositivos de áudio e voz (microfone e fones de ouvido/alto-falantes);

-   Possuir acesso a internet;

-   Browser (Google Chrome);

-   Uma conta do Google com o Google Agenda ativado.


```

### [](https://github.com/BrunoGDF/PLIINB#bibliotecas)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#bibliotecas)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#installing)Bibliotecas

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

```
pip install PyAudio
```

## [](https://github.com/BrunoGDF/PLIINB#execu%C3%A7%C3%A3o-do-c%C3%B3digo)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#execu%C3%A7%C3%A3o-do-c%C3%B3digo)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Execução do Código

O código do PLIINB é composto por funções, a primeira função tem o papel de reconhecimento de voz. Código do reconhecimento de voz:  [https://github.com/BrunoGDF/PLIINB/blob/master/Entrega_2/audio.py](https://github.com/BrunoGDF/PLIINB/blob/master/Entrega_2/audio.py)

Flask:  [https://github.com/BrunoGDF/PLIINB/blob/Sprint03/Ol%C3%A1%20mundo.py](https://github.com/BrunoGDF/PLIINB/blob/Sprint03/Ol%C3%A1%20mundo.py)

### [](https://github.com/BrunoGDF/PLIINB#reconhecimento-de-voz)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Reconhecimento de voz

Iniciado o reconhecimento de voz, é identificado o idioma (Português), ao qual armazena o som em uma variável (retornoAudio).

### [](https://github.com/BrunoGDF/PLIINB#autentica%C3%A7%C3%A3o-de-usu%C3%A1rio)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Autenticação de Usuário

A próxima função faz a autenticação das credênciais direcionando o usuário para dar as permissões necessárias. Autenticação do usuário na conta google através da API com login e senha.

```
LOGIN:           @gmail.com
SENHA: 
```

Dadas as premissões, o código possui a função eventos que vai identificar a existência ou não de eventos na agenda.

### [](https://github.com/BrunoGDF/PLIINB#acesso-%C3%A0-agenda)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#instalar--os-softwares)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Acesso à agenda

As funções (eventos) e (day) presentes no código possuem a função de procurar por palavras chave em uma frase dita ao reconhecimento e retornar ao usuário os compromissos daquele dia. Por exemplo, ao falar: "Eventos no dia 10 de Junho", ele identifica compromissos na data ou avisa que não há eventos no dia.

A função (editarEventos) possibilita ao usuário fazer alterações em um evento, seja no título ou data do compromisso.

## [](https://github.com/BrunoGDF/PLIINB#frameworks)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#frameworks)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Frameworks

Utilizamos o Python 3.6 (com Flask) após uma pesquisa entre os frameworks Justpy e o Flask, para saber qual se adequaria melhor ao projeto, onde foi decidido que seria utilizado o Flask pois o justpy apresentou erro ao rodar.

## [](https://github.com/BrunoGDF/PLIINB#pr%C3%B3ximos-passos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Próximos passos

 - [ ] Tela inicial do programa;
       
 - [ ] Comando para incluir, editar e excluir compromissos na agenda.

 - [ ] Comando para fechamento da agenda.


## [](https://github.com/BrunoGDF/PLIINB#pr%C3%B3ximos-passos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Entrega 3

De acordo com o planejado para a entrega 3, o grupo atingiu as metas e obteve os seguintes avanços:

Interação do Python com Google Calender API através da autenticação com json-https://github.com/BrunoGDF/PLIINB/blob/Sprint03/reconhecimentoDeVoz.py

Interação do Python com interface web(Flask)- https://github.com/BrunoGDF/PLIINB/blob/Sprint03/Ol%C3%A1%20mundo.py


## [](https://github.com/BrunoGDF/PLIINB#pr%C3%B3ximos-passos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Entrega 4


Conforme foi definido os próximos passos para entrega 4, foram encontradas algumas dificuldades, porém sobressaiu o sucesso da equipe em grandes avanços com êxitos onde o codigo executa as seguintes funções:

Comando para abrir agenda. ✔️

Comando para criar compromissos. ✔️ 

Comando para fechamento da agenda. ✔️

Comando para editar compromissos na agenda. (codigo pronto, porem, finalizando últimas correções visando qualidade ao cliente) 🛠

Acesso aos comandos realizados: https://github.com/BrunoGDF/PLIINB/tree/Sprint04

Vídeo de apresentação está contido no arquivo rar: https://github.com/BrunoGDF/PLIINB/blob/master/Video_Apresentacao_Entrega4.rar


## [](https://github.com/BrunoGDF/PLIINB#pr%C3%B3ximos-passos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Entrega 5

Nesta entrega realizamos uma interação de voz com a API desenvolvida pelos alunos do 6º semestre voltada a pesquisa de filmes, foi concluído também o comando editar, ele possibilita a consulta e a alteração de um compromisso na agenda. Sendo assim, o objetivo final da entrega de 5 comandos teve sucesso.

Vídeo de apresentação: https://drive.google.com/file/d/1haTgoNxlE3Bz-iWjvClHnNTCGq0rlkxC/view?usp=sharing


## [](https://github.com/BrunoGDF/PLIINB#pr%C3%B3ximos-passos)[](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#pr%C3%B3ximos-passos)[](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Entrega final

