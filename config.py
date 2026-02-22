# Configuration settings for CrewAI Workshop - GROQ Only

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# 🔑 GROQ Configuration (FREE - Recommended for workshops)
# ============================================================================

GROQ_CONFIG = {
    'api_key': os.getenv('GROQ_API_KEY', '').strip().strip("'\""),
    'model': os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant'),
    'temperature': float(os.getenv('GROQ_TEMPERATURE', 1)),
    'max_tokens': int(os.getenv('GROQ_MAX_TOKENS', 1024)),
    'top_p': float(os.getenv('GROQ_TOP_P', 1)),
    'stream': os.getenv('GROQ_STREAM', 'true').lower() == 'true',
    'stop': None,
}

# ============================================================================
# 🤖 Agent Configuration
# ============================================================================

AGENT_CONFIG = {
    'verbose': True,
    'max_iterations': 10,
    'memory_enabled': True,
    'temperature': 0.7
}

# ============================================================================
# 🎨 UI Configuration
# ============================================================================

UI_CONFIG = {
    'menu_width': 60,
    'separator_width': 80,
    'show_timestamps': True,
    'colored_output': True
}

# ============================================================================
# 📁 File Configuration
# ============================================================================

FILE_CONFIG = {
    'default_save_location': '.',
    'auto_backup': True,
    'log_file': 'agent_system.log',
    'max_log_size': 10485760  # 10MB
}

# ============================================================================
# 📊 Performance Configuration
# ============================================================================

PERFORMANCE_CONFIG = {
    'enable_metrics': True,
    'save_metrics': True,
    'metrics_file': 'performance_metrics.json'
}

# ============================================================================
# 🎓 Workshop Configuration
# ============================================================================

WORKSHOP_CONFIG = {
    'title': 'CrewAI Workshop - Agentic AI Learning',
    'description': 'Learn multi-agent systems with free tools',
    'free_tier_enabled': True,
    'show_provider_info': True,
}