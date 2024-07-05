# Agentes de Pesquisa e Produção de Artigos com e sobre IA

- [crew-ai](https://www.crewai.com/)

## Funcionalidades
### Agentes e Ferramentas:
Utiliza agentes automatizados para realizar tarefas específicas.

### Tarefas Automatizadas:
- Pesquisa de tendências.
- Validação de dados coletados.
- Revisão de conteúdo.
- Produção de artigos e posts baseados em dados.
- Estrutura do Projeto

### Configuração:
Arquivos de configuração estão localizados na pasta config/.
Os arquivos JSON contêm definições de agentes e tarefas.

### Componentes:

agents.py:_ Define os agentes e suas configurações._
tasks.py: _Define as tarefas a serem executadas, carregando configurações de um arquivo JSON._
main.py: _Orquestra a execução das tarefas através da criação de uma equipe (Crew) e execução das tarefas._


