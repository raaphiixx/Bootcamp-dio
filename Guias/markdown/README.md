# 📑 Guia Rápido sobre MARKDOWN 📑
---
## O que é Markdown?
Markdown é uma linguagem de marcação, utilizada para formatar texto textos simples. Sua extensão é o .md

## Por que usar o Markdown?
- MarkDown é uma plataforma independente.
- Plataformas como Reddit, GitHub, GitLab tem suporte nativo a linguagem.
- Pode ser usada por todos, pessoas que criam sites, documentos, livros, apresentações email e documentos técnicos.

## Como criar um arquivo MarkDown?
Existem algumas ferramentas online que possibilitam a criação de arquivos e o download de arquivos Markdown.  
- [Dillinger](https://dillinger.io/)  
- [SlackEdit](https://stackedit.io/app#)  
- [GitHub](https://github.com)  

Porém também é possivel fazer o download de algumas ferramentas para criar seu arquivo, algumas dessas ferramentas já podem até fazer parte do seu cotidiano.
- [Notepad++](https://notepad-plus-plus.org/downloads/)
  - Dentro programa, vá na aba plugins, gerenciador de plugins, na aba disponíveis procure por Markdown e instale a extensão **MarkdownViewer++** .
  - Após a instalação reinicie a aplicação e crie seu arquivo .md, vá na aba plugins e lá estará habilitada a opção MarkdownViewer++ (CTRL+SHIFT+M), agora será possível criar seu arquivo e ver exatamente como está ficando.
  - 
- [VisualStudioCode](https://code.visualstudio.com/)
  - Dentro da aplicação, vá na aba extensões, busque por **Markdown All in One**, instale e reinicie a aplicação
  - Após este procedimento, crie ou edite seu arquivo .md, para ver o resultado pressione CTRL+SHIFT+V e o preview do arquivo será aberto.

## Marcações
- [Comentários](#comentários)
- [Títulos](#titulo)
- [Paragrafos](#paragrafos)
- [Links](#links)
- [Listas](#listas)

# Como utilizar o MarkDown?

## **Comentários**
Os comentários são uma parte importante de toda linguagem, seja ela de marcação ou de programação, pois é apartir deles que podemos deixar pequenas instruções sobre algum trecho para quem vai utilizar o código ~~(ou até lembrarmos o que fizemos)~~.

### Input / Entrada:   
```
[O comentário fica entre colchetes, logo após adiciona-se os dois pontos e finalizado com o # no final]: # 
```
[Easter Egg, linha oculta]: # 
 
## **Titulo**
Em todo texto é necessário que se utilizem titulos, sejam eles maiores ou menores, o Markdown fornece diversos tamanhos de títulos para serem utilizados, cada # aumenta mais o tamanho do título, tendo até 6 opções de escolha, troque o valor por um número entre 1 e 6. 

### Input/ Entrada:
```
# 1º Titulo
### 3º Titulo
###### 6º Titulo
```
### Output / Saída:

# 1º Titulo
### 3º Titulo
###### 6º Titulo  


## **Paragrafos**
Fazer uma quebra de linha entre paragráfos é bastante simples, é necessário que tenha uma linha sem conteúdo entre os paragráfos.

### Input / Entrada:
```
Isso é um paragrafo

Isso é outro paragráfo
```
### Output / Saída:

Isso é um paragráfo

Isso é outro paragráfo

## **Links**
Para inserir links o processo é mais simples do que parece, inserimos a referência e logo após a URL, vale ressaltar que nem a referência para os links e nem mesmo as URLS podem conter espaços.

### Input / Entrada:
```
[GitHub](https://www.github.com/raaphiixx)
```
### Output / Saída:
[GitHub](https://www.github.com/raaphiixx)

## **Listas**
Existem três formas de construir listas desordenadas e uma forma para listas ordenadas, e em ambas tem a possibilidade de fazer uma lista dentro de uma outra lista ~~(famoso inception)~~ .

### **Listas Ordenadas:**

## Input / Entrada:
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```
## Output / Saída:
1. Primeiro item
2. Segundo item
3. Terceiro item
  
## Input / Entrada:
```
1. Primeiro item
  1. Primeiro item interno
  2. Segundo item interno
2. Segundo item
  1. Primeiro item interno
  2.  Segundo item interno
```
## Output / Saída:
1. Primeiro item
   1. Primeiro item interno
   2. Segundo item interno
2. Segundo item
   1. Segundo item interno
   2. Segundo item interno

### **Lista Desordenada:**

## Input / Entrada:
```
* Item
* Item
```
## Output / Saída:
* Item
* Item

## Input / Entrada:
```
- Item
- Item
```
## Output / Saída:
- Item
- Item

## Input / Entrada:
```
+ Item
+ Item
```
## Output / Saída:
+ Item
+ Item

## Input / Entrada:
```
- Item
  - Item interno
  - Item interno
- Item
  - Item interno
  - Item interno
```
## Output / Saída:
- Item
  - Item interno
  - Item interno
- Item
  - Item interno
  - Item interno

---
## Referências:
[MarkdownGuide](https://www.markdownguide.org/getting-started/)   
[LeticiaCampos](https://dev.to/leticiacamposs2/escrevendo-textos-no-formato-markdown-usando-o-notepad-o99)