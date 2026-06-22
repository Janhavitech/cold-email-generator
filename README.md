# 📧 AI Cold Email Generator

An AI-powered tool that generates personalized cold emails for job/business outreach. Paste in a company's careers page URL, and the app scrapes the job listing, understands the role using an LLM, and drafts a tailored cold email — automatically matching relevant portfolio projects to the job description using vector similarity search (RAG).

## 🎯 Problem It Solves
Writing a personalized cold email for every single job or client lead takes time. This tool automates outreach by combining web scraping, LLM-based information extraction, and retrieval-augmented matching of relevant past work.

## 🛠️ Tech Stack
- **LangChain** – orchestration of LLM prompt chains
- **Groq (LLaMA 3.1)** – fast LLM inference for extraction and email generation
- **ChromaDB** – vector database for portfolio similarity search (RAG)
- **Streamlit** – web app interface
- **Python** – pandas, python-dotenv, BeautifulSoup/Selenium for scraping

## ⚙️ How It Works
1. User pastes a company's careers/job page URL into the app
2. The page is scraped and the raw text is cleaned
3. An LLM (via Groq) extracts the job role and key requirements from the text
4. A portfolio of past projects (tech stack + links) is embedded and stored in ChromaDB
5. The extracted job requirements are used to query ChromaDB for the most relevant portfolio links (Retrieval-Augmented Generation)
6. The LLM drafts a personalized cold email referencing the matched projects
7. The generated email is displayed in the Streamlit app

## 📁 Project Structure
```
cold-email-generator/
├── app/
│   ├── main.py              # Streamlit app entry point
│   ├── chains.py            # LLM prompt chains (job extraction + email writing)
│   ├── portfolio.py         # ChromaDB portfolio storage & retrieval
│   ├── utils.py             # Text cleaning utilities
│   └── Resource/
│       └── my_portfolio.csv # Sample portfolio data (tech stack + links)
├── requirements.txt
└── README.md
```

## 🚀 Setup & Installation
1. Clone the repository
   ```bash
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator/app
   ```
2. Install dependencies
   ```bash
   pip install -r ../requirements.txt
   ```
3. Get a free API key from [Groq Console](https://console.groq.com/) and create a `.env` file inside the `app/` folder:
   ```
   GROQ_API_KEY=your_own_api_key_here
   ```
4. Run the app
   ```bash
   streamlit run main.py
   ```

## 🔮 Future Improvements
- Support multiple LLM providers (OpenAI, Gemini) as fallback options
- Add tone customization (formal / casual / concise)
- Improve portfolio matching with semantic re-ranking
- Add support for PDF job descriptions, not just URLs

## 👩‍💻 Author
Janhavi — Data Science graduate exploring GenAI & LLM-powered applications.
