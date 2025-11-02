# Introdução

## Sistemas de Controle de Versão (Version Control Systems – VCS)

São ferramentas que registram e organizam o histórico de evolução de arquivos e projetos.
Permitem saber exatamente o que mudou, quando mudou e quem fez a mudança.
Trazem mais controle, segurança, rastreabilidade e colaboração em projetos – especialmente em equipes.

## Tipos de Sistemas de Controle de Versão
* VCS Centralizado (CVCS)
  * Existe um servidor único que armazena todo o histórico e arquivos do projeto.
  * Os usuários acessam esse servidor para visualizar ou modificar o código.
  * Ponto crítico: se o servidor central cair ou ficar indisponível, o trabalho pode parar, pois ele é o único detentor do histórico principal.

* VCS Distribuído (DVCS)
  * Cada desenvolvedor mantém uma cópia completa do repositório localmente, incluindo o histórico.
  * Permite trabalhar offline, mesmo sem conexão com servidor.
  * Cada clone funciona como um backup.
  * Maior flexibilidade de fluxo de trabalho, colaboração e versionamento paralelo (branches, experimentações, etc).

**Hoje, o modelo DVCS é o padrão mais adotado mundialmente. Git é o exemplo mais famoso e dominante deste modelo.**
