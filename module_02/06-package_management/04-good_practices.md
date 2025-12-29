# Boas práticas em Python

Python possui um ecossistema maduro de convenções, padrões e recomendações formais, documentadas principalmente por meio das PEPs (Python Enhancement Proposals). Essas propostas descrevem desde detalhes de implementação da linguagem até diretrizes de estilo, legibilidade e organização de código.

Adotar essas boas práticas é essencial para:
* Melhorar a legibilidade do código;
* Facilitar a manutenção e evolução de projetos;
* Promover consistência em equipes de desenvolvimento;
* Reduzir erros e ambiguidades durante o desenvolvimento.

## PEPs (Python Enhancement Proposals)

* As PEPs são documentos oficiais que descrevem novas funcionalidades, processos ou padrões para a linguagem Python.
* Elas servem como referência técnica e histórica para decisões da comunidade Python.
* Nem todas as PEPs tratam de estilo; muitas abordam sintaxe, desempenho, governança e interoperabilidade.

## PEP 8 — Guia de Estilo para Código Python

A PEP 8 é a PEP mais amplamente adotada e tem como objetivo principal padronizar o estilo de escrita do código Python, promovendo clareza e uniformidade.

Ela define recomendações sobre:
* Identação;
* Comprimento de linhas;
* Convenções de nomenclatura;
* Organização de imports;
* Uso de espaços em branco;
* Estrutura geral do código.

* **Documentação oficial:** https://peps.python.org/pep-0008/

## Principais recomendações da PEP 8

### Identação
* Utilizar 4 espaços por nível de identação.
* Não utilizar tabulações.
* Garante consistência visual e evita ambiguidades entre editores.

### Comprimento de linha
* Limitar linhas a 79 caracteres.
* Para comentários e docstrings, o limite recomendado é 72 caracteres.
* Facilita leitura em telas menores e revisões de código.

### Convenções de nomenclatura
* **Funções e variáveis:** `snake_case`
* **Classes:** `CamelCase`
* **Constantes:** `UPPER_CASE`
* **Métodos “protegidos” (uso interno):** `_nome`
* **Métodos “privados”:** `__nome`

Essas convenções ajudam a identificar rapidamente o papel de cada elemento no código.

### Exemplo de código seguindo a PEP 8
```python
class ContaBancaria:
    # classe de exemplo que representa uma conta bancária
    pass


def somar(argumento_1, argumento_2):
    # função de exemplo que soma dois valores
    pass
```

Observações:
* Uso correto de identação;
* Nomes descritivos e padronizados;
* Separação adequada entre classes e funções;
* Inclusão de docstrings para documentação básica.

## Ferramentas de checagem de estilo

Ferramentas de linting são amplamente utilizadas para analisar código estaticamente e identificar:
* Violações da PEP 8;
* Erros comuns;
* Código potencialmente problemático;
* Inconsistências de estilo.

### Flake8
* Combina múltiplas ferramentas (PyFlakes, pycodestyle, McCabe).
* Muito utilizada em pipelines de CI/CD.
* Ideal para reforçar padrões de qualidade em projetos colaborativos.

#### Exemplo de uso:
```bash
pip install flake8
flake8 meu_script.py
```

## Formatação automática de código
### Black
* Black é um formatador automático de código Python.
* Segue a filosofia de “formato único e sem discussões”.
* Remove decisões subjetivas de estilo, padronizando todo o código automaticamente.
* Facilita revisões de código e reduz conflitos em controle de versão.

#### Exemplo de uso:
```bash
pip install black
black meu_script.py
```

> **Observação:** Black pode alterar a formatação além do mínimo exigido pela PEP 8, priorizando consistência. É amplamente adotado em projetos profissionais e open source.

## Organização de imports com isort
### isort
* Ferramenta responsável por organizar automaticamente os imports.
* Classifica importações em seções padrão:
    * Bibliotecas padrão do Python;
    * Bibliotecas de terceiros;
    * Imports locais do projeto.
* Ordena alfabeticamente e aplica espaçamentos adequados.

#### Exemplo de uso:
```bash
pip install isort
isort meu_script.py
```

Benefícios:
* Código mais limpo e previsível;
* Facilidade de leitura;
* Redução de conflitos em merges.

## Nota conceitual importante

As ferramentas citadas (como flake8, Black e isort) não são o foco principal, pois tecnologias podem mudar ao longo do tempo.

O ponto central é compreender os conceitos fundamentais:
* Padronização de código;
* Legibilidade e manutenção;
* Automação de boas práticas;
* Qualidade e profissionalismo no desenvolvimento de software.

Esses princípios permanecem relevantes independentemente das ferramentas específicas utilizadas.