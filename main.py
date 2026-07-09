from fastapi import FastAPI, HTTPException

from pydantic import (
    BaseModel,
    Field
)

from agent.graph import agent


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(

    title="Autonomous AI Document Agent",

    description=(
        "LangGraph based autonomous AI agent "
        "that understands requests, creates TODO plans, "
        "executes tasks and generates professional DOCX documents."
    ),

    version="1.0.0"
)


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class AgentRequest(BaseModel):

    request: str = Field(

        min_length=5,

        description=
        "Natural language instruction for the autonomous agent"

    )


# --------------------------------------------------
# Health Endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {

        "status": "running",

        "message":
        "Autonomous AI Document Agent API is active"

    }



# --------------------------------------------------
# Agent Endpoint
# --------------------------------------------------

@app.post("/agent")
def run_agent(
        data: AgentRequest
):

    try:


        # Initial LangGraph State

        initial_state = {

            # User request

            "request":
            data.request,


            # Planner generated TODO list

            "plan":
            [],


            # Executor generated final content

            "final_document":
            "",


            # DOCX tool output path

            "file_path":
            ""

        }



        result = agent.invoke(
            initial_state
        )



        return {

            "status":
            "completed",


            "message":
            "Agent executed successfully",


            # Showing autonomous thinking

            "execution_plan":
            result["plan"],


            "document":
            result["file_path"]

        }



    except Exception as error:


        raise HTTPException(

            status_code=500,

            detail=str(error)

        )