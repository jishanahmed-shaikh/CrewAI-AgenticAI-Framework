#!/usr/bin/env python3
"""
[START] CrewAI Workshop - Multi-Agent System with GROQ & OpenAI Support
Learn agentic AI with free tools and services
"""

from crewai import Agent, Task, Crew, LLM
import os
import sys
import logging
from datetime import datetime
from config import (
    AGENT_CONFIG, UI_CONFIG, FILE_CONFIG, PERFORMANCE_CONFIG,
    GROQ_CONFIG, WORKSHOP_CONFIG
)
from utils import save_performance_metrics, load_performance_metrics, format_duration

# Application Constants
APP_NAME = WORKSHOP_CONFIG['title']
VERSION = "3.0.0"
MENU_WIDTH = UI_CONFIG['menu_width']
SEPARATOR_WIDTH = UI_CONFIG['separator_width']

# Performance tracking
performance_metrics = load_performance_metrics()


def check_api_keys():
    """Check if GROQ API key is configured"""
    groq_key = GROQ_CONFIG.get('api_key')
    
    if not groq_key:
        print("\n" + "="*70)
        print("[WARNING] NO GROQ API KEY CONFIGURED")
        print("="*70)
        print("\n[INFO] You need to configure your GROQ API key:\n")
        print("[1] Get your free GROQ API key:")
        print("   • Visit: https://console.groq.com/keys")
        print("   • Sign up (no credit card needed)\n")
        print("[INFO] Add your API key to .env file:")
        print("   GROQ_API_KEY=your_key_here\n")
        print("="*70)
        return False
    
    return True


def get_llm_config():
    """Get GROQ LLM configuration using CrewAI's LLM class"""
    api_key = GROQ_CONFIG.get('api_key')
    if not api_key:
        return None
    
    return LLM(
        model=f"groq/{GROQ_CONFIG['model']}",
        api_key=api_key,
        temperature=GROQ_CONFIG['temperature'],
        max_tokens=GROQ_CONFIG['max_tokens'],
        top_p=GROQ_CONFIG['top_p'],
        stream=GROQ_CONFIG['stream']
    )


def setup_logging():
    """Setup application logging with error recovery"""
    try:
        # Fix for Windows Unicode encoding issues
        import sys
        import io
        
        # Configure StreamHandler with UTF-8 encoding for Windows
        stream_handler = logging.StreamHandler(sys.stdout)
        if sys.platform == 'win32':
            stream_handler.stream = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(FILE_CONFIG['log_file'], encoding='utf-8'),
                stream_handler
            ]
        )
        return logging.getLogger(__name__)
    except Exception as e:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler()]
        )
        logger = logging.getLogger(__name__)
        logger.warning(f"File logging failed, using console only: {e}")
        return logger


logger = setup_logging()

# Global variables for lazy initialization
groq_client = None
llm_config = None
provider_info = None
dev_agent = None
doc_agent = None
readme_agent = None
code_reviewer = None


def initialize_agents():
    """Initialize all agents lazily on first use"""
    global groq_client, llm_config, provider_info, dev_agent, doc_agent, readme_agent, code_reviewer
    
    if dev_agent is not None:
        return  # Already initialized
    
    llm_config = get_llm_config()
    
    if not llm_config:
        provider_info = "(No LLM configured)"
        print("\n[ERROR] GROQ API key not configured!")
        print("Please add GROQ_API_KEY to .env file")
        sys.exit(1)
    
    provider_info = f"(GROQ - {GROQ_CONFIG['model']})"
    
    dev_agent = Agent(
        role="Python Developer",
        goal="Write clean Python code for any problem",
        backstory="An expert Python programmer who follows best practices.",
        verbose=True,
        llm=llm_config
    )

    doc_agent = Agent(
        role="Technical Documentation Expert",
        goal="Create well-structured, comprehensive, and highly informative documentation with clear explanations, examples, and proper formatting",
        backstory="An expert technical writer with 10+ years of experience creating clear, concise documentation. You excel at breaking down complex topics into digestible sections with examples, use cases, and practical applications. You structure documentation with clear headings, bullet points, and logical flow.",
        verbose=True,
        llm=llm_config,
        max_iter=5
    )

    readme_agent = Agent(
        role="README Generator",
        goal="Create professional, detailed, and emojified README.md files from natural language project descriptions",
        backstory="An expert technical writer and project analyst who excels at understanding complex project contexts and transforming them into comprehensive, professional README files.",
        verbose=True,
        max_iter=10,
        memory=True,
        llm=llm_config
    )

    code_reviewer = Agent(
        role="Senior Code Reviewer",
        goal="Analyze code for bugs, security vulnerabilities, performance issues, and best practices",
        backstory="A seasoned software engineer with 15+ years of experience in code review, security analysis, and performance optimization.",
        verbose=True,
        max_iter=8,
        memory=True,
        llm=llm_config
    )


def get_dev_task(choice, custom_description=None):
    """Create development tasks based on user choice"""
    if choice == 1:
        return Task(
            description="Write a Python function to reverse a string.",
            expected_output="Python code that takes a string and returns it reversed.",
            agent=dev_agent
        )
    elif choice == 2:
        return Task(
            description="Write a Python function to check if a number is a palindrome.",
            expected_output="Python code that takes a number and returns True if it's a palindrome, False otherwise.",
            agent=dev_agent
        )
    elif choice == 3:
        return Task(
            description=custom_description,
            expected_output="Clean, optimized and well-commented Python code that solves the given problem with proper error handling and best practices.",
            agent=dev_agent
        )


def get_doc_task(choice, custom_description=None):
    """Create documentation tasks based on user choice"""
    if choice == 1:
        return Task(
            description="""Write a comprehensive technical report about computers. Include:
1. Definition and purpose of computers
2. Main components (CPU, RAM, Storage, GPU, Motherboard)
3. Types of computers (Desktop, Laptop, Server, Mobile)
4. How computers work (basic architecture and processing)
5. Modern applications and use cases
6. Future trends in computing

Format with clear headings, bullet points, and practical examples. Make it accessible to beginners while being informative.""",
            expected_output="A well-structured, detailed technical report with clear sections, examples, and practical applications. Should be 1000+ words with proper formatting.",
            agent=doc_agent
        )
    elif choice == 2:
        return Task(
            description="""Write a comprehensive technical report about the Internet. Include:
1. Definition and history of the Internet
2. How the Internet works (TCP/IP, DNS, routing)
3. Key technologies (HTTP, HTTPS, protocols)
4. Internet infrastructure (servers, data centers, ISPs)
5. Impact on society and business
6. Security and privacy considerations
7. Future of the Internet (Web3, 5G, etc.)

Format with clear headings, bullet points, and real-world examples. Make it accessible to beginners while being technically accurate.""",
            expected_output="A well-structured, detailed technical report with clear sections, examples, and practical applications. Should be 1000+ words with proper formatting.",
            agent=doc_agent
        )
    elif choice == 3:
        return Task(
            description=f"""{custom_description}

Please structure your response with:
- Clear headings and subheadings
- Bullet points for key information
- Practical examples where applicable
- Logical flow and organization
- Comprehensive coverage of the topic""",
            expected_output="A comprehensive, well-structured document with clear sections, examples, and practical applications. Should be detailed and informative.",
            agent=doc_agent
        )


def get_project_context():
    """Get comprehensive natural language project context from user"""
    print("\n[DOC] Welcome to the Enhanced Professional README Generator!")
    print("="*70)
    print("[NOTE] Please provide your comprehensive project context.")
    print("[TIP] TIP: The more details you provide, the better your README will be!")
    print("\n[TARGET] Include information about:")
    print("   • Project title and purpose")
    print("   • What it does and how it works")
    print("   • Technologies and tools used")
    print("   • Key features and functionalities")
    print("   • Installation requirements")
    print("="*70)
    print("[NOTE] You can enter multiple lines - press Enter twice when done.")
    print("="*70)
    
    context_lines = []
    empty_line_count = 0
    
    while True:
        try:
            line = input()
            if line.strip() == "":
                empty_line_count += 1
                if empty_line_count >= 2:
                    break
                context_lines.append("")
            else:
                empty_line_count = 0
                context_lines.append(line)
        except KeyboardInterrupt:
            print("\n[ERROR] Input cancelled by user.")
            return None
        except EOFError:
            break
    
    context = "\n".join(context_lines).strip()
    
    if not context:
        print("[ERROR] Project context cannot be empty!")
        return None
    
    word_count = len(context.split())
    print(f"\n[STATS] Context received: {word_count} words")
    
    return context


def create_readme_task(project_context, improvement_feedback=None):
    """Create README generation task from natural language context"""
    base_description = f"""
    Based on the following comprehensive project context, create a professional, detailed, and emojified README.md file:
    
    PROJECT CONTEXT: 
    {project_context}
    
    CREATE A COMPREHENSIVE README WITH:
    1. [TARGET] Attractive title with relevant emojis and tagline
    2. [STATS] Professional badges (GitHub, build status, version, license, etc.)
    3.  Clear and compelling project description
    4.  Comprehensive features list with emojis
    5.  Complete technology stack section
    6.  Detailed prerequisites and system requirements
    7. [START] Step-by-step installation instructions
    8. [TIP] Usage examples with realistic code snippets
    9. [FILE] Project structure/architecture overview
    10.  Configuration options and environment variables
    11.  Testing instructions
    12.  API documentation (if applicable)
    13.  Contributing guidelines
    14. [DOC] License information
    15.  Authors/contributors section
    16.  Support and contact information
    
    QUALITY STANDARDS:
    - Use professional markdown formatting
    - Include appropriate emojis for visual appeal
    - Ensure all code blocks have proper syntax highlighting
    - Create realistic and functional examples
    - Make it comprehensive yet readable
    - Follow modern README best practices
    """
    
    if improvement_feedback:
        base_description += f"\n\nIMPROVEMENT REQUEST: {improvement_feedback}"
        base_description += "\nPlease address the feedback and improve the README accordingly."
    
    return Task(
        description=base_description,
        expected_output="A complete, professional, and comprehensive README.md file with proper markdown formatting, emojis, and all requested improvements.",
        agent=readme_agent
    )


def get_save_location():
    """Get save location from user"""
    print("\n Where would you like to save the README.md file?")
    print("1. Current directory")
    print("2. Custom location")
    
    try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        
        if choice == 1:
            return "README.md"
        elif choice == 2:
            custom_path = input("Enter the full path: ").strip()
            
            if not custom_path:
                print("[WARN] No path provided, using current directory.")
                return "README.md"
            
            if not custom_path.endswith('.md'):
                if os.path.isdir(custom_path) or custom_path.endswith('\\') or custom_path.endswith('/'):
                    custom_path = os.path.join(custom_path, "README.md")
                else:
                    custom_path += "\\README.md"
            
            return custom_path
        else:
            print("[ERROR] Invalid choice! Using current directory.")
            return "README.md"
            
    except ValueError:
        print("[ERROR] Invalid input! Using current directory.")
        return "README.md"


def get_code_review_input():
    """Get code for review with multiple input methods"""
    print("\n[SEARCH] Welcome to the Code Review Agent!")
    print("="*60)
    print("Choose how you want to provide code for review:")
    print("1. [FILE] Review a specific file")
    print("2. [NOTE] Paste code directly")
    print("3.  Back to Main Menu")
    print("="*60)
    
    try:
        choice = int(input("\nEnter your choice (1, 2, or 3): "))
        
        if choice == 1:
            file_path = input("\n[FILE] Enter the file path to review: ").strip()
            if not file_path:
                print("[ERROR] File path cannot be empty!")
                return None, None
            
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_content = f.read()
                    return code_content, f"File: {file_path}"
                else:
                    print(f"[ERROR] File not found: {file_path}")
                    return None, None
            except Exception as e:
                print(f"[ERROR] Error reading file: {e}")
                return None, None
                
        elif choice == 2:
            print("\n[NOTE] Paste your code below (press Enter twice when done):")
            print("="*50)
            
            code_lines = []
            empty_line_count = 0
            
            while True:
                try:
                    line = input()
                    if line.strip() == "":
                        empty_line_count += 1
                        if empty_line_count >= 2:
                            break
                        code_lines.append("")
                    else:
                        empty_line_count = 0
                        code_lines.append(line)
                except (KeyboardInterrupt, EOFError):
                    break
            
            code_content = "\n".join(code_lines).strip()
            if not code_content:
                print("[ERROR] No code provided!")
                return None, None
            
            return code_content, "Direct input"
            
        elif choice == 3:
            return None, None
        else:
            print("[ERROR] Invalid choice! Please select 1, 2, or 3.")
            return None, None
            
    except ValueError:
        print("[ERROR] Invalid input! Please enter a number.")
        return None, None


def create_code_review_task(code_content, code_source):
    """Create comprehensive code review task"""
    return Task(
        description=f"""
        Perform a comprehensive code review of the following code from {code_source}:
        
        CODE TO REVIEW:
        ```
        {code_content}
        ```
        
        REVIEW REQUIREMENTS:
        
        1.  BUG DETECTION:
           - Identify potential runtime errors
           - Check for logical errors
           - Find edge cases that might cause issues
        
        2.  SECURITY ANALYSIS:
           - Check for security vulnerabilities
           - Identify potential injection attacks
           - Review input validation
        
        3.  PERFORMANCE REVIEW:
           - Identify performance bottlenecks
           - Check algorithm efficiency
           - Suggest optimization opportunities
        
        4.  CODE QUALITY:
           - Check adherence to coding standards
           - Review naming conventions
           - Assess code readability
        
        5.  ARCHITECTURE & DESIGN:
           - Review design patterns usage
           - Check SOLID principles adherence
           - Assess code structure
        
        PROVIDE ACTIONABLE RECOMMENDATIONS:
        - Specific feedback where applicable
        - Code examples for suggested improvements
        - Priority levels (Critical, High, Medium, Low)
        - Rate overall code quality (1-10)
        """,
        expected_output="A comprehensive code review report with detailed analysis, specific recommendations, and actionable improvements.",
        agent=code_reviewer
    )


def handle_code_review():
    """Handle the code review process"""
    while True:
        code_content, code_source = get_code_review_input()
        
        if code_content is None:
            if code_source is None:
                print(" Returning to Main Menu...")
                break
            else:
                continue
        
        print(f"\n[SEARCH] Analyzing code from: {code_source}")
        print("[WAIT] Please wait while I perform a comprehensive code review...")
        
        task = create_code_review_task(code_content, code_source)
        crew = Crew(
            agents=[code_reviewer],
            tasks=[task],
            verbose=False
        )
        
        try:
            result = crew.kickoff()
            
            print("\n" + "="*80)
            print("[SEARCH] CODE REVIEW REPORT")
            print("="*80)
            print(result)
            print("="*80)
            
            save_choice = input("\n Would you like to save this review to a file? (Y/N): ").strip().upper()
            
            if save_choice == 'Y':
                try:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"code_review_{timestamp}.md"
                    
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"# Code Review Report\n\n")
                        f.write(f"**Source:** {code_source}\n")
                        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                        f.write("---\n\n")
                        f.write(str(result))
                    
                    print(f"[OK] Code review saved to: {filename}")
                except Exception as e:
                    print(f"[ERROR] Error saving review: {e}")
            
            continue_choice = input("\n[RETRY] Would you like to review more code? (Y/N): ").strip().upper()
            if continue_choice != 'Y':
                break
                
        except Exception as e:
            print(f"[ERROR] Error during code review: {e}")
            print("[TIP] Please try again or check your input.")
            continue


def handle_readme_generation():
    """Handle the enhanced README generation process"""
    project_context = get_project_context()
    
    if not project_context:
        return
    
    while True:
        print("\n[START] Generating comprehensive professional README...")
        print("[WAIT] Please wait while I analyze your project context...")
        
        task = create_readme_task(project_context)
        crew = Crew(
            agents=[readme_agent],
            tasks=[task],
            verbose=False
        )
        
        try:
            result = crew.kickoff()
            
            print("\n" + "="*80)
            print("[DOC] GENERATED README.md")
            print("="*80)
            print(result)
            print("="*80)
            
            print("\n Are you satisfied with this README?")
            satisfaction = input("Type 'Y' if satisfied, or provide feedback for improvements: ").strip()
            
            if satisfaction.upper() == 'Y':
                save_location = get_save_location()
                
                try:
                    save_dir = os.path.dirname(save_location)
                    if save_dir and not os.path.exists(save_dir):
                        os.makedirs(save_dir, exist_ok=True)
                    
                    with open(save_location, 'w', encoding='utf-8') as f:
                        f.write(str(result))
                    print(f"[OK] README.md saved successfully at: {os.path.abspath(save_location)}")
                    break
                except Exception as e:
                    print(f"[ERROR] Error saving file: {e}")
                    print("[TIP] Please check the path and try again.")
                    continue
                    
            elif satisfaction:
                print(f"\n[RETRY] Regenerating README with your feedback...")
                project_context += f"\n\nADDITIONAL REQUIREMENTS: {satisfaction}"
                continue
            else:
                print("[ERROR] Please provide feedback or type 'Y' if satisfied.")
                continue
                
        except Exception as e:
            print(f"[ERROR] Error during README generation: {e}")
            print("[TIP] Please try again or check your input.")
            continue


def show_help():
    """Display help information"""
    print("\n" + "="*MENU_WIDTH)
    print(" HELP & USAGE TIPS")
    print("="*MENU_WIDTH)
    print("[PYTHON] Dev Agent: Generate Python functions and custom code")
    print("[NOTE] Doc Agent: Create comprehensive documentation")
    print("[DOC] README Generator: Professional project documentation")
    print("[SEARCH] Code Review: Analyze code for bugs, security, performance")
    print("\n[TIP] Tips:")
    print("• Use Dev Agent → Code Review for best workflow")
    print("• README Generator supports multi-line input")
    print("• Code Review can analyze files or pasted code")
    print("• All outputs can be saved to files")
    print("="*MENU_WIDTH)


def show_main_menu():
    """Display the main menu"""
    print("\n" + "="*MENU_WIDTH)
    print(f"[AGENT] {APP_NAME} v{VERSION}")
    print(f"[PROVIDER] Provider: {provider_info}")
    print("="*MENU_WIDTH)
    print("1. [PYTHON] Dev Agent (Python Development)")
    print("2. [NOTE] Doc Agent (Documentation)")
    print("3. [DOC] README Generator (Project Documentation)")
    print("4. [SEARCH] Code Review Agent (Code Analysis)")
    print("5.  Help & Tips")
    print("6. [EXIT] Exit")
    print("="*MENU_WIDTH)


def handle_dev_agent():
    """Handle Dev Agent operations"""
    while True:
        print("\n[PYTHON] Dev Agent Selected!")
        print("Choose a task:")
        print("1. Function to Reverse a String in Python")
        print("2. Function to Check if the number is palindrome")
        print("3. Enter Custom Programming Task")
        print("4. Back to Main Menu")
        
        try:
            task_choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
            
            if task_choice == 4:
                print(" Returning to Main Menu...")
                break
            elif task_choice in [1, 2]:
                task = get_dev_task(task_choice)
                crew = Crew(
                    agents=[dev_agent],
                    tasks=[task],
                    verbose=True
                )
                
                print(f"\n[START] Starting task execution...")
                result = crew.kickoff()
                print("\n[OK] Final Output:")
                print(result)
                
                input("\n[NOTE] Press Enter to continue...")
                
            elif task_choice == 3:
                print("\n Custom Task Selected!")
                custom_task = input("Enter your custom task in natural language: ")
                if custom_task.strip():
                    task = get_dev_task(3, custom_task)
                    crew = Crew(
                        agents=[dev_agent],
                        tasks=[task],
                        verbose=True
                    )
                    
                    print(f"\n[START] Starting task execution...")
                    result = crew.kickoff()
                    print("\n[OK] Final Output:")
                    print(result)
                    
                    input("\n[NOTE] Press Enter to continue...")
                else:
                    print("[ERROR] Task description cannot be empty!")
            else:
                print("[ERROR] Invalid choice! Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("[ERROR] Invalid input! Please enter a number.")
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")


def handle_doc_agent():
    """Handle Doc Agent operations"""
    while True:
        print("\n[NOTE] Doc Agent Selected!")
        print("Choose a task:")
        print("1. Report on Computer")
        print("2. Report on Internet")
        print("3. Enter Custom Documentation Task")
        print("4. Back to Main Menu")
        
        try:
            task_choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
            
            if task_choice == 4:
                print(" Returning to Main Menu...")
                break
            elif task_choice in [1, 2]:
                task = get_doc_task(task_choice)
                crew = Crew(
                    agents=[doc_agent],
                    tasks=[task],
                    verbose=True
                )
                
                print(f"\n[START] Starting task execution...")
                result = crew.kickoff()
                print("\n[OK] Final Output:")
                print(result)
                
                input("\n[NOTE] Press Enter to continue...")
                
            elif task_choice == 3:
                print("\n Custom Documentation Task Selected!")
                custom_task = input("Enter your custom documentation task in natural language: ")
                if custom_task.strip():
                    task = get_doc_task(3, custom_task)
                    crew = Crew(
                        agents=[doc_agent],
                        tasks=[task],
                        verbose=True
                    )
                    
                    print(f"\n[START] Starting task execution...")
                    result = crew.kickoff()
                    print("\n[OK] Final Output:")
                    print(result)
                    
                    input("\n[NOTE] Press Enter to continue...")
                else:
                    print("[ERROR] Task description cannot be empty!")
            else:
                print("[ERROR] Invalid choice! Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("[ERROR] Invalid input! Please enter a number.")
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")


def main():
    """Main application loop"""
    session_start = datetime.now()
    logger.info(f"Starting {APP_NAME} v{VERSION}")
    
    # Initialize agents on first use
    initialize_agents()
    
    # Check API keys
    if not check_api_keys():
        print("\n[ERROR] Setup incomplete. Please run: python setup.py")
        return
    
    print("\n[INFO] Welcome to the CrewAI Workshop!")
    print("[INFO] Learn agentic AI with free tools and services")
    print(f"[INFO] Session started: {session_start.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        show_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1, 2, 3, 4, 5, or 6): "))
            
            if choice == 1:
                performance_metrics['dev_agent_calls'] += 1
                handle_dev_agent()
                
            elif choice == 2:
                performance_metrics['doc_agent_calls'] += 1
                handle_doc_agent()
                
            elif choice == 3:
                performance_metrics['readme_agent_calls'] += 1
                print("\n[INFO] Enhanced README Generator Selected!")
                handle_readme_generation()
                input("\n[INFO] Press Enter to continue...")
                
            elif choice == 4:
                performance_metrics['code_review_calls'] += 1
                print("\n[INFO] Code Review Agent Selected!")
                handle_code_review()
                input("\n[INFO] Press Enter to continue...")
                
            elif choice == 5:
                show_help()
                input("\n[INFO] Press Enter to continue...")
                
            elif choice == 6:
                session_end = datetime.now()
                session_duration = session_end - session_start
                formatted_duration = format_duration(session_duration)
                
                save_performance_metrics(performance_metrics)
                
                logger.info(f"Session ended. Duration: {session_duration}")
                print(f"\n[INFO] Session duration: {formatted_duration}")
                print("[INFO] Thank you for learning with CrewAI Workshop!")
                print("[INFO] Exiting...")
                break
            else:
                print("[ERROR] Invalid choice! Please select 1, 2, 3, 4, 5, or 6.")
                
        except ValueError:
            print("[ERROR] Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n[BYE] Thank you for learning with CrewAI Workshop!")
            print("[EXIT] Exiting...")
            break
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
            print(f"[ERROR] An error occurred: {e}")
            print("[TIP] The system will continue running. Please try again.")


if __name__ == "__main__":
    main()
