<div align="center">

# 🚀 CrewAI Workshop

**Learn Multi-Agent Systems with Free Tools**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://crewai.com)
[![GROQ](https://img.shields.io/badge/GROQ-Free-orange.svg)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 What is This?

A hands-on workshop to learn how AI agents work together to solve complex problems. Build multi-agent systems using CrewAI with free tools (GROQ API).

---

## ⚡ Setup (5 Minutes)

### Step 1: Star & Fork the Repository

1. Click **⭐ Star** button (top right) - VERY IMPORTANT ⚠️🚨 [if you miss this, you will have 20+ Errors in your terminal]
2. Click **Fork** button (top right)
3. Select your account

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/CrewAI-AgenticAI-Framework.git
cd CrewAI-AgenticAI-Framework
```

### Step 3: Run Setup Script

```bash
python setup.py
```

The script will:
- ✅ Check Python version (3.11+)
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create `.env` file

### Step 4: Add Your API Keys

The script will ask for API keys. Choose one:

**Option A: GROQ (FREE - Recommended)**
1. Visit: https://console.groq.com/keys
2. Sign up (no credit card needed)
3. Create API key
4. Copy and paste into terminal

**Option B: OpenAI (PAID)**
1. Visit: https://platform.openai.com/api-keys
2. Sign up + add payment method
3. Create API key
4. Copy and paste into terminal

### Step 5: Verify Setup

The terminal will ask:
```
✅ Setup complete! Continue? (yes/no):
```

Type `yes` to confirm.

Your `.env` file is now configured with:
- API keys
- Model settings
- Provider configuration

### Step 6: Activate Virtual Environment

```bash
# Windows
crewai_workshop\Scripts\activate

# macOS/Linux
source crewai_workshop/bin/activate
```

You should see `(crewai_workshop)` in your terminal prompt.

---

## 🎓 Learn by Running

### Run the Workshop

```bash
python main.py
```

You'll see a menu with 4 agents:

```
1. 🐍 Dev Agent       → Write Python code
2. 📝 Doc Agent       → Generate documentation
3. 📄 README Generator → Create project docs
4. 🔍 Code Review     → Analyze code quality
5. ❓ Help            → Get tips
6. 🚪 Exit
```

### Try Each Agent

**Dev Agent (Option 1)**
- Task 1: Reverse a string
- Task 2: Check if palindrome
- Task 3: Custom Python task

Watch the AI write code for you!

**Doc Agent (Option 2)**
- Task 1: Report on Computers
- Task 2: Report on Internet
- Task 3: Custom documentation

See how it generates comprehensive docs!

**README Generator (Option 3)**
- Describe your project
- Get a professional README

**Code Review Agent (Option 4)**
- Paste your code
- Get detailed analysis

---

## 🤖 How Agents Work

Each agent has:
- **Role** - What they do
- **Goal** - What they want to achieve
- **Backstory** - Their expertise
- **Tools** - Special abilities

Agents work together to complete tasks!

---

## 📁 Project Structure

```
.
├── setup.py              # Automated setup
├── main.py               # Main application
├── config.py             # Configuration
├── utils.py              # Utilities
├── test3agents.py        # Advanced example
├── requirements.txt      # Dependencies
├── .env.example          # Config template
├── README.md             # This file
└── Instructions.md       # Detailed guide
```

---

## 🔧 Troubleshooting

### Python Version Error
```bash
python --version  # Need 3.11+
# Download from https://python.org
```

### API Key Not Found
- Check `.env` file exists
- Verify key format (GROQ: `gsk_`, OpenAI: `sk_`)
- Restart terminal
- Run `python setup.py` again

### Module Not Found
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### Connection Error
- Check internet connection
- Check API status pages
- Try again in a few minutes

---

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

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-agent`
3. Implement your agent
4. Add tests
5. Submit PR

---

## 📄 License

MIT License - See LICENSE file

---

<div align="center">

**Made with ❤️ for the AI Community**

[⭐ Star this repo](https://github.com/jishanahmed-shaikh/CrewAI-AgenticAI-Framework)

</div>
