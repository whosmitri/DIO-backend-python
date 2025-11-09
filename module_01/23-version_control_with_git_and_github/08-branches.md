# Branches (ramificações)

* Uma branch é uma linha de desenvolvimento independente dentro do projeto.
* É um ponteiro móvel que aponta para um commit específico no histórico do repositório, permitindo evoluir o código sem afetar a branch principal.
* Ao criar uma branch a partir de outra já existente, ela nasce apontando para o mesmo commit que a branch original estava naquele momento.
* Branches são fundamentais para desenvolvimento paralelo, testes, correção de bugs e novas features sem quebrar o projeto principal.

## Criação, navegação e manipulação de Branches
* `git branch -v`: \
    Lista todas as branches existentes no repositório local, com a referência do último commit.

* `git checkout -b <nome-da-branch>`: \
    Cria uma nova branch e já muda para ela automaticamente.

* `git checkout <nome-da-branch>`: \
    Alterna para a branch desejada.

* `git merge <nome-da-branch>`: \
    Mescla as alterações da branch indicada para a branch atual.

* `git branch -d <nome-da-branch>`: \
    Exclui uma branch que não é mais necessária (após merge, por exemplo).

> **Observação**: para que uma branch exista também no repositório remoto, é necessário enviar ela com push após criá-la localmente: `git push -u origin <nome-da-branch>`

## Erros Comuns (e atenção especial)

### Conflitos de Merge

* Ocorrem quando duas alterações são feitas no mesmo local/linha de um arquivo em branches diferentes.

* O Git marca o conflito dentro do arquivo usando marcadores especiais: \
`<<<<<<<`, `=======`, `>>>>>>>`

* Estes marcadores indicam o bloco da sua branch versus a alteração da branch que está sendo mesclada.

## Comandos úteis do dia-a-dia

* `git fetch`: \
    Busca alterações do repositório remoto, mas não realiza merge automático. Excelente para atualizar contexto sem alterar arquivos locais.

* `git stash`: \
    Guarda (“arquiva temporariamente”) suas alterações locais sem precisar commitar.

* `git stash list`: \
    Lista todos os stashes salvos.

* `git stash pop`: \
    Aplica o stash mais recente e o remove do armazenamento.

* `git stash apply`: \
    Aplica o stash, mas mantém ele na lista (não remove).