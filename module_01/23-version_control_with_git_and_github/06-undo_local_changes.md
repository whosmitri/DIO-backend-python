# Desfazendo Alterações no Repositório Local

## Restaurar arquivos na árvore de trabalho (working tree)
- `git restore <arquivo>`: \
    Retorna o arquivo ao estado da última versão confirmada (commit), descartando alterações locais não enviadas. Útil quando você quer “voltar atrás” sem criar novo commit.

## Alterar a mensagem do último commit
- `git commit --amend -m "nova mensagem"`: \
    Substitui rapidamente a mensagem do último commit já feito, sem abrir editor.

- `git commit --amend`: \
    Abre o editor padrão (como vim) para editar a mensagem do último commit. \
    **Importante**: não use `amend` em commits já publicados no remoto, exceto se souber lidar com reescrita de histórico.

## Desfazer alterações de commits já realizados (`reset`)

Antes, consulte o histórico:

- `git log`: \
    Permite visualizar o histórico com os hashes dos commits anteriores.

Depois, escolha o tipo de reset desejado:

- `git reset --soft <hash>`: \
    Reverte o commit para o hash especificado, mas mantém todas as alterações do commit na área de stage (preparação). Útil se quiser refazer commits, mas manter o código como está.

- `git reset --mixed <hash> (padrão)`: \
    Reverte commits e mantém os arquivos alterados somente na working tree (tira do stage). É o reset mais comum para rework.

- `git reset --hard <hash>`: \
    Reverte commit e descarta completamente as alterações tanto do stage quanto da working tree. \
    **Uso crítico**: destrói alterações locais.

## Visualizar histórico total, incluindo referências internas
- `git reflog`: \
    Lista todo o histórico interno do Git, inclusive ações como reset, checkout, merges, etc. Permite recuperar estados mesmo após comandos destrutivos.

## Remover apenas o último arquivo adicionado no stage
- `git reset (sem parâmetros)`: \
    Remove o último arquivo enviado ao stage, mantendo sua alteração apenas na working tree, sem apagar código.