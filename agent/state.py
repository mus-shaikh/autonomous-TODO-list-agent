from typing import TypedDict, List


class AgentState(TypedDict):

    request: str

    plan: List[str]

    final_document: str

    file_path: str