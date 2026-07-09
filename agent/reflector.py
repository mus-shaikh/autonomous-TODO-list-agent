from llm.model import llm


def reflection_node(state):


    content = "\n\n".join(
        state["task_outputs"]
    )


    prompt=f"""

You are a professional AI document editor.

Your task is to convert the completed work
into a polished final document.


Original User Request:

{state['request']}


Completed Agent Work:

{content}



Instructions:

Understand the document type automatically.

Examples:

Personal request:
Create personal plans, schedules,
checklists or action items.

Learning request:
Create roadmap, milestones,
practice plan and resources.

Technical request:
Create architecture,
implementation steps,
requirements and explanation.

Business request:
Create proposal,
strategy,
analysis and recommendations.


Rules:

- Create a suitable title
- Choose headings according to the topic
- Do not force business sections everywhere
- Use clear professional headings
- Use bullet lists for actions/features/tasks

Important bullet rule:
Every bullet point MUST start with "-"

Example:

- Define project goals
- Prepare weekly milestones
- Track progress regularly


Writing rules:

- Remove repeated information
- Keep paragraphs short
- Finish every sentence completely
- Do not use markdown symbols
- Do not use ### or **
- Maintain professional tone

End with a meaningful conclusion.

"""


    response = llm.invoke(prompt)


    state["final_document"] = (
        response.content
    )


    return state