# Manipulando Arquivos em Python

## Por que precisamos manipular arquivos?

A manipulação de arquivos é um dos pilares da programação, pois permite que aplicações lidem com dados de forma persistente e estruturada.

* Arquivos são essenciais para praticamente qualquer tipo de software, desde scripts simples até sistemas complexos.
* Permitem o armazenamento permanente de dados, possibilitando que informações sejam reutilizadas mesmo após o encerramento da execução de um programa.
* Viabilizam a entrada e saída de dados (I/O), servindo como meio de comunicação entre o programa, o usuário e outros sistemas.

* São fundamentais para:
    * registro de logs e auditorias;
    * leitura de configurações;
    * persistência de resultados de processamento;
    * integração entre aplicações distintas.
* Diferenciam-se das variáveis em memória, pois:
    * variáveis existem apenas durante a execução do programa;
    * arquivos permanecem armazenados no sistema de arquivos até serem explicitamente removidos.

> **Observação:**
    Em aplicações reais, a persistência de dados pode ocorrer tanto por meio de arquivos quanto por bancos de dados. O estudo de arquivos é um passo inicial para compreender mecanismos mais avançados de armazenamento.

## Conceito de arquivo em informática

* Um arquivo é um container lógico no computador onde informações são armazenadas em formato digital.
* Ele é identificado por:
    * um nome;
    * uma extensão (que geralmente indica o tipo ou formato);
    * um caminho no sistema de arquivos.
* Arquivos são gerenciados pelo sistema operacional, que controla:
    * permissões de leitura, escrita e execução;
    * localização no disco;
    * acesso simultâneo por diferentes processos.

* Do ponto de vista da programação, um arquivo é tratado como um fluxo de dados (stream), permitindo operações sequenciais de leitura e escrita.

## Tipos de arquivos manipuláveis em Python

Em Python, os arquivos podem ser classificados, de forma geral, em dois grandes grupos:

### Arquivos de texto
* Armazenam dados em formato legível por humanos.
* Cada caractere é representado segundo uma codificação (ex.: UTF-8).
* Exemplos comuns:
    * `.txt`, `.csv`, `.md`, `.json`, `.xml`

* São amplamente utilizados para:
    * registros de logs;
    * arquivos de configuração;
    * troca de dados entre sistemas.

* **Vantagem:** fácil leitura, edição e depuração.
* **Limitação:** menor eficiência para dados complexos ou volumosos.

### Arquivos binários

* Armazenam dados em formato bruto (bytes).
* Não são legíveis diretamente por humanos.

* Exemplos comuns:
    * imagens (`.png`, `.jpg`);
    * áudio (`.mp3`, `.wav`);
    * vídeo (`.mp4`);
    * arquivos executáveis.

* São utilizados quando:
    * é necessário maior eficiência;
    * os dados possuem estrutura específica;
    * o conteúdo não é textual.

* **Vantagem:** maior desempenho e compactação.
* **Limitação:** exigem interpretação específica pelo programa.

## Anotações importantes para estudo

* A manipulação de arquivos envolve conceitos como:
    * abertura e fechamento de arquivos;
    * modos de acesso (leitura, escrita, anexação);
    * tratamento de exceções;
    * codificação de caracteres.

* Em Python, o uso correto de arquivos está diretamente ligado a boas práticas de:
    * gerenciamento de recursos;
    * segurança;
    * confiabilidade do software.

> **Dica:**
    Antes de avançar para bancos de dados ou sistemas distribuídos, dominar leitura e escrita de arquivos ajuda a consolidar conceitos fundamentais de persistência e entrada/saída.