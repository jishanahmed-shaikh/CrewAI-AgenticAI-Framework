# 🤖 CrewAI Agentic AI Framework & Multi-Agent System

[![Python](https://img.shields.io/badge/Python-3.11.9-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com)

> 🚀 **Welcome to the future of AI collaboration!** This project demonstrates how to build powerful multi-agent systems using CrewAI, where AI agents work together like a real team to solve complex problems.

## 🌟 What is CrewAI?

CrewAI is a cutting-edge framework that enables you to orchestrate role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks more effectively than any single AI could alone.

### 🎯 Key Features

- 🤝 **Multi-Agent Collaboration**: Agents work together like a real team
- 🎭 **Role-Based Agents**: Each agent has specific roles and expertise
- 🔄 **Sequential Task Execution**: Tasks flow logically from one agent to another
- 🛠️ **Custom Tools**: Extend agents with specialized capabilities
- 📊 **Verbose Logging**: Track every step of the process

## 📁 Project Structure

```
📦 CrewAI-Project/
├── 🐍 main.py              # Interactive multi-agent system
├── 🔧 test3agents.py       # Advanced 3-agent collaboration
├── 📋 requirements.txt     # Python dependencies
├── 📝 Instructions.md      # 📋 Detailed setup guide
├── 🙈 .gitignore          # Git ignore rules
├── 🌍 .env                # Environment variables (create this)
└── 📖 README.md           # This file
```

## 🚀 Quick Start Guide

> 📋 **Detailed Setup Instructions**: For a comprehensive step-by-step guide, see our [**Instructions.md**](Instructions.md) file!

### 📋 Prerequisites

- 🐍 **Python 3.11.9** (Required version)
- 🔑 **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- 💻 **Terminal/Command Prompt/Powershell**

### 🛠️ Installation Steps

#### 1️⃣ Clone & Navigate

```bash
git clone https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework.git
cd CrewAI-AgenticAI-Framework
```

#### 2️⃣ Create Environment File

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_actual_api_key_here
```

> 🔐 **Security Note**: Never commit your API key to version control!

#### 3️⃣ Setup Virtual Environment

```bash
# Create virtual environment
python -m venv crew-env

# Activate it (Windows)
crew-env\Scripts\activate

# Activate it (macOS/Linux)
source crew-env/bin/activate
```

#### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎮 Running the Examples

### 🌱 Basic Example (Single Agent)

Perfect for beginners! This example shows a single Python developer agent:

```bash
python main.py
```

**What it does:**

- 🤖 Creates a Python Developer agent
- 📝 Assigns a task to reverse a string
- ✅ Executes and shows the result

### 🚀 Advanced Example (Multi-Agent System)

This showcases the real power of CrewAI with 3 specialized agents:

```bash
python test3agents.py
```

**Meet the Team:**

- 🔧 **Technician Agent**: Sets up software and environments
- 🛡️ **Security Agent**: Handles authentication with Keycloak
- 🧪 **Testing Agent**: Validates everything works perfectly

## 🏗️ Understanding the Architecture

### 🤖 Agent Components

```python
agent = Agent(
    role="Your Agent's Job Title",           # 🎭 What they do
    goal="What they want to achieve",        # 🎯 Their objective
    backstory="Their background story",      # 📚 Their expertise
    verbose=True,                           # 📢 Show their work
    tools=[custom_tools]                    # 🛠️ Special abilities
)
```

### 📋 Task Structure

```python
task = Task(
    description="What needs to be done",     # 📝 The assignment
    expected_output="What you expect",       # ✅ Success criteria
    agent=assigned_agent                     # 🤖 Who does it
)
```

### 👥 Crew Assembly

```python
crew = Crew(
    agents=[agent1, agent2, agent3],        # 🤖 The team
    tasks=[task1, task2, task3],            # 📋 The work
    verbose=True                            # 📊 Show progress
)
```

## 🛠️ Creating Custom Tools

Want to give your agents superpowers? Here's how to create custom tools:

```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class CustomToolInput(BaseModel):
    parameter: str = Field(..., description="Tool parameter")

class CustomTool(BaseTool):
    name = "ToolName"
    description = "What this tool does"
    args_schema = CustomToolInput
    
    def _run(self, parameter: str) -> str:
        # Your tool logic here
        return f"Tool executed with: {parameter}"
```

## 🎯 Use Cases & Applications

### 🏢 Business Applications

- 📊 **Data Analysis Pipeline**: Research → Analysis → Reporting
- 🛒 **E-commerce Automation**: Product research → Content creation → Marketing
- 📈 **Financial Planning**: Market analysis → Strategy → Risk assessment

### 💻 Development Workflows

- 🔧 **DevOps Pipeline**: Setup → Security → Testing (like our example!)
- 📱 **App Development**: Planning → Coding → Testing → Deployment
- 🐛 **Bug Resolution**: Detection → Analysis → Fix → Verification

### 🎨 Creative Projects

- ✍️ **Content Creation**: Research → Writing → Editing → Publishing
- 🎬 **Video Production**: Scripting → Storyboarding → Editing → Review
- 🎵 **Music Production**: Composition → Arrangement → Mixing → Mastering

## 🔧 Troubleshooting

> 📋 **Need More Help?** Check our comprehensive [**Instructions.md**](Instructions.md) for detailed troubleshooting steps!

### Common Issues & Solutions

#### 🚫 "OpenAI API Key not found"

- ✅ Check your `.env` file exists
- ✅ Verify the key format: `OPENAI_API_KEY=sk-...`
- ✅ Restart your terminal after creating `.env`

#### 🐍 "Python version mismatch"

- ✅ Use Python 3.11.9 specifically
- ✅ Check with: `python --version`
- ✅ Consider using pyenv for version management

#### 📦 "Module not found"

- ✅ Activate your virtual environment
- ✅ Run: `pip install -r requirements.txt`
- ✅ Check you're in the right directory

## 📚 Learning Resources

### 🎓 Official Documentation

- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [LangChain Docs](https://python.langchain.com/docs/introduction/)
- [LangChain Tools & Agents](https://python.langchain.com/docs/how_to/#agents)

### 🎬 Videos, Courses & Tutorials

- [CrewAI Crash Course Multi-Agent Systems Explained](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- [AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)

### 📖 Recommended Reading

- "Multi-Agent Systems" by Gerhard Weiss
- "Artificial Intelligence: A Modern Approach" by Russell & Norvig
- "The Alignment Problem" by Brian Christian

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch: `git checkout -b amazing-feature`
3. 💾 Commit your changes: `git commit -m 'Add amazing feature'`
4. 📤 Push to the branch: `git push origin amazing-feature`
5. 🎉 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎉 **CrewAI Team** for the amazing framework
- 🤖 **OpenAI** for the powerful language models
- 🐍 **Python Community** for the excellent ecosystem
- 👥 **Contributors** who make this project better

## 📞 Support & Community

- 💬 **Community**: [Join the CrewAI community](https://community.crewai.com/)
- 🐦 **Twitter**: [@CrewAI](https://x.com/@crewAIInc)
- 📧 **Help**: [Help](https://help.crewai.com)
- 🐛 **Issues**: [GitHub Issues](https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework/issues)

---

<div align="center">

### 🌟 Star this repo if you found it helpful! 🌟

**Made with ❤️ by the Mr. [Jishanahmed AR Shaikh](https://linktr.ee/jishanahmedshaikh) for the AI Community**

*"The future belongs to organizations that can harness the collective intelligence of AI agents working in harmony."*

</div>

## 🚀 What's Next?

Ready to build your own AI agent team? Here are some ideas:

- 🎯 **Customer Service Crew**: Support → Escalation → Resolution
- 📊 **Market Research Team**: Data collection → Analysis → Insights
- 🎨 **Creative Agency**: Brainstorming → Design → Review → Refinement
- 🏥 **Healthcare Assistant**: Symptoms → Diagnosis → Treatment → Follow-up

The possibilities are endless! 🌈

---
*Happy coding! 🎉*
