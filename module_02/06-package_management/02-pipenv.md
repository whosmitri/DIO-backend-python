# Gerenciamento de Dependências com Pipenv (Python)

## Introdução ao Pipenv

O Pipenv é uma ferramenta oficial recomendada pela Python Software Foundation para o gerenciamento de dependências em projetos Python. Ele integra, de forma unificada:
* Gerenciamento de pacotes (substituindo o uso direto do `pip`)
* Criação e controle de ambientes virtuais
* Registro e versionamento de dependências

Diferentemente do uso tradicional de `pip + venv + requirements.txt`, o Pipenv automatiza e padroniza esse processo, reduzindo erros de configuração e inconsistências entre ambientes.

### Principais características
* Cria automaticamente um ambiente virtual isolado para cada projeto
* Utiliza arquivos `Pipfile` e `Pipfile.lock` para controle de dependências
* Separa dependências de produção e desenvolvimento
* Resolve dependências transitivas automaticamente
* Garante reprodutibilidade do ambiente

## Arquivos principais do Pipenv

### Pipfile

O `Pipfile` substitui o `requirements.txt` e descreve as dependências do projeto de forma legível e organizada.

Ele é dividido, geralmente, em três seções principais:

* `[packages]`: dependências necessárias para execução do projeto
* `[dev-packages]`: dependências usadas apenas em desenvolvimento (ex.: linters, testes)
* `[requires]`: versão do Python utilizada no projeto

Exemplo conceitual:
```toml
[packages]
numpy = "*"
requests = ">=2.0"

[dev-packages]
pytest = "*"
black = "*"

[requires]
python_version = "3.11"
```

### Pipfile.lock

O `Pipfile.lock` é um arquivo gerado automaticamente e não deve ser editado manualmente. Ele contém:
* Versões exatas de todas as dependências
* Dependências transitivas (subdependências)
* Hashes criptográficos dos pacotes

Esse arquivo é essencial para garantir que o ambiente seja reproduzido exatamente da mesma forma em qualquer máquina ou servidor.

## Instalação do Pipenv
### Instalação global
```bash
pip install pipenv
```

> **Observação:** recomenda-se instalar o Pipenv globalmente, pois ele gerencia os ambientes virtuais por projeto de forma independente.

## Comandos básicos do Pipenv

### Criar ambiente virtual e instalar uma biblioteca
```bash
pipenv install numpy
```
* Cria o ambiente virtual (caso não exista)
* Instala a biblioteca especificada
* Atualiza automaticamente o Pipfile e o Pipfile.lock

### Instalar dependência de desenvolvimento
```bash
pipenv install pytest --dev
```
* A biblioteca será adicionada à seção `[dev-packages]`.

### Remover uma biblioteca
```bash
pipenv uninstall numpy
```
* Remove a biblioteca do ambiente virtual
* Atualiza o `Pipfile` e o `Pipfile.lock`

### Ativar o ambiente virtual
```bash
pipenv shell
```
* Permite executar comandos Python dentro do ambiente isolado do projeto.

### Executar comandos sem entrar no shell
```bash
pipenv run python script.py
```

## Congelamento de dependências: `pipenv lock`
```bash
pipenv lock
```

### Função do comando

O comando `pipenv lock` gera (ou atualiza) o arquivo Pipfile.lock, congelando:
* Versões exatas das dependências diretas
* Versões das dependências transitivas
* Hashes de integridade dos pacotes

### Importância do Pipfile.lock
* Garante consistência entre ambientes de desenvolvimento, teste e produção
* Evita problemas causados por atualizações inesperadas de bibliotecas
* Facilita deploys e integração contínua (CI/CD)
* Reduz falhas de compatibilidade e erros difíceis de rastrear

> **Boa prática:** sempre versionar o Pipfile.lock em projetos colaborativos ou ambientes de produção.

## Boas práticas no uso do Pipenv
* Utilizar o Pipenv por projeto, nunca para múltiplos projetos ao mesmo tempo
* Versionar Pipfile e Pipfile.lock no controle de versão (Git)
* Separar claramente dependências de produção e desenvolvimento
* Evitar o uso simultâneo de requirements.txt e Pipenv
* Definir explicitamente a versão do Python no Pipfile

## Considerações finais

O Pipenv simplifica o gerenciamento de dependências em Python ao unir ambiente virtual, controle de versões e segurança em uma única ferramenta. Seu uso é especialmente indicado para:
* Projetos acadêmicos
* Desenvolvimento profissional
* Ambientes colaborativos
* Aplicações que exigem reprodutibilidade e controle rigoroso de dependências