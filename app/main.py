import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input(
        "Enter a URL:",
        value="https://careers.nike.com/career-areas"
    )

    submit_button = st.button("Submit")

    if submit_button:
        try:
            # 1. Load and clean website text
            loader = WebBaseLoader([url_input])
            raw_text = loader.load().pop().page_content
            cleaned_data = clean_text(raw_text)

            # 2. Load portfolio into Chroma
            portfolio.load_portfolio()

            # 3. Extract job context (TEXT, not JSON)
            job_context = llm.extract_jobs(cleaned_data)

            # 4. Query portfolio using job context
            links = portfolio.query_links(job_context)

            # 5. Generate cold email
            email = llm.write_mail(job_context, links)

            # 6. Display result
            st.subheader("Generated Cold Email")
            st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()

    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    create_streamlit_app(chain, portfolio, clean_text)
