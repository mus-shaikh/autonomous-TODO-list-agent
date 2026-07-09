from langgraph.graph import StateGraph, END


from agent.state import AgentState

from agent.planner import planner_node

from agent.executor import executor_node

from tools.document_tool import (
    create_word_document
)



def document_node(state):


    path = create_word_document.invoke(

        {
            "content":
            state["final_document"]
        }

    )


    state["file_path"] = path


    return state



workflow = StateGraph(
    AgentState
)



workflow.add_node(
    "planner",
    planner_node
)


workflow.add_node(
    "executor",
    executor_node
)


workflow.add_node(
    "document",
    document_node
)



workflow.set_entry_point(
    "planner"
)



workflow.add_edge(
    "planner",
    "executor"
)


workflow.add_edge(
    "executor",
    "document"
)


workflow.add_edge(
    "document",
    END
)



agent = workflow.compile()