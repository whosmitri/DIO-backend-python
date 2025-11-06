# Salvando alterações no repositório local (Git)

O processo de versionamento local no Git é baseado em etapas sucessivas e explícitas, permitindo controle granular sobre o que será registrado no histórico do projeto. Antes de enviar qualquer alteração para um repositório remoto (como o GitHub), todo o fluxo inicia localmente.

- `git status`: exibe o estado atual da árvore de trabalho. Mostra arquivos modificados, arquivos novos ainda não rastreados e arquivos já preparados para commit. É um comando essencial para validar o estado real do repositório antes de qualquer ação.

- `git add <nome-do-arquivo>`: insere arquivos individuais na stage area (área de preparação). É como selecionar manualmente apenas os arquivos que farão parte do próximo commit. Esse controle previne que alterações não relacionadas sejam versionadas juntas.

- `git add .`: adiciona todos os arquivos modificados e novos ao stage de uma vez. Útil quando todas as alterações fazem parte do mesmo contexto de atualização. Entretanto, exige maior cuidado, pois pode incluir arquivos não intencionais.

- `git commit -m "mensagem"`: registra definitivamente no histórico local tudo que está na stage. Cada commit representa um estado do projeto, com justificativa textual. O parâmetro -m permite escrever a mensagem concisa e objetiva do commit. Bons commits facilitam rastreabilidade e auditoria.

- `git log`: exibe o histórico completo de commits já realizados, com hash único de identificação, data, autor e mensagens. Permite consultar, auditar e navegar na evolução temporal do repositório.

Esse fluxo consolidado (status -> add -> commit -> log) é a base do controle de versão profissional com Git. Somente após estas etapas é que se realiza o envio remoto para plataformas como GitHub.