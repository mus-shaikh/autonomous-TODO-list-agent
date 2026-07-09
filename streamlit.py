import streamlit as st
import requests
import os
import time


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(

    page_title="AI Document Agent",

    layout="wide"
)


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown(
"""

<style>

.stApp {

background:#0f172a;

}


.main-title {

font-size:42px;
font-weight:800;
text-align:center;
color:white;

}


.subtitle {

text-align:center;
color:#cbd5e1;
font-size:17px;

}

</style>

""",

unsafe_allow_html=True
)



# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
"""

<div class='main-title'>
Autonomous AI Document Agent
</div>

<br>

""",

unsafe_allow_html=True
)



# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:


    st.title(
        "Agent Architecture"
    )


    st.success(
        "FastAPI"
    )

    st.success(
        "LangGraph Planner"
    )

    st.success(
        "Parallel Executor"
    )

    st.success(
        "Reflection Agent"
    )

    st.success(
        "DOCX Tool"
    )



# --------------------------------------------------
# Main Layout
# --------------------------------------------------

left,right = st.columns(
    [1.2,1]
)



with left:


    st.subheader(
        "Describe your document requirement"
    )


    user_request = st.text_area(

        "Input",

        height=220,

        placeholder=
        "Example: Give one week minimum budget travel plan for Mumbai"

    )


    run = st.button(

        "Run AI Agent",

        use_container_width=True
    )




with right:


    st.subheader(
        "Agent Execution Status"
    )


    status = st.empty()




# --------------------------------------------------
# Agent Call
# --------------------------------------------------

if run:


    if not user_request:


        st.warning(
            "Please enter a request"
        )


    else:


        try:


            status.info(
                "Creating execution plan..."
            )


            time.sleep(0.5)


            response = requests.post(

                "http://127.0.0.1:8000/agent",

                json={

                    "request":
                    user_request

                }

            )


            data=response.json()



            if data["status"]=="completed":


                status.success(

                    "Agent completed successfully"

                )


                st.divider()



                st.subheader(
                    "Generated TODO List"
                )


                for index,task in enumerate(

                    data["execution_plan"],

                    start=1

                ):


                    st.write(

                        f"{index}. {task}"

                    )



                st.divider()



                st.subheader(

                    "Generated Document"

                )


                file_path = data["document"]



                if os.path.exists(
                    file_path
                ):


                    with open(
                        file_path,
                        "rb"
                    ) as file:


                        st.download_button(

                            "Download Word Document",

                            file,

                            file_name=
                            "AI_Document.docx",

                            mime=
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

                            use_container_width=True

                        )



                else:


                    st.error(

                        "Document file not found"

                    )


            else:


                st.error(

                    "Agent failed"

                )



        except Exception as e:


            st.error(

                f"""

Connection Error:

{e}

Ensure FastAPI backend is running.

"""

            )