# Gerenciamento de Dependências com Poetry

## Introdução ao Poetry

O Poetry é uma ferramenta moderna de gerenciamento de dependências e empacotamento para projetos em Python. Seu objetivo principal é simplificar o controle do ambiente de desenvolvimento, garantindo reprodutibilidade, isolamento e consistência entre diferentes máquinas e colaboradores.

Diferentemente do uso direto do `pip` com arquivos `requirements.txt`, o Poetry:
* Centraliza a configuração do projeto em um único arquivo (`pyproject.toml`);
* Resolve automaticamente conflitos de dependências;
* Cria e gerencia ambientes virtuais de forma transparente;
* Facilita o empacotamento e a publicação de projetos no PyPI (Python Package Index).

## Principais características
* Declaração explícita de dependências e versões compatíveis
* Geração automática do arquivo `poetry.lock`, que fixa versões exatas
* Suporte nativo a dependências de desenvolvimento (ex: testes e lint)
* Integração com padrões modernos do ecossistema Python (PEP 517 e PEP 518)

2. Estrutura básica de um projeto com Poetry

Ao criar ou inicializar um projeto com Poetry, os principais arquivos gerados são:

* `pyproject.toml`: Arquivo central do projeto. Contém:
    * Metadados do projeto (nome, versão, descrição, autores)
    * Dependências principais (`[tool.poetry.dependencies]`)
    * Dependências de desenvolvimento (`[tool.poetry.group.dev.dependencies]`)

* `poetry.lock`
    * Arquivo de bloqueio que registra as versões exatas das dependências instaladas.
    * Esse arquivo é essencial para garantir que todos os desenvolvedores utilizem o mesmo ambiente.

## Instalação do Poetry

A instalação pode ser feita via pip, embora em ambientes profissionais seja comum utilizar o instalador oficial.

* Instalação global via pip (forma simplificada)
```bash
pip install poetry
```
> **Observação:** Em sistemas Linux e macOS, pode ser necessário garantir que o diretório de scripts do Python esteja no `PATH`.

## Criando um projeto do zero com Poetry

Para criar um novo projeto estruturado automaticamente:
```bash
poetry new myproject
```

Esse comando cria:
* Um diretório chamado myproject
* Um pacote Python inicial
* O arquivo `pyproject.toml`
* Uma estrutura básica de testes

Em seguida, navegue até a pasta do projeto:
```bash
cd myproject
```

## Gerenciamento de dependências

### Adicionando pacotes

Para adicionar uma nova dependência ao projeto:
```bash
poetry add numpy
```

Esse comando:
* Atualiza o pyproject.toml
* Resolve dependências compatíveis
* Atualiza o poetry.lock
* Instala o pacote no ambiente virtual do projeto

> **Dica:** É possível especificar versões, por exemplo:
```bash
poetry add numpy@^1.26
```

### Removendo pacotes

Para remover uma dependência:
```bash
poetry remove numpy
```

O pacote é removido tanto do ambiente quanto da configuração do projeto.

### Visualizando dependências instaladas

Para listar todos os pacotes instalados no projeto:
```bash
poetry show
```

Esse comando exibe:
* Nome do pacote
* Versão instalada
* Descrição resumida

Para visualizar a árvore de dependências:
```bash
poetry show --tree
```

## Utilizando Poetry em um projeto existente

Caso o projeto já exista (sem Poetry), é possível inicializá-lo:
```bash
poetry init
```

Esse comando:
* Faz perguntas interativas sobre o projeto
* Permite adicionar dependências manualmente
* Cria o arquivo pyproject.toml sem alterar a estrutura atual

> **Boa prática:** Após o poetry init, recomenda-se rodar: `poetry install` para criar o ambiente virtual e instalar as dependências declaradas.

## Considerações acadêmicas e boas práticas

* O uso do Poetry melhora a reprodutibilidade científica e acadêmica de projetos em Python.
* O arquivo `poetry.lock` deve ser versionado em sistemas de controle de versão (ex: Git).
* A separação entre dependências de produção e desenvolvimento facilita manutenção e deploy.
* O Poetry reduz erros comuns de incompatibilidade de versões em ambientes colaborativos.