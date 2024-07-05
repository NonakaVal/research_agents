### Projeto de Pesquisa e Produção de Artigos com e sobre IA

- [crew-ai](https://www.crewai.com/)

#### Funcionalidades
##### Agentes e Ferramentas:
Utiliza agentes automatizados para realizar tarefas específicas.

##### Tarefas Automatizadas:
- Pesquisa de tendências.
- Validação de dados coletados.
- Revisão de conteúdo.
- Produção de artigos e posts baseados em dados.
- Estrutura do Projeto

##### Configuração:
Arquivos de configuração estão localizados na pasta config/.
Os arquivos JSON contêm definições de agentes e tarefas.

##### Componentes:

agents.py:_ Define os agentes e suas configurações._
tasks.py: _Define as tarefas a serem executadas, carregando configurações de um arquivo JSON._
main.py: _Orquestra a execução das tarefas através da criação de uma equipe (Crew) e execução das tarefas._

##### Requisitos de Instalação
Python 3.10 ou superior
Pacotes listados em pyproject.toml
Variáveis de ambiente configuradas em .env para chaves de API (Serper e OpenAI)
Como Usar

- Configuração inicial:
Clone o repositório.
Crie um ambiente virtual Python e ative-o.

- Instalação de dependências:
bash
Copy code
pip install -r requirements.txt
Configuração das variáveis de ambiente:

- Crie um arquivo .env na raiz do projeto com as variáveis SERPER_API_KEY e OPENAI_API_KEY.

##### Execução:

bash
Copy code
python main.py
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para discutir novas funcionalidades, melhorias ou correções.

Licença
Este projeto está licenciado sob a Licença MIT.
