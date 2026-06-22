import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )

    def extract_jobs(self, cleaned_text: str) -> str:
        prompt_extract = PromptTemplate.from_template(
            """
            Below is text scraped from a company's careers page.

            Extract the job roles and summarize them in simple text.
            Do NOT return JSON.
            Do NOT add explanations.

            TEXT:
            {page_data}
            """
        )

        chain = prompt_extract | self.llm
        res = chain.invoke({"page_data": cleaned_text})

        return res.content

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### PORTFOLIO LINKS:
            {link_list}

            ### INSTRUCTION:
            You are Mohan, a Business Development Executive at AtliQ.
            AtliQ is an AI & Software Consulting company that helps businesses
            automate processes, improve efficiency, and scale using technology.

            Write a concise, professional cold email to the client regarding
            the job mentioned above, clearly explaining how AtliQ can fulfill
            their needs.

            Do NOT add greetings like "Hope you are doing well".
            Do NOT add explanations.
            Do NOT provide a preamble.

            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": links
        })

        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
