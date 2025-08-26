from crewai import Agent, Task, Crew
import os
import logging
from datetime import datetime

# Application Constants
APP_NAME = "Enhanced AI Agent System"
VERSION = "2.0.0"
MENU_WIDTH = 60
SEPARATOR_WIDTH = 80

# Performance tracking
performance_metrics = {
    'dev_agent_calls': 0,
    'doc_agent_calls': 0,
    'readme_agent_calls': 0,
    'code_review_calls': 0,
    'total_tasks_completed': 0
}

# Setup logging
def setup_logging():
    """Setup application logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('agent_system.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# Create Agents
dev_agent = Agent(
    role="Python Developer",
    goal="Write clean Python code for any problem",
    backstory="An expert Python programmer who follows best practices.",
    verbose=True
)

doc_agent = Agent(
    role="Documentation Writer",
    goal="Create comprehensive and informative documentation on various topics",
    backstory="A skilled technical writer who can explain complex topics in simple terms.",
    verbose=True
)

readme_agent = Agent(
    role="README Generator",
    goal="Create professional, detailed, and emojified README.md files from natural language project descriptions with extensive context understanding",
    backstory="An expert technical writer and project analyst who excels at understanding complex project contexts from natural language descriptions and transforming them into comprehensive, professional README files. Skilled at inferring project structure, tech stack requirements, and creating engaging documentation. Can handle large project descriptions and multiple requirements with high attention to detail.",
    verbose=True,
    max_iter=10,  # Increased iterations for complex projects
    memory=True   # Enable memory for better context retention
)

code_reviewer = Agent(
    role="Senior Code Reviewer",
    goal="Analyze code for bugs, security vulnerabilities, performance issues, best practices, and provide actionable improvement suggestions",
    backstory="A seasoned software engineer with 15+ years of experience in code review, security analysis, and performance optimization. Expert in multiple programming languages with deep knowledge of design patterns, SOLID principles, and industry best practices. Specializes in identifying potential issues before they reach production.",
    verbose=True,
    max_iter=8,
    memory=True
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
            expected_output="Clean, Optimized and well-commented Python code that solves the given problem with proper error handling and best practices.",
            agent=dev_agent
        )

def get_doc_task(choice, custom_description=None):
    """Create documentation tasks based on user choice"""
    if choice == 1:
        return Task(
            description="Write a comprehensive report about computers, covering their history, components, and modern applications.",
            expected_output="A detailed text document explaining computers in an informative and accessible way.",
            agent=doc_agent
        )
    elif choice == 2:
        return Task(
            description="Write a comprehensive report about the internet, covering its history, how it works, and its impact on society.",
            expected_output="A detailed text document explaining the internet in an informative and accessible way.",
            agent=doc_agent
        )
    elif choice == 3:
        return Task(
            description=custom_description,
            expected_output="A comprehensive, well-structured document that thoroughly explains the requested topic in clear, informative language suitable for the target audience.",
            agent=doc_agent
        )

def get_project_context():
    """Get comprehensive natural language project context from user with enhanced input handling"""
    print("\n📄 Welcome to the Enhanced Professional README Generator!")
    print("="*70)
    print("📝 Please provide your comprehensive project context.")
    print("💡 TIP: The more details you provide, the better your README will be!")
    print("\n🎯 Include information about:")
    print("   • Project title and purpose")
    print("   • What it does and how it works")
    print("   • Technologies, frameworks, and tools used")
    print("   • Key features and functionalities")
    print("   • Target audience and use cases")
    print("   • Installation requirements")
    print("   • Any special configurations or setup")
    print("="*70)
    print("📝 You can enter multiple lines - press Enter twice when done.")
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
            print("\n❌ Input cancelled by user.")
            return None
        except EOFError:
            break
    
    context = "\n".join(context_lines).strip()
    
    if not context:
        print("❌ Project context cannot be empty!")
        return None
    
    # Show context length for user feedback
    word_count = len(context.split())
    char_count = len(context)
    print(f"\n📊 Context received: {word_count} words, {char_count} characters")
    
    return context

def create_readme_task(project_context, improvement_feedback=None):
    """Create README generation task from natural language context with enhanced context handling"""
    base_description = f"""
    Based on the following comprehensive project context, create a professional, detailed, and emojified README.md file:
    
    PROJECT CONTEXT (FULL ANALYSIS REQUIRED): 
    {project_context}
    
    COMPREHENSIVE ANALYSIS REQUIREMENTS:
    - Thoroughly analyze ALL provided context information
    - Extract project title/name and variations
    - Understand the complete project scope and purpose
    - Identify ALL technologies, frameworks, and tools mentioned
    - Capture ALL features, functionalities, and capabilities
    - Note any specific requirements, constraints, or preferences
    - Understand target audience and use cases
    - Identify any architectural patterns or design decisions
    
    CREATE A COMPREHENSIVE README WITH:
    1. 🎯 Attractive title with relevant emojis and tagline
    2. 📊 Professional badges (GitHub, build status, version, license, etc.)
    3. 📖 Clear and compelling project description
    4. ✨ Comprehensive features list with emojis and detailed explanations
    5. 🛠️ Complete technology stack section with versions where applicable
    6. 📋 Detailed prerequisites and system requirements
    7. 🚀 Step-by-step installation instructions with code blocks
    8. 💡 Usage examples with realistic code snippets and scenarios
    9. 📁 Project structure/architecture overview
    10. 🔧 Configuration options and environment variables
    11. 🧪 Testing instructions and examples
    12. 📚 API documentation (if applicable)
    13. 🤝 Contributing guidelines with development setup
    14. 📄 License information
    15. 👥 Authors/contributors section
    16. 🙏 Acknowledgments
    17. 📞 Support and contact information
    18. 🗺️ Roadmap or future plans (if mentioned)
    19. 📋 Table of contents for easy navigation
    20. 🔗 Relevant links and resources
    
    QUALITY STANDARDS:
    - Use professional markdown formatting
    - Include appropriate emojis for visual appeal
    - Ensure all code blocks have proper syntax highlighting
    - Create realistic and functional examples
    - Make it comprehensive yet readable
    - Follow modern README best practices
    - Ensure accessibility and mobile-friendly formatting
    
    CONTEXT PROCESSING:
    - Handle large amounts of context information efficiently
    - Prioritize the most important information
    - Create logical flow and organization
    - Ensure no critical information is missed
    """
    
    if improvement_feedback:
        base_description += f"\n\nIMPROVEMENT REQUEST: {improvement_feedback}"
        base_description += "\nPlease address the feedback and improve the README accordingly while maintaining all quality standards."
    
    return Task(
        description=base_description,
        expected_output="A complete, professional, and comprehensive README.md file with proper markdown formatting, emojis, badges, detailed sections, and all requested improvements that accurately reflects the full project context.",
        agent=readme_agent
    )

def get_save_location():
    """Get save location from user with browse-like experience"""
    print("\n💾 Where would you like to save the README.md file?")
    print("1. Current directory")
    print("2. Browse to another location")
    
    try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        
        if choice == 1:
            return "README.md"
        elif choice == 2:
            print("\n📁 Browse for save location:")
            print("💡 Tip: Enter the full path where you want to save (e.g., C:\\Projects\\MyApp\\README.md)")
            custom_path = input("Enter the full path: ").strip()
            
            if not custom_path:
                print("⚠️ No path provided, using current directory.")
                return "README.md"
            
            # Ensure it ends with .md
            if not custom_path.endswith('.md'):
                if os.path.isdir(custom_path) or custom_path.endswith('\\') or custom_path.endswith('/'):
                    custom_path = os.path.join(custom_path, "README.md")
                else:
                    custom_path += "\\README.md"
            
            return custom_path
        else:
            print("❌ Invalid choice! Using current directory.")
            return "README.md"
            
    except ValueError:
        print("❌ Invalid input! Using current directory.")
        return "README.md"

def get_code_review_input():
    """Get code for review with multiple input methods and fallback mechanisms"""
    print("\n🔍 Welcome to the Code Review Agent!")
    print("="*60)
    print("Choose how you want to provide code for review:")
    print("1. 📁 Review a specific file")
    print("2. 📝 Paste code directly")
    print("3. 🔄 Review code generated by Dev Agent")
    print("4. 🏠 Back to Main Menu")
    print("="*60)
    
    try:
        choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
        
        if choice == 1:
            # File path input with fallback
            file_path = input("\n📁 Enter the file path to review: ").strip()
            if not file_path:
                print("❌ File path cannot be empty!")
                return None, None
            
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_content = f.read()
                    return code_content, f"File: {file_path}"
                else:
                    print(f"❌ File not found: {file_path}")
                    print("💡 Please check the file path and try again.")
                    return None, None
            except Exception as e:
                print(f"❌ Error reading file: {e}")
                return None, None
                
        elif choice == 2:
            # Direct code input
            print("\n📝 Paste your code below (press Enter twice when done):")
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
                print("❌ No code provided!")
                return None, None
            
            return code_content, "Direct input"
            
        elif choice == 3:
            # Review last generated code (fallback mechanism)
            print("\n🔄 This feature will review the last code generated by Dev Agent.")
            print("💡 Make sure you've generated code using Dev Agent first.")
            
            # For now, we'll ask user to paste the generated code
            print("\n📝 Please paste the code generated by Dev Agent:")
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
                print("❌ No code provided!")
                return None, None
            
            return code_content, "Dev Agent generated code"
            
        elif choice == 4:
            return None, None
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
            return None, None
            
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
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
        
        1. 🐛 BUG DETECTION:
           - Identify potential runtime errors
           - Check for logical errors
           - Find edge cases that might cause issues
           - Detect null pointer/undefined variable risks
        
        2. 🔒 SECURITY ANALYSIS:
           - Check for security vulnerabilities
           - Identify potential injection attacks
           - Review input validation
           - Check for sensitive data exposure
        
        3. ⚡ PERFORMANCE REVIEW:
           - Identify performance bottlenecks
           - Check algorithm efficiency
           - Review memory usage patterns
           - Suggest optimization opportunities
        
        4. 📏 CODE QUALITY:
           - Check adherence to coding standards
           - Review naming conventions
           - Assess code readability
           - Check for code duplication
        
        5. 🏗️ ARCHITECTURE & DESIGN:
           - Review design patterns usage
           - Check SOLID principles adherence
           - Assess code structure and organization
           - Review error handling patterns
        
        6. 🧪 TESTABILITY:
           - Assess how testable the code is
           - Suggest areas that need unit tests
           - Review dependency injection opportunities
        
        7. 📚 DOCUMENTATION:
           - Check for adequate comments
           - Review docstring quality
           - Suggest documentation improvements
        
        PROVIDE ACTIONABLE RECOMMENDATIONS:
        - Specific line-by-line feedback where applicable
        - Code examples for suggested improvements
        - Priority levels (Critical, High, Medium, Low)
        - Explanation of why each issue matters
        - Alternative approaches where relevant
        
        FORMAT YOUR REVIEW:
        - Use clear headings and bullet points
        - Include code snippets for examples
        - Provide before/after comparisons
        - Rate overall code quality (1-10)
        - Give a summary of key findings
        """,
        expected_output="A comprehensive code review report with detailed analysis, specific recommendations, code examples, and actionable improvements categorized by importance and type.",
        agent=code_reviewer
    )

def handle_code_review():
    """Handle the code review process with fallback mechanisms"""
    while True:
        code_content, code_source = get_code_review_input()
        
        if code_content is None:
            if code_source is None:  # User chose to go back
                print("🔙 Returning to Main Menu...")
                break
            else:  # Error occurred, try again
                continue
        
        print(f"\n🔍 Analyzing code from: {code_source}")
        print("⏳ Please wait while I perform a comprehensive code review...")
        
        # Create and run the code review task
        task = create_code_review_task(code_content, code_source)
        crew = Crew(
            agents=[code_reviewer],
            tasks=[task],
            verbose=False  # Less verbose for better UX
        )
        
        try:
            result = crew.kickoff()
            
            # Display the review results
            print("\n" + "="*80)
            print("🔍 CODE REVIEW REPORT")
            print("="*80)
            print(result)
            print("="*80)
            
            # Ask if user wants to save the review
            save_choice = input("\n💾 Would you like to save this review to a file? (Y/N): ").strip().upper()
            
            if save_choice == 'Y':
                try:
                    timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"code_review_{timestamp}.md"
                    
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"# Code Review Report\n\n")
                        f.write(f"**Source:** {code_source}\n")
                        f.write(f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                        f.write("---\n\n")
                        f.write(str(result))
                    
                    print(f"✅ Code review saved to: {filename}")
                except Exception as e:
                    print(f"❌ Error saving review: {e}")
            
            # Ask if user wants to review more code
            continue_choice = input("\n🔄 Would you like to review more code? (Y/N): ").strip().upper()
            if continue_choice != 'Y':
                break
                
        except Exception as e:
            print(f"❌ Error during code review: {e}")
            print("💡 Please try again or check your input.")
            continue

def handle_readme_generation():
    """Handle the enhanced README generation process"""
    project_context = get_project_context()
    
    if not project_context:
        return
    
    while True:
        print("\n🚀 Generating comprehensive professional README...")
        print("⏳ Please wait while I analyze your project context and create the README...")
        
        # Create and run the README generation task
        task = create_readme_task(project_context)
        crew = Crew(
            agents=[readme_agent],
            tasks=[task],
            verbose=False  # Less verbose for better UX
        )
        
        try:
            result = crew.kickoff()
            
            # Display the generated README
            print("\n" + "="*80)
            print("📄 GENERATED README.md")
            print("="*80)
            print(result)
            print("="*80)
            
            # Ask for user satisfaction
            print("\n🤔 Are you satisfied with this README?")
            satisfaction = input("Type 'Y' if satisfied, or provide feedback for improvements: ").strip()
            
            if satisfaction.upper() == 'Y':
                # User is satisfied, get save location
                save_location = get_save_location()
                
                try:
                    # Create directory if it doesn't exist
                    save_dir = os.path.dirname(save_location)
                    if save_dir and not os.path.exists(save_dir):
                        os.makedirs(save_dir, exist_ok=True)
                    
                    with open(save_location, 'w', encoding='utf-8') as f:
                        f.write(str(result))
                    print(f"✅ README.md saved successfully at: {os.path.abspath(save_location)}")
                    break
                except Exception as e:
                    print(f"❌ Error saving file: {e}")
                    print("💡 Please check the path and try again.")
                    continue
                    
            elif satisfaction:
                # User provided feedback
                print(f"\n🔄 Regenerating README with your feedback: '{satisfaction}'")
                project_context += f"\n\nADDITIONAL REQUIREMENTS: {satisfaction}"
                continue
            else:
                # Empty input, ask again
                print("❌ Please provide feedback or type 'Y' if satisfied.")
                continue
                
        except Exception as e:
            print(f"❌ Error during README generation: {e}")
            print("💡 Please try again or check your input.")
            continue

def show_help():
    """Display help information and usage tips"""
    print("\n" + "="*MENU_WIDTH)
    print("❓ HELP & USAGE TIPS")
    print("="*MENU_WIDTH)
    print("🐍 Dev Agent: Generate Python functions and custom code")
    print("📝 Doc Agent: Create comprehensive documentation")
    print("📄 README Generator: Professional project documentation")
    print("🔍 Code Review: Analyze code for bugs, security, performance")
    print("\n💡 Tips:")
    print("• Use Dev Agent → Code Review for best workflow")
    print("• README Generator supports multi-line input")
    print("• Code Review can analyze files or pasted code")
    print("• All outputs can be saved to files")
    print("="*MENU_WIDTH)

def show_main_menu():
    """Display the enhanced main menu"""
    print("\n" + "="*MENU_WIDTH)
    print(f"🤖 {APP_NAME} v{VERSION} - Main Menu")
    print("="*MENU_WIDTH)
    print("1. 🐍 Dev Agent (Python Development)")
    print("2. 📝 Doc Agent (Documentation)")
    print("3. 📄 README Generator (Enhanced Project Documentation)")
    print("4. 🔍 Code Review Agent (Code Analysis & Review)")
    print("5. ❓ Help & Tips")
    print("6. 🚪 Exit")
    print("="*MENU_WIDTH)

def handle_dev_agent():
    """Handle Dev Agent operations with enhanced input validation"""
    while True:
        print("\n🐍 Dev Agent Selected!")
        print("Choose a task:")
        print("1. Function to Reverse a String in Python")
        print("2. Function to Check if the number is palindrome")
        print("3. Enter Custom Programming Task")
        print("4. Back to Main Menu")
        
        try:
            user_input = input("\nEnter your choice (1, 2, 3, or 4): ").strip()
            if not user_input:
                print("❌ Please enter a valid choice!")
                continue
            task_choice = int(user_input)
            
            if task_choice == 4:
                print("🔙 Returning to Main Menu...")
                break
            elif task_choice in [1, 2]:
                task = get_dev_task(task_choice)
                crew = Crew(
                    agents=[dev_agent],
                    tasks=[task],
                    verbose=True
                )
                
                print(f"\n🚀 Starting task execution...")
                result = crew.kickoff()
                print("\n✅ Final Output:")
                print(result)
                
                input("\n📝 Press Enter to continue...")
                
            elif task_choice == 3:
                print("\n✏️ Custom Task Selected!")
                custom_task = input("Enter your custom task in natural language: ")
                if custom_task.strip():
                    task = get_dev_task(3, custom_task)
                    crew = Crew(
                        agents=[dev_agent],
                        tasks=[task],
                        verbose=True
                    )
                    
                    print(f"\n🚀 Starting task execution...")
                    result = crew.kickoff()
                    print("\n✅ Final Output:")
                    print(result)
                    
                    input("\n📝 Press Enter to continue...")
                else:
                    print("❌ Task description cannot be empty!")
            else:
                print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def handle_doc_agent():
    """Handle Doc Agent operations"""
    while True:
        print("\n📝 Doc Agent Selected!")
        print("Choose a task:")
        print("1. Report on Computer")
        print("2. Report on Internet")
        print("3. Enter Custom Documentation Task")
        print("4. Back to Main Menu")
        
        try:
            task_choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
            
            if task_choice == 4:
                print("🔙 Returning to Main Menu...")
                break
            elif task_choice in [1, 2]:
                task = get_doc_task(task_choice)
                crew = Crew(
                    agents=[doc_agent],
                    tasks=[task],
                    verbose=True
                )
                
                print(f"\n🚀 Starting task execution...")
                result = crew.kickoff()
                print("\n✅ Final Output:")
                print(result)
                
                input("\n📝 Press Enter to continue...")
                
            elif task_choice == 3:
                print("\n✏️ Custom Documentation Task Selected!")
                custom_task = input("Enter your custom documentation task in natural language: ")
                if custom_task.strip():
                    task = get_doc_task(3, custom_task)
                    crew = Crew(
                        agents=[doc_agent],
                        tasks=[task],
                        verbose=True
                    )
                    
                    print(f"\n🚀 Starting task execution...")
                    result = crew.kickoff()
                    print("\n✅ Final Output:")
                    print(result)
                    
                    input("\n📝 Press Enter to continue...")
                else:
                    print("❌ Task description cannot be empty!")
            else:
                print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def main():
    """Enhanced main application loop with code review integration"""
    session_start = datetime.now()
    logger.info(f"Starting {APP_NAME} v{VERSION}")
    
    print("🎉 Welcome to the Enhanced AI Agent System!")
    print("💡 Now featuring advanced README generation and comprehensive code review!")
    print(f"📅 Session started: {session_start.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        show_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1, 2, 3, 4, 5, or 6): "))
            
            if choice == 1:
                performance_metrics['dev_agent_calls'] += 1
                handle_dev_agent()
                
                # Offer code review after dev agent completes
                print("\n⚙️ Would you like to review the generated code?")
                review_choice = input("Type 'Y' to review with Code Review Agent, or any key to continue: ").strip().upper()
                if review_choice == 'Y':
                    print("\n🔄 Switching to Code Review Agent...")
                    print("💡 Please paste the code generated above when prompted.")
                    handle_code_review()
                    
            elif choice == 2:
                performance_metrics['doc_agent_calls'] += 1
                handle_doc_agent()
            elif choice == 3:
                performance_metrics['readme_agent_calls'] += 1
                print("\n📄 Enhanced README Generator Selected!")
                handle_readme_generation()
                input("\n📝 Press Enter to continue...")
            elif choice == 4:
                performance_metrics['code_review_calls'] += 1
                print("\n🔍 Code Review Agent Selected!")
                handle_code_review()
                input("\n📝 Press Enter to continue...")
            elif choice == 5:
                show_help()
                input("\n📝 Press Enter to continue...")
            elif choice == 6:
                session_end = datetime.now()
                session_duration = session_end - session_start
                logger.info(f"Session ended. Duration: {session_duration}")
                print(f"\n⏱️ Session duration: {session_duration}")
                print("👋 Thank you for using Enhanced AI Agent System!")
                print("🚪 Exiting...")
                break
            else:
                print("❌ Invalid choice! Please select 1, 2, 3, 4, 5, or 6.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using Enhanced AI Agent System!")
            print("🚪 Exiting...")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("💡 The system will continue running. Please try again.")

if __name__ == "__main__":
    main()