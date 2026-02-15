from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

##Research Task
research_task=Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel"
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of the video",
    tools=[yt_tool],
    agent=blog_researcher,
)

writing_task=Task(
    description=(
        "Get the information from the youtube channel on the topic {topic} and create the content for the blog"
        ),
        tools=[yt_tool],
        agent=blog_writer,
        async_execution=False,
        output_file="blog-post.md",
)