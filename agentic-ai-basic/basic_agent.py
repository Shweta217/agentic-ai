from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

# Step 1: Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Step 2: Load tool (calculator)
tools = load_tools(["llm-math"], llm=llm)

# Step 3: Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Step 4: Run agent
result = agent.run("What is 23 * 7 plus 89?")
print("Answer:", result)
