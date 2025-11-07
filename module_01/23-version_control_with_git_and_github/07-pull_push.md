# Trabalhando com o repositório remoto (enviar e receber alterações)

Após configurar um repositório remoto no GitHub e definir uma branch principal, é comum sincronizar o trabalho local com o servidor remoto. Existem dois comandos essenciais para esse fluxo:

- `git pull`: \
    Busca do servidor remoto as alterações mais recentes e as integra ao seu repositório local. Mantém o ambiente atualizado com o que outros desenvolvedores fizeram (ou você mesmo em outra máquina).

- `git push -u origin main`: \
    Envia para o GitHub tudo que foi commitado localmente, atualizando o repositório remoto. \
    O parâmetro `-u` cria o vínculo (tracking) da branch local com a branch remota main, facilitando o uso de próximos comandos `git push` e `git pull` sem precisar especificar o remoto e branch novamente.

## Em resumo:

Primeiro sempre puxe antes de desenvolver, para evitar conflitos e trabalhar atualizado (`pull`).

Depois, quando terminar sua evolução e com seus commits feitos, envie suas alterações para o GitHub (`push`).