from llm.model import llm


def planner_node(state):


    prompt = f"""

You are an autonomous AI planning agent.

Understand the user request:

{state['request']}


Create your own TODO execution list.

The request can belong to:

- Personal planning
- Travel
- Education
- Fitness
- Business
- Technical projects
- Research
- Events
- Reports


Instructions:

Create ONLY the important tasks required
to complete the user goal.


Rules:

- Maximum 4 tasks
- Each task must be actionable
- Do not explain
- Do not add numbering
- One task per line


Example:

Analyze user requirements
Prepare structured plan
Create detailed content
Finalize output

"""


    response = llm.invoke(prompt)


    tasks = [

        task.strip(
            "-1234567890. "
        )

        for task in response.content.split("\n")

        if task.strip()

    ]


    state["plan"] = tasks[:4]


    return state