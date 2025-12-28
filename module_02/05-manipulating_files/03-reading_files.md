# Leitura de Arquivos em Python

Em Python, a leitura de arquivos é realizada por meio da função embutida open(), que permite acessar arquivos armazenados no sistema de arquivos para operações de leitura, escrita ou ambos.
Neste contexto, serão abordados os principais métodos utilizados para leitura de arquivos de texto.

## Abertura de Arquivos
* Para ler um arquivo, utiliza-se o modo `'r'` (read):

```python
file = open('example.txt', 'r')
```
* `'example.txt'` é o caminho do arquivo.
* `'r'` indica que o arquivo será aberto apenas para leitura.
* Caso o arquivo não exista, será gerada uma exceção (`FileNotFoundError`).

Após o uso, é fundamental fechar o arquivo com `close()` para liberar recursos do sistema.

## Métodos de Leitura
### 1. read()
O método `read()` lê todo o conteúdo do arquivo de uma vez e retorna uma única string.

```python
file = open('example.txt', 'r')
print(file.read())
file.close()
```

* **Características:**
    * Retorna uma str contendo todo o texto do arquivo.
    * Mantém quebras de linha (\n) originais.
    * Indicado para arquivos pequenos ou quando é necessário processar todo o conteúdo de uma só vez.

> **Observação:**
    Em arquivos muito grandes, o uso de read() pode causar alto consumo de memória, pois todo o conteúdo é carregado de uma vez.

### 2. readline()
O método readline() lê apenas uma linha por chamada, retornando-a como uma string.

```python
file = open('example.txt', 'r')
print(file.readline())
file.close()
```

* **Características:**
    * Cada chamada lê a próxima linha do arquivo.
    * Inclui o caractere de quebra de linha (`\n`) ao final da string.
    * Útil para processamento sequencial ou leitura controlada de grandes arquivos.

### 3. readlines()
O método readlines() lê todas as linhas do arquivo e retorna uma lista, onde cada elemento corresponde a uma linha.

```python
file = open('example.txt', 'r')
lines = file.readlines()
print(lines)
file.close()
```

* **Características:**
    * Retorna uma `list[str]`.
    * Cada elemento da lista contém uma linha, incluindo `\n`.
    * Facilita iteração e manipulação linha a linha.
    * Pode consumir muita memória em arquivos extensos.

## Comparação entre os Métodos
| Método | Retorno |	Leitura	Uso recomendado |
| - | - | - |
| `read()` |	`str` |	Arquivo inteiro	Arquivos pequenos |
| `readline()` |	`str` |	Uma linha por vez	Leitura controlada |
| `readlines()` |	`list[str]` |	Todas as linhas	Manipulação em lista |

## Boas Práticas
* Sempre feche o arquivo após o uso com a função `close()`.
* Prefira leitura linha a linha para arquivos grandes.
* Utilize nomes de variáveis descritivos (ex.: file, lines, content).
* Evite manter arquivos abertos por longos períodos.

> **Nota:**
    Em aplicações modernas, é altamente recomendável o uso da estrutura with, que gerencia automaticamente a abertura e o fechamento do arquivo (será abordado em aulas posteriores).