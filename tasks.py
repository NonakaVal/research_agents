import json
from crewai.task import Task

def create_tasks(tasks_file, researcher, validator, reviewer, summary_writer):
    with open(tasks_file, 'r') as f:
        tasks_data = json.load(f)

    research = Task(
        description=tasks_data['research']['description'],
        expected_output=tasks_data['research']['expected_output'],
        agent=researcher
    )

    validate = Task(
        description=tasks_data['validate']['description'],
        expected_output=tasks_data['validate']['expected_output'],
        agent=validator
    )

    review = Task(
        description=tasks_data['review']['description'],
        expected_output=tasks_data['review']['expected_output'],
        agent=reviewer
    )

    write_post = Task(
        description=tasks_data['write_post']['description'],
        expected_output=tasks_data['write_post']['expected_output'],
        agent=summary_writer,
        output_file=tasks_data['write_post']['output_file']
    )

    return research, validate, review, write_post
