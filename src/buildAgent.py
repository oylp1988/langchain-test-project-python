from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import getpass
import os

# LANGSMITH_TRACING="true"
# LANGSMITH_API_KEY = ""
# LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
# os.environ["TAVILY_API_KEY"] = "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"
# Create the agent
load_dotenv()
memory = MemorySaver()
model = ChatOllama(
    model="mistral",
    temperature=0,
    # other params...
)
search = TavilySearchResults(max_results=2)
# search_results = search.invoke("what is the weather in SF")
# print(search_results)
tools = [search]
# model_with_tools = model.bind_tools(tools)
# response = model_with_tools.invoke([("user", "what is the weather in SF")])
# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")

agent_executor = create_react_agent(model, tools)
# response = agent_executor.invoke({"messages": [HumanMessage(content="whats the weather in sf?")]})
# print(f"Response : {response}")
for step in agent_executor.stream(
    {"messages": [HumanMessage(content="whats the weather in sf?")]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()