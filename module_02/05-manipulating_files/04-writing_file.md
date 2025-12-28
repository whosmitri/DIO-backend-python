# Escrita em arquivos em Python

A escrita em arquivos é uma operação fundamental em programação, utilizada para persistência de dados, geração de logs, exportação de resultados e comunicação entre processos.

## Métodos para escrita

Em Python, os principais métodos para escrever dados em arquivos são:

* `write()`
    * Escreve uma única string no arquivo.
    * Não adiciona quebra de linha automaticamente (\n deve ser inserido manualmente).
    * Retorna o número de caracteres escritos.

* `writelines()`
    * Escreve uma sequência de strings (lista, tupla ou outro iterável).
    * Não adiciona quebras de linha automaticamente.
    * Cada string deve conter \n caso se deseje escrever em linhas separadas.

## Modos de abertura de arquivo

É essencial abrir o arquivo no modo correto, pois isso define o comportamento da escrita:

* `'w'` (write)
    * Cria o arquivo se ele não existir.
    * Sobrescreve o conteúdo caso o arquivo já exista.

* `'a'` (append)
    * Cria o arquivo se ele não existir.
    * Adiciona o conteúdo ao final do arquivo, sem apagar o conteúdo existente.

* `'x'` (exclusive creation)
    * Cria um novo arquivo.
    * Gera erro se o arquivo já existir (útil para evitar sobrescrita acidental).

* Exemplo básico de escrita
```python
file = open('example.txt', 'w')
file.write('Hello world!')
file.close()
```

## Observações importantes
* O método close() deve sempre ser chamado após a escrita para:
    * Garantir que os dados sejam efetivamente gravados no disco.
    * Liberar recursos do sistema operacional.
* Se o programa encerrar inesperadamente antes do close(), os dados podem não ser salvos corretamente.

## Escrita de múltiplas linhas

* Exemplo usando `writelines()`:
``` python
lines = [
    'Primeira linha\n',
    'Segunda linha\n',
    'Terceira linha\n'
]

with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## Considerações adicionais
* Arquivos de texto utilizam codificação de caracteres (por padrão, UTF-8). Para especificar explicitamente:
```python
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Texto com acentuação')
```

* Escrita em arquivos é uma operação de I/O (Input/Output), que pode ser relativamente lenta; por isso, deve ser feita de forma consciente em aplicações maiores. Erros comuns incluem:
    * Esquecer o modo correto ('w' em vez de 'a').
    * Não incluir \n ao escrever múltiplas linhas.
    * Não fechar o arquivo corretamente.