# Introdução

A programação é a atividade de criar instruções lógicas e estruturadas para que um computador execute tarefas específicas. Essas instruções são escritas por meio de linguagens de programação, que seguem regras sintáticas e semânticas bem definidas.

No entanto, além da linguagem utilizada, a forma como um problema é analisado, estruturado e resolvido no código depende diretamente do paradigma de programação adotado.

## Paradigmas de Programação

### Conceito

Um paradigma de programação é um estilo ou modelo de programação que define a forma como os problemas são abordados e solucionados por meio do código.

Ele influencia:
* A organização do código
* A forma de pensar a solução
* A estrutura dos dados
* A maneira como as instruções são executadas

> **Importante:**
    Um paradigma não é uma linguagem de programação.
    Linguagens como Python, Java e C podem suportar um ou mais paradigmas simultaneamente.

## Relação entre linguagem e paradigma

* Uma linguagem pode ser:
    * Monoparadigma (ex.: C — predominantemente imperativo/procedural)
    * Multiparadigma (ex.: Python — imperativo, orientado a objetos e funcional)

* O paradigma adotado depende mais da forma como o desenvolvedor escreve o código do que da linguagem em si.

## Principais paradigmas de programação

### Paradigma Imperativo (ou Procedural)
* Baseia-se na ideia de sequência de comandos que alteram o estado do programa.

* O foco está em:
    * Como o programa executa as tarefas
    * Passo a passo da solução

* Características:
    * Uso intenso de variáveis
    * Estruturas de controle (if, for, while)
    * Funções e procedimentos
    * Código executado de forma linear

* Exemplos de linguagens:
    * C
    * Pascal
    * Python (quando usado de forma procedural)

### Paradigma Funcional
* Baseia-se no conceito matemático de funções.

* O foco está em:
    * O que deve ser feito, não como
    * Evitar efeitos colaterais e estados mutáveis

* Características:
    * Funções puras
    * Imutabilidade de dados
    * Uso frequente de funções como parâmetros
    * Menor dependência de variáveis globais

* Exemplos de linguagens:
    * Haskell
    * Lisp
    * Python (suporte parcial, com lambda, map, filter, reduce)

### Paradigma Orientado a Eventos
* O fluxo do programa é controlado por eventos, como:
    * Cliques do usuário
    * Pressionar teclas
    * Respostas de rede
    * Temporizadores

* Características:
    * Muito utilizado em interfaces gráficas e aplicações web
    * Código reage a eventos específicos
    * Uso de handlers (tratadores de eventos)

* Exemplos de uso:
    * Interfaces gráficas (Tkinter, PyQt)
    * Desenvolvimento web
    * Jogos

## Programação Orientada a Objetos (POO)

### Conceito

A Programação Orientada a Objetos (POO) é um paradigma que organiza o código a partir da abstração de entidades do mundo real, representadas como objetos.

Cada objeto:
* Possui características (atributos)
* Executa comportamentos (métodos)

Esse modelo aproxima o código da realidade, tornando-o:
* Mais legível
* Mais modular
* Mais reutilizável
* Mais fácil de manter e expandir

### Vantagens da POO
* Melhor organização do código
* Facilidade de manutenção
* Reaproveitamento de código
* Escalabilidade de sistemas grandes
* Separação clara de responsabilidades

## Observação importante
* Em Python, tudo é um objeto:
    * Números
    * Strings
    * Listas
    * Funções
* Isso torna Python uma linguagem fortemente alinhada à POO, mesmo sendo multiparadigma.