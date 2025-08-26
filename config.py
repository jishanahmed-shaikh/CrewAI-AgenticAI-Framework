# Configuration settings for Enhanced AI Agent System

# Agent Configuration
AGENT_CONFIG = {
    'verbose': True,
    'max_iterations': 10,
    'memory_enabled': True,
    'temperature': 0.7
}

# UI Configuration
UI_CONFIG = {
    'menu_width': 60,
    'separator_width': 80,
    'show_timestamps': True,
    'colored_output': True
}

# File Configuration
FILE_CONFIG = {
    'default_save_location': '.',
    'auto_backup': True,
    'log_file': 'agent_system.log',
    'max_log_size': 10485760  # 10MB
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    'enable_metrics': True,
    'save_metrics': True,
    'metrics_file': 'performance_metrics.json'
}