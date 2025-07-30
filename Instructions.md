# 📋 Setup Instructions - CrewAI Multi-Agent System

> 🚀 **Quick Setup Guide** - Get your AI agents up and running in minutes!

## 🎯 Prerequisites

Before we begin, make sure you have:

- 🐍 **Python 3.11.9** (Required - this specific version is important!)
- 🔑 **OpenAI API Key** ([Get yours here](https://platform.openai.com/api-keys))
- 💻 **Terminal/Command Prompt** access
- 📁 **Git** (for cloning the repository)

---

## 🛠️ Step-by-Step Installation

### 1️⃣ **Python Version Check**

First, verify you have the correct Python version:

```bash
python --version
```

**Expected Output:** `Python 3.11.9`

> ⚠️ **Important**: This project requires Python 3.11.9 specifically. If you have a different version, please install Python 3.11.9 from [python.org](https://www.python.org/downloads/)

---

### 2️⃣ **Navigate to Project Directory**

Make sure you're in the correct directory:

```bash
cd CrewAI-AgenticAI-Framework
```

> 📂 **Tip**: Use `pwd` (Linux/Mac) or `cd` (Windows) to check your current directory

---

### 3️⃣ **Create Environment Configuration**

Create a `.env` file in the project root directory:

#### Option A: Using Command Line

**Windows:**

```cmd
echo OPENAI_API_KEY=your_actual_api_key_here > .env
```

**Linux/Mac:**

```bash
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
```

#### Option B: Manual Creation

1. Create a new file named `.env` in the project root
2. Add the following content:

```env
OPENAI_API_KEY=your_actual_api_key_here
```

> 🔐 **Security Note**: Replace `your_actual_api_key_here` with your real OpenAI API key. Never share this key publicly!

---

### 4️⃣ **Setup Virtual Environment**

Create and activate a Python virtual environment:

#### **Windows (Command Prompt/PowerShell):**

```cmd
# Create virtual environment
python -m venv crew-env

# Activate virtual environment
crew-env\Scripts\activate
```

#### **Linux/Mac (Terminal):**

```bash
# Create virtual environment
python -m venv crew-env

# Activate virtual environment
source crew-env/bin/activate
```

> ✅ **Success Indicator**: You should see `(crew-env)` at the beginning of your command prompt

---

### 5️⃣ **Install Dependencies**

Install all required Python packages:

```bash
pip install -r requirements.txt
```

> ⏳ **Wait Time**: This may take a few minutes depending on your internet connection

---

### 6️⃣ **Verify Installation**

Test your setup by running the basic example:

```bash
python main.py
```

> 🎉 **Success**: If you see the AI agent system menu, congratulations! Your setup is complete.

---

## 🎮 Available Examples

### 🌱 **Basic Example - Single Agent**

```bash
python main.py
```

**Features:**

- 🤖 Interactive AI Agent System
- 🐍 Python Development Agent
- 📝 Documentation Agent  
- 📄 README Generator Agent
- 🔄 Menu-driven interface

### 🚀 **Advanced Example - Multi-Agent Team**

```bash
python test3agents.py
```

**Features:**

- 🔧 Technician Agent (Environment Setup)
- 🛡️ Security Agent (Keycloak Authentication)
- 🧪 Testing Agent (Quality Assurance)
- 👥 Collaborative workflow

---

## 🔧 Troubleshooting

### ❌ **Common Issues & Solutions**

#### **Issue: "OpenAI API Key not found"**

```
✅ Solution:
1. Check if .env file exists in project root
2. Verify the format: OPENAI_API_KEY=sk-...
3. Restart your terminal
4. Make sure there are no spaces around the = sign
```

#### **Issue: "Python version mismatch"**

```
✅ Solution:
1. Install Python 3.11.9 from python.org
2. Use pyenv for version management (recommended)
3. Verify with: python --version
```

#### **Issue: "Module not found"**

```
✅ Solution:
1. Activate virtual environment: crew-env\Scripts\activate
2. Install dependencies: pip install -r requirements.txt
3. Check you're in the correct directory
```

#### **Issue: "Virtual environment not activating"**

```
✅ Solution:
1. Windows: Use crew-env\Scripts\activate.bat
2. PowerShell: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Linux/Mac: Use source crew-env/bin/activate
```

---

## 📁 **Project File Structure**

```
📦 CrewAI-AgenticAI-Framework/
├── 🐍 main.py              # Interactive multi-agent system
├── 🔧 test3agents.py       # Advanced 3-agent collaboration
├── 📋 requirements.txt     # Python dependencies
├── 📝 Instructions.md      # This setup guide
├── 📖 README.md           # Project documentation
├── 🙈 .gitignore          # Git ignore rules
├── 🌍 .env                # Environment variables (you create this)
└── 📁 crew-env/           # Virtual environment (created during setup)
```

---

## 🎯 **Next Steps**

After successful installation:

1. 🎮 **Try the Examples**: Run both `main.py` and `test3agents.py`
2. 📚 **Read the Documentation**: Check out the detailed README.md
3. 🛠️ **Customize Agents**: Modify agent roles and tasks
4. 🚀 **Build Your Own**: Create custom multi-agent workflows

---

## 🆘 **Need Help?**

If you encounter any issues:

1. 📖 **Check the README.md** for detailed documentation
2. 🐛 **Report Issues**: [GitHub Issues](https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework/issues)
3. 💬 **Community Support**: [CrewAI Community](https://community.crewai.com/)
4. 📧 **Contact**: [Help Center](https://help.crewai.com)

---

<div align="center">

### 🎉 **You're All Set!** 🎉

**Ready to explore the future of AI collaboration?**

*Happy coding with your AI agent team! 🤖✨*

</div>
