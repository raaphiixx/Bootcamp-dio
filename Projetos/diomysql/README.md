# Projeto Banco de Controle

Este é um projeto criado para o BootCamp **Cognizant Cloud Data Engineer #2** que tem como objetivo criar um banco de dados em *MySQL* para controlar as séries assistidas, por não ter o costume de acompanhar séries resolvi fazer algumas pequenas modificações. Segue abaixo os incrementos que fiz
1. É possível adicionar Filmes, Séries e Filmes
   1. Dentro de cada tabela há campos em comuns para serem adicionados, como nome, descrição, colocar uma imagem e dar uma nota.
   2. Outros campos são especiais para cada tabela.
2. Todos as tabelas serão mostradas já formatadas no Front-End
3. Na index há um slide com todas as capas das tabelas

Para iniciar o projeto será necessário executar alguns passos, para que não haja problemas de compatibilidade.

### Passos que devem ser seguidos
1. Criar seu ambiente virtual para que as depêndencias sejam instaladas, isso vai evitar poluir seu Python com extensões desnecessárias.

**Pacote para criação de ambientes virtuais:**
```
    pip install virtualenv
```
**Criando seu ambiente:**
```
    virtualenv nome_da_virtualenv
```
**Ativando seu ambiente:** *Utilizar o tab vai auxiliar*
```
    nome_da_virtualenv/Scripts/Activate
```
**Desativando o ambiente:**
```
    deactive nome_da_virtualenv
```

Após esses passos poderemos de começar o projeto. 

2. Há um arquivo chamado ```requirements.txt```, nele estão todos os pacotes utilizados na criação deste projeto, então vamos utiliza-lo, lembre-se de estar com o ambiente virtual **ativo**

**Instalando os pacotes:**
```
    pip install -r requirements.txt
```

Pronto, todos os pacotes estão instalados no seu ambiente.

3. Hora de começar as alterações nos arquivos

Dentro do diretório ```diomysql\diomysql``` teremos um arquivo chamado ```settings.py``` nele estão contidas todas as configurações do projeto.

**Mudanças no arquivo settings.py:**

```commandline
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_db',
        'USER': 'seu_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Primeiramente crie um banco de dados no **MySQL** e depois passe as informações para este parâmetro.

```
    TIME_ZONE = 'America/Bahia'
```
Caso esteja em outro fuso, pode alterar neste parâmetro

4. Pronto, seu projeto está quase pronto, agora basta salvar as informações no BD e iniciar seu servidor.

**Salvando informações:**
```commandline
    py manage.py makemigrations core
```
Esse comando vai criar um arquivo de migração que informa o que será executado no seu banco de dados.

**Inserindo as informações:**
```commandline
    py manage.py migrate
```
Pronto, informações salvas, seu servidor já está funcionando.

5. Estamos quase no final, para inserir informações no seu banco de dados será necessário ter um usuário administrativo, também conhecido como super usuário.

**Criando Super User:**
```commandline
    py manage.py createsuperuser
```
Quando executado, serão feitas algumas perguntas para configurar o usuário administrativo, basta completar as informações requisitadas e pronto já poderá acessar o painel administrativo.

## ROTAS:
**/root/** <- Painel administrativo
**/movies** <- Página com os filmes
**/books** <- Página com os livros
**/series** <- Página com os series
