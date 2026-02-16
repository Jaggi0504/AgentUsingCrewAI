from crewai import Agent, LLM
from tools import yt_tool
import os
from dotenv import load_dotenv

load_dotenv()
print("OPENAI KEY:", os.getenv("OPENAI_API_KEY"))

llm = LLM(
    model="groq/llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)



blog_researcher = Agent(
    role="Blog Researcher from YouTube videos",
    goal="Get the relevant video content for the topic {topic} from YouTube channel",
    verbose=True,
    memory=True,
    backstory="Expert in understanding AI videos and giving suggestions",
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compiling tech stories about the video {topic}",
    verbose=True,
    memory=True,
    backstory="You simplify complex topics into engaging narratives",
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)
