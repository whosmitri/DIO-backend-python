# Trabalhando com Arquivos CSV em Python

## Conceito de CSV (Comma-Separated Values)
* CSV (Comma-Separated Values) é um formato de arquivo simples e amplamente utilizado para o armazenamento de dados tabulares.
* Os dados são organizados em linhas e colunas, onde:
    * Cada linha representa um registro.
    * Cada coluna representa um atributo.
* Os valores são separados, por padrão, por vírgulas, mas podem utilizar outros delimitadores (como `;` ou `\t`), dependendo da localidade ou configuração.
* Arquivos CSV são leves, portáveis e compatíveis com diversas ferramentas, como:
    * Planilhas eletrônicas (Excel, LibreOffice Calc)
    * Bancos de dados
    * Linguagens de programação

> **Observação:** Apesar de simples, o formato CSV não armazena informações de tipo (inteiro, string, data), apenas texto.

## Manipulação de CSV em Python
* O Python fornece o módulo padrão csv, que permite a leitura e escrita de arquivos CSV de forma segura e eficiente.
* Esse módulo abstrai detalhes importantes, como:
    * Separadores de campos
    * Quebras de linha
    * Aspas e caracteres especiais
* Para utilizá-lo, é necessário importar o módulo:
    ```python
    import csv
    ```

## Leitura de Arquivos CSV

### Exemplo básico de leitura
```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Explicação técnica
* `open('example.csv', 'r')`: abre o arquivo no modo leitura.
* `with`: garante o fechamento automático do arquivo, mesmo em caso de erro.
* `csv.reader(file)`: cria um objeto iterável que lê o CSV linha por linha.
* Cada row é uma lista de strings, representando uma linha do arquivo.

> **Nota:** Todos os dados lidos do CSV são retornados como `str`. Caso seja necessário trabalhar com números, é preciso convertê-los explicitamente (`int`, `float`, etc.).

## Escrita de Arquivos CSV

### Exemplo básico de escrita
```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'idade'])
    writer.writerow(['Miguel', 18])
    writer.writerow(['Dmitri', 19])
```

### Explicação técnica
* `open('example.csv', 'w')`: abre o arquivo no modo escrita (sobrescreve o conteúdo existente).
* `newline=''`: evita a criação de linhas em branco adicionais, especialmente em sistemas Windows.
* `csv.writer(file)`: cria um objeto responsável pela escrita no formato CSV.
* `writer.writerow()`: escreve uma única linha no arquivo.

> **Observação:** Para escrever múltiplas linhas de uma vez, pode-se utilizar writer.`writerows()` com uma lista de listas.

## Boas Práticas Recomendadas
* Utilizar `csv.reader` e `csv.writer` em vez de manipular strings manualmente.
* Sempre abrir arquivos utilizando o gerenciador de contexto (`with`).
* Definir explicitamente:
    * `newline=''` ao escrever arquivos CSV.
    * `encoding='utf-8'` para evitar problemas com caracteres acentuados.

* Exemplo recomendado:
    ```python
    with open('example.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
    ```

* Implementar tratamento de exceções, especialmente para:
    * Arquivo não encontrado (`FileNotFoundError`)
    * Erros de permissão (`PermissionError`)
    * Dados mal formatados

* Exemplo simples:
    ```python
    try:
        with open('example.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    ```

## Considerações Didáticas e Técnicas
* O módulo csv é ideal para arquivos pequenos e médios.
* Para grandes volumes de dados ou análises estatísticas, bibliotecas como pandas são mais adequadas.
* CSV é um formato amplamente utilizado em:
    * Ciência de dados
    * Engenharia de dados
    * Automação de processos
    * Interoperabilidade entre sistemas