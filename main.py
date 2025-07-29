from crewai import Agent, Task, Crew

# Step 1: Create an Agent
dev_agent = Agent(
    role="Python Developer",
    goal="Write clean Python code for any problem",
    backstory="An expert Python programmer who follows best practices.",
    verbose=True
)

# Step 2: Create a Task for the Agent
dev_task = Task(
    description="Write a Python function to reverse a string.",
    expected_output="Python code that takes a string and returns it reversed.",
    agent=dev_agent
)

# Step 3: Assemble the Crew and Assign the Task
crew = Crew(
    agents=[dev_agent],
    tasks=[dev_task],
    verbose=True
)

# Step 4: Run the Crew
result = crew.kickoff()
print("\n✅ Final Output:")
print(result)