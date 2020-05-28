# PLIINB

Projeto Integrador - FATEC 2020 1º Sem - BD

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#equipe--)**Equipe  💻**

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#dev-team)**Dev Team**

-   Isidro A. A. Jr.
-   Israel Zanardi
-   Lucas Rodrigues
-   Natália Assis Romanini
-   Pedro Garcia

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#master)**Master**

-   Bruno G. D. Faria

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#o-que-%C3%A9-o-pliinb-)**O que é o PLIINB?  🔍**

Assistente Pessoal Virtual vinculado à API Google Calendar, no qual o usuário usará comandos de voz para acessar a Agenda Google através da API, executar os comandos de abrir, editar e visualizar compromissos da agenda. Além de consumir API do sexto semestre.

### [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#lista-de-comandos-poss%C3%ADveis)**Lista de comandos possíveis:**

-   Abrir agenda;
-   Fechar agenda;
-   Ler compromissos do dia;
-   Digitar compromisso;
-   Editar compromisso;
-   Excluir compromisso.

# [](https://github.com/BrunoGDF/PLIINB/blob/master/README.md#ferramentas-e-linguagens-%EF%B8%8F)**Ferramentas e Linguagens**  🛠️

Ferramentas utilizadas para o desenvolvimento do projeto:

-   Python 3.6 (com Flask) 
    
-   Spyder (IDE)
    
-   Agenda do Google (API Google Calendar)
    
-   Gerenciamento de pacotes pip
    
-   Uma conta do Google com o Google Agenda ativado


###[]
# Criando  o PLIINB

Assistente Pessoal Virtual 
### [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)
## Pré-requisitos

### [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#prerequisites)Instalar  os softwares:
```
-   Python 3.6 (com Flask) 
    
-   Spyder (IDE)
    
-   Agenda do Google (API Google Calendar)
    
-   Gerenciamento de pacotes pip
    
-   Uma conta do Google com o Google Agenda ativado

```

### [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#installing)Bibliotecas

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

## [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Execução do Código


Colocar informações sobre a execução do código.



## [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#running-the-tests)Reconhecimento de voz
 ![Reconhecimento de voz - ícones de tecnologia grátis](data:image/png;base64,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)

Iniciando o reconhecimento de voz

### [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#break-down-into-end-to-end-tests)Observações

comandos

```
Give an example

```

### [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#and-coding-style-tests) codificação

Explique o que esses testes testam e por que

```
Give an example

```

## [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#deployment)Autenticação de Usuário 
![Pesquisa por voz no Google: nova era no marketing digital](data:image/png;base64,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)

Autenticação do usuário na conta google através da API.







## [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#built-with)Frameworks


Utilizamos o Python 3.6 (com Flask) após uma pesquisa entre os frameworks Justpy e o Flask, para saber qual se adequaria melhor ao projeto, onde foi decidido que seria utilizado o Flask pois o justpy apresentou erro ao rodar.

## [](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#contributing)Próximos passos

Descrição das próximas etapas do projeto.


