import os
from dotenv import load_dotenv
from agents import create_agents
from tasks import create_tasks
from crewai import Crew
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar as chaves da API
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# Inicializar ferramentas
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# Inicializar modelo de linguagem
llm = ChatOpenAI(model='gpt-3.5-turbo')

# Arquivos JSON
agents_file = './config/agents.json'
tasks_file = './config/tasks.json'

# Criar agentes
researcher, validator, reviewer, summary_writer = create_agents(agents_file, os.getenv('SERPER_API_KEY'))

# Criar tarefas
research, validate, review, write_post = create_tasks(tasks_file, researcher, validator, reviewer, summary_writer)

# Montar a equipe
crew = Crew(
    agents=[researcher, validator, reviewer, summary_writer],
    tasks=[research, validate, review, write_post],
    verbose=2,
    manager_llm=llm
)

# Executar as tarefas
crew.kickoff()
