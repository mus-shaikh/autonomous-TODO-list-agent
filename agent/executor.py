from llm.model import llm


def executor_node(state):


    prompt = f"""

You are an autonomous execution agent.

User request:

{state['request']}


Your generated TODO list:

{state['plan']}


Execute every TODO step.

Create the final document content.

Adapt automatically:

Travel:
- itinerary
- budget
- checklist

Learning:
- roadmap
- milestones

Technical:
- architecture
- implementation

Personal:
- action plan

Business:
- professional proposal


Formatting rules:

- Create a clear title
- Use proper headings
- Use bullet points starting with "-"
- Keep sections organized
- Complete all sentences
- Professional tone
- No markdown symbols


"""


    response = llm.invoke(
        prompt
    )


    state["final_document"] = (
        response.content
    )


    return state