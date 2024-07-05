import json
from crewai.agent import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool

def create_agents(agents_file, serper_api_key):
    with open(agents_file, 'r') as f:
        agents_data = json.load(f)

    researcher = Agent(
        role=agents_data['senior_research_analyst']['role'],
        goal=agents_data['senior_research_analyst']['goal'],
        backstory=agents_data['senior_research_analyst']['backstory'],
        tools=[SerperDevTool(api_key=serper_api_key), WebsiteSearchTool()],
        verbose=True
    )

    validator = Agent(
        role=agents_data['senior_validation_specialist']['role'],
        goal=agents_data['senior_validation_specialist']['goal'],
        backstory=agents_data['senior_validation_specialist']['backstory'],
        tools=[],
        verbose=True
    )

    reviewer = Agent(
        role=agents_data['senior_review_editor']['role'],
        goal=agents_data['senior_review_editor']['goal'],
        backstory=agents_data['senior_review_editor']['backstory'],
        tools=[],
        verbose=True
    )

    summary_writer = Agent(
        role=agents_data['senior_summary_writer']['role'],
        goal=agents_data['senior_summary_writer']['goal'],
        backstory=agents_data['senior_summary_writer']['backstory'],
        tools=[],
        verbose=True
    )

    return researcher, validator, reviewer, summary_writer
