from crewai import Agent, Task
from composio_crewai import ComposioToolset, App, Action
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType
llm = ChatOpenAI(openai_api_key="sk-**", model="gpt-4-0613")

composioCrewAI = ComposioToolset([App.GITHUB, App.LINEAR])

agent = Agent(role='Github-Linear TODO Agent',
  goal="""Take action on Linear via Linear APIs based on Github commits. Linear Project to create issues: Hermes""",
  backstory="""You are an AI Agent with access to Github and Linear and wants to keep the Github Code TODOs and Linear in Sync. Linear Project to create issues: Hermes""",
  verbose=True,
  tools=composioCrewAI,
  llm=llm)

#TODO: Multiple errors can be wrapped inside an exception.
