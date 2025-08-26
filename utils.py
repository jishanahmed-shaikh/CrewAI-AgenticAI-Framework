# Utility functions for Enhanced AI Agent System

import os
import json
from datetime import datetime
from config import PERFORMANCE_CONFIG

def save_performance_metrics(metrics):
    """Save performance metrics to file"""
    if PERFORMANCE_CONFIG['save_metrics']:
        try:
            with open(PERFORMANCE_CONFIG['metrics_file'], 'w') as f:
                json.dump(metrics, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save metrics: {e}")

def load_performance_metrics():
    """Load performance metrics from file"""
    try:
        if os.path.exists(PERFORMANCE_CONFIG['metrics_file']):
            with open(PERFORMANCE_CONFIG['metrics_file'], 'r') as f:
                return json.load(f)
    except Exception:
        pass
    return {
        'dev_agent_calls': 0,
        'doc_agent_calls': 0,
        'readme_agent_calls': 0,
        'code_review_calls': 0,
        'total_tasks_completed': 0
    }

def format_duration(duration):
    """Format duration in a human-readable way"""
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def create_backup_filename(original_filename):
    """Create a backup filename with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(original_filename)
    return f"{name}_backup_{timestamp}{ext}"

def validate_file_path(file_path):
    """Validate if a file path is safe and accessible"""
    try:
        # Check if path exists and is readable
        if os.path.exists(file_path) and os.access(file_path, os.R_OK):
            return True, "File is accessible"
        elif not os.path.exists(file_path):
            return False, "File does not exist"
        else:
            return False, "File is not readable"
    except Exception as e:
        return False, f"Error validating file: {e}"