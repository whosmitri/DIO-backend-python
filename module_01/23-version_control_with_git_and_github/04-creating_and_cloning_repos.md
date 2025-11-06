# Criando e Clonando Repositórios

Para começar a trabalhar com Git, é necessário ter um repositório. Ele pode ser criado localmente ou clonado de um repositório remoto.

## 1. Criar repositório local

- `git init`: inicializa o controle de versão em uma pasta local já existente. A partir deste ponto, o Git passa a rastrear alterações e permitir commits.

## 2. Clonar repositório remoto

- `git clone <url-do-repositorio>`: clona um repositório remoto (ex: GitHub) para sua máquina, trazendo código e histórico já existente.
- `git clone <url> --branch <nome> --single-branch`: clona somente um branch específico, reduzindo download e carga local. Caso não especifique branch, o padrão costuma ser o main.

## 3. Conectar repositório local ao remoto
- `git remote add origin <url-do-repositorio>`: vincula o repositório local ao GitHub, permitindo enviar (push) ou buscar atualizações (pull). origin é o nome padrão do repositório remoto principal.

---

Com isso, estabelecemos a base do fluxo Git: criar ou clonar, conectar ao remoto e, a partir daí, versionar e sincronizar alterações.