from crewai import Agent
from tools import yt_tool

##Create a blog content researcher

blog_researcher=Agent(
    role="Blog Researcher from YouTube videos",
    goal="Get the relevant video content for the topic {topic} from YouTube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, and Gen AI and give suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

##Create a blog writer agent with YT tool

blog_writer=Agent(
    role="Blog Writer",
    goal="Narrate compiling tech stories about the video {topic} from YouTube channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=False
)