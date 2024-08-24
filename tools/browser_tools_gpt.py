import requests
import streamlit as st
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from langchain.chat_models import ChatOpenAI

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        """Useful to scrape and summarize a website's content."""
        
        # Fetch the website content using requests
        response = requests.get(website)
        if response.status_code != 200:
            return f"Failed to retrieve content from {website}, status code: {response.status_code}"
        
        # Extract text content from HTML
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        
        # Chunk content into smaller pieces (if too large for a single call)
        content_chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        
        summaries = []
        
        # Initialize the GPT-4o-mini model using LangChain's ChatOpenAI
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)  # Using GPT-4
        for chunk in content_chunks:
            # Define agent using GPT-4
            agent = Agent(
                role='Principal Researcher',
                goal='Summarize web content and extract key information.',
                backstory="You're a researcher analyzing website content.",
                llm=llm,  # Set the LLM to GPT-4
                allow_delegation=False
            )
            
            # Define the task for the agent
            task = Task(
                agent=agent,
                description=f"Please summarize the following content:\n\nCONTENT\n----------\n{chunk}"
            )
            
            # Execute the task and get the summary
            summary = task.execute()
            summaries.append(summary)
        
        # Combine all summaries into one
        return "\n\n".join(summaries)
