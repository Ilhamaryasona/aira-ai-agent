from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from memory import memory
from tools import tools
from prompts import SYSTEM_PROMPT

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    memory=memory,
    system_message=SYSTEM_PROMPT,
    verbose=True
)
