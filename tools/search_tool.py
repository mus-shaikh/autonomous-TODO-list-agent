from langchain_core.tools import tool
from duckduckgo_search import DDGS


@tool
def web_search(query: str) -> str:

    """
    Searches live internet information.
    Used for factual information like:
    hotels, pricing, ratings, news, companies.
    """

    results = []


    with DDGS() as ddgs:

        for r in ddgs.text(
            query,
            max_results=5
        ):

            results.append(
                f"""
Title:
{r['title']}

Information:
{r['body']}

Source:
{r['href']}
"""
            )


    return "\n".join(results)