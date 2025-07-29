from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

# Only for tools
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

# Load your OpenAI key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Custom tool definition
class InstallSoftwareInput(BaseModel):
    command: str = Field(..., description="The shell command to run for installation")

class InstallSoftwareTool(BaseTool):
    name = "InstallSoftware"
    description = "Installs software on a machine by executing setup commands."

    args_schema: Type[BaseModel] = InstallSoftwareInput

    def _run(self, command: str, run_manager=None) -> str:
        return f"Simulating: Executing install command -> {command}"

    def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not implemented")

# Define the tool instance
install_tool = InstallSoftwareTool()

# AGENTS
technician = Agent(
    role="Technician Agent",
    goal="Setup the machine with required software and environments.",
    backstory="Expert in DevOps and software setup. Handles environment provisioning.",
    verbose=True,
    tools=[install_tool]
)

security = Agent(
    role="Security Agent",
    goal="Secure the machine by setting up authentication using Keycloak.",
    backstory="Expert in cybersecurity and identity management.",
    verbose=True
)

tester = Agent(
    role="Testing Agent",
    goal="Test if the environment is properly setup and everything works as expected.",
    backstory="QA professional responsible for ensuring system stability.",
    verbose=True
)

# TASKS
task1 = Task(
    description="Install required packages, setup Python, Docker, and Kubernetes using kubeadm.",
    expected_output="Machine setup successfully with all dependencies installed.",
    agent=technician
)

task2 = Task(
    description="Integrate Keycloak with the app, configure roles, users, and ensure secure login.",
    expected_output="Authentication system added and working.",
    agent=security
)

task3 = Task(
    description="Run unit and integration tests to validate the setup and authentication flow.",
    expected_output="All tests passed and system is stable.",
    agent=tester
)

# CREW
crew = Crew(
    agents=[technician, security, tester],
    tasks=[task1, task2, task3],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n📦 Final Output:")
    print(result)