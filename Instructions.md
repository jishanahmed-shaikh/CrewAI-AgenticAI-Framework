# Setup & Usage Guide

## Prerequisites

- Python 3.11+
- Git
- Internet connection

## Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework.git
cd CrewAI-AgenticAI-Framework
```

### Step 2: Run Setup
```bash
python setup.py
```

The script will:
- Check Python version
- Create virtual environment
- Install dependencies
- Configure .env file
- Verify installation

### Step 3: Activate Environment
```bash
# Windows
crewai_workshop\Scripts\activate

# macOS/Linux
source crewai_workshop/bin/activate
```

### Step 4: Verify Installation
```bash
pip list | grep crewai
cat .env  # Check API key is set
```

## Running the Workshop

```bash
python main.py
```

Menu options:
1. Dev Agent - Write Python code
2. Doc Agent - Generate documentation
3. README Generator - Create project docs
4. Code Review - Analyze code
5. Help - Get tips
6. Exit

## API Configuration

### Get GROQ API Key (FREE)
1. Visit https://console.groq.com/keys
2. Sign up (no credit card needed)
3. Create API key
4. Copy key (starts with `gsk_`)

### Get OpenAI API Key (PAID)
1. Visit https://platform.openai.com/api-keys
2. Sign up + add payment
3. Create API key
4. Copy key (starts with `sk_`)

## Troubleshooting

### Python Version Error
```bash
python --version  # Need 3.11+
# Download from https://python.org
```

### API Key Not Found
- Check .env file exists
- Verify key format (GROQ: `gsk_`, OpenAI: `sk_`)
- Restart terminal
- Run `python setup.py` again

### Module Not Found
```bash
# Activate virtual environment first
pip install -r requirements.txt
```

### Connection Timeout
- Check internet connection
- Check API status pages
- Try again in a few minutes

## Creating Custom Agents

### 1. Plan Your Agent
Create `AGENT_PLAN.md`:
```markdown
# Agent Name

## Role
[What does it do?]

## Goal
[What does it achieve?]

## Backstory
[Background and expertise]

## Use Cases
- [Use case 1]
- [Use case 2]
```

### 2. Implement Agent
Create `custom_agent.py`:
```python
from crewai import Agent, Task, Crew

custom_agent = Agent(
    role="Your Role",
    goal="Your Goal",
    backstory="Your Backstory",
    verbose=True
)

def create_task(description):
    return Task(
        description=description,
        expected_output="Expected output",
        agent=custom_agent
    )

if __name__ == "__main__":
    task = create_task("Your task")
    crew = Crew(agents=[custom_agent], tasks=[task], verbose=True)
    result = crew.kickoff()
    print(result)
```

### 3. Test Your Agent
```bash
python custom_agent.py
```

### 4. Add Unit Tests
Create `test_custom_agent.py`:
```python
import unittest
from custom_agent import custom_agent

class TestCustomAgent(unittest.TestCase):
    def test_agent_initialization(self):
        assert custom_agent.role is not None
    
    def test_task_creation(self):
        task = create_task("Test")
        assert task is not None

if __name__ == '__main__':
    unittest.main()
```

### 5. Integrate into Main App
Edit `main.py`:
- Import your agent
- Add menu option
- Create handler function
- Test integration

### 6. Submit PR
```bash
git checkout -b feature/your-agent-name
git add .
git commit -m "feat: Add [Agent Name]"
git push origin feature/your-agent-name
# Create PR on GitHub
```

## Learning Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [GROQ API Docs](https://console.groq.com/docs)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [LangChain Docs](https://python.langchain.com/)

## Support

- GitHub Issues: https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework/issues
- CrewAI Community: https://community.crewai.com/
- Twitter: https://x.com/@crewAIInc
