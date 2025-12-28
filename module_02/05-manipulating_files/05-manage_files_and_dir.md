# Gerenciamento de Arquivos e Diretórios em Python

O gerenciamento de arquivos e diretórios é uma tarefa fundamental em aplicações Python que lidam com automação, organização de dados, processamento de arquivos ou administração de sistemas. Para esse fim, a linguagem disponibiliza módulos da biblioteca padrão, com destaque para `os` e `shutil`.

## Principais módulos utilizados

* `os`
    * Fornece uma interface para interação com o sistema operacional, permitindo manipular arquivos, diretórios, variáveis de ambiente e caminhos de forma multiplataforma.

* `shutil`
    * Oferece operações de alto nível para manipulação de arquivos e diretórios, como cópia, movimentação e remoção recursiva.

> **Observação:** ambos os módulos fazem parte da biblioteca padrão do Python, não sendo necessária a instalação de pacotes externos.

## Operações básicas com arquivos e diretórios

Com os módulos os e shutil, é possível:
* Criar diretórios
* Renomear arquivos ou diretórios
* Remover arquivos
* Mover arquivos entre diretórios
* Automatizar tarefas repetitivas no sistema de arquivos

Essas operações são amplamente utilizadas em scripts de automação, pipelines de dados e aplicações backend.

### Exemplo prático de código
```python
import os
import shutil

# Criar um diretório
os.mkdir('example')

# Renomear um arquivo
os.rename('old.txt', 'new.txt')

# Remover um arquivo
os.remove('unwanted.txt')

# Mover um arquivo
shutil.move('source.txt', 'destination.txt')
```

## Anotações e detalhes importantes
1. Criação de diretórios (`os.mkdir`)
    * Cria apenas um nível de diretório.
    * Gera um erro (`FileExistsError`) caso o diretório já exista.
    * Para criar diretórios aninhados, utiliza-se `os.makedirs()`.
    * `os.makedirs('a/b/c')`

2. Renomeação de arquivos (`os.rename`)
    * Pode ser usada tanto para arquivos quanto para diretórios.
    * Se o destino já existir, o comportamento depende do sistema operacional.
    * Também pode ser usada para mover arquivos dentro do mesmo sistema de arquivos.

3. Remoção de arquivos (`os.remove`)
    * Remove apenas arquivos, não diretórios.
    * Caso o arquivo não exista, ocorre um erro (FileNotFoundError).
    * Para remover diretórios vazios, utiliza-se `os.rmdir()`.

4. Movimentação de arquivos (`shutil.move`)
    * Move arquivos ou diretórios para outro local.
    * Se o destino estiver em outro sistema de arquivos, o shutil realiza uma cópia seguida da exclusão do original.
    * Pode ser usado como alternativa mais robusta ao os.rename().

## Boas práticas e dicas
* Sempre verificar se arquivos ou diretórios existem antes de manipulá-los: `os.path.exists('example')`
* Utilizar `try`/`except` para evitar que o programa seja interrompido por erros inesperados.
* Preferir `os.path.join()` para construir caminhos de forma portátil entre sistemas operacionais.
* Evitar operações destrutivas (como `remove` ou `rmtree`) sem validação prévia.

## Considerações finais

O uso adequado dos módulos os e shutil permite que aplicações Python interajam de forma segura e eficiente com o sistema de arquivos. Compreender essas operações é essencial para áreas como automação, administração de sistemas, ciência de dados e cibersegurança, onde o controle de arquivos é recorrente.