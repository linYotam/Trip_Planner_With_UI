# 🏖️ VacAIgent: Streamlit-Integrated AI Crew for Trip Planning

## Running the Application

To experience the VacAIgent app:

- **Install Dependencies**: Execute `pip install -r requirements.txt` in your terminal.
- **Launch the App**: Run `streamlit run streamlit_app.py` to start the Streamlit interface.

★ **Disclaimer**: The application uses GPT-4 by default. Ensure you have access to OpenAI's API and be aware of the associated costs.

## Details & Explanation

- **Streamlit UI**: The Streamlit interface is implemented in `streamlit_app.py`, where users can input their trip details.
- **Components**:
  - `./trip_tasks.py`: Contains task prompts for the agents.
  - `./trip_agents.py`: Manages the creation of agents.
  - `./tools directory`: Houses tool classes used by agents.
  - `./streamlit_app.py`: The heart of the Streamlit app.

## Using GPT 3.5

To switch from GPT-4 to GPT-3.5, pass the llm argument in the agent constructor:

```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o-mini') # Loading gpt-3.5-turbo (see more OpenAI models at https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4)

class TripAgents:
    # ... existing methods

    def local_expert(self):
        return Agent(
            role='Local Expert',
            goal='Provide insights about the selected city',
            tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website],
            llm=llm,
            verbose=True
        )

```

## Using Local Models with Ollama

For enhanced privacy and customization, you can integrate local models like Ollama:

### Setting Up Ollama

- **Installation**: Follow Ollama's guide for installation.
- **Configuration**: Customize the model as per your requirements.

### Integrating Ollama with CrewAI

Pass the Ollama model to agents in the CrewAI framework:

```python
from langchain.llms import Ollama

ollama_model = Ollama(model="agent")

class TripAgents:
    # ... existing methods

    def local_expert(self):
        return Agent(
            role='Local Expert',
            tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website],
            llm=ollama_model,
            verbose=True
        )

```

## Benefits of Local Models

- **Privacy**: Process sensitive data in-house.
- **Customization**: Tailor models to fit specific needs.
- **Performance**: Potentially faster responses with on-premises models.
