from crewai import Agent, Task, Crew
import os

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
    goal="Create professional, detailed, and emojified README.md files from natural language project descriptions",
    backstory="An expert technical writer and project analyst who excels at understanding project contexts from natural language descriptions and transforming them into comprehensive, professional README files. Skilled at inferring project structure, tech stack requirements, and creating engaging documentation.",
    verbose=True
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
    """Get natural language project context from user"""
    print("\n� PWelcome to the Professional README Generator!")
    print("="*60)
    print("📝 Please provide your project context in natural language.")
    print("Include: Project title, what it does, tech stack, and key features.")
    print("="*60)
    
    context = input("\n💬 Enter the context of your project: ").strip()
    
    if not context:
        print("❌ Project context cannot be empty!")
        return None
    
    return context

def create_readme_task(project_context, improvement_feedback=None):
    """Create README generation task from natural language context"""
    base_description = f"""
    Based on the following project context, create a professional, detailed, and emojified README.md file:
    
    PROJECT CONTEXT: {project_context}
    
    Analyze the context and extract:
    - Project title/name
    - What the project does (description)
    - Technologies used (tech stack)
    - Key features mentioned
    - Any other relevant information
    
    Create a comprehensive README that includes:
    - Attractive title with relevant emojis
    - Clear project description
    - Features list with emojis
    - Technology stack section
    - Installation instructions (infer from tech stack)
    - Usage examples (create realistic examples based on project type)
    - Contributing guidelines
    - License section
    - Contact information placeholder
    - Table of contents
    - Badges (create appropriate badges based on tech stack)
    
    Make it professional, engaging, and comprehensive while maintaining clarity.
    """
    
    if improvement_feedback:
        base_description += f"\n\nIMPROVEMENT REQUEST: {improvement_feedback}"
        base_description += "\nPlease address the feedback and improve the README accordingly."
    
    return Task(
        description=base_description,
        expected_output="A complete, professional README.md file content with proper markdown formatting, emojis, badges, and comprehensive sections that accurately reflects the project context.",
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

def handle_readme_generation():
    """Handle the streamlined README generation process"""
    project_context = get_project_context()
    
    if not project_context:
        return
    
    while True:
        print("\n🚀 Generating professional README...")
        print("⏳ Please wait while I analyze your project and create the README...")
        
        # Create and run the README generation task
        task = create_readme_task(project_context)
        crew = Crew(
            agents=[readme_agent],
            tasks=[task],
            verbose=False  # Less verbose for better UX
        )
        
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

def show_main_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🤖 AI Agent System - Main Menu")
    print("="*50)
    print("1. Dev Agent (Python Development)")
    print("2. Doc Agent (Documentation)")
    print("3. README Generator (Project Documentation)")
    print("4. Exit")
    print("="*50)

def handle_dev_agent():
    """Handle Dev Agent operations"""
    while True:
        print("\n🐍 Dev Agent Selected!")
        print("Choose a task:")
        print("1. Function to Reverse a String in Python")
        print("2. Function to Check if the number is palindrome")
        print("3. Enter Custom Programming Task")
        print("4. Back to Main Menu")
        
        try:
            task_choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
            
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
    """Main application loop"""
    print("🎉 Welcome to the AI Agent System!")
    
    while True:
        show_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
            
            if choice == 1:
                handle_dev_agent()
            elif choice == 2:
                handle_doc_agent()
            elif choice == 3:
                print("\n📄 README Generator Selected!")
                handle_readme_generation()
                input("\n📝 Press Enter to continue...")
            elif choice == 4:
                print("\n👋 Thank you for using AI Agent System!")
                print("🚪 Exiting...")
                break
            else:
                print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using AI Agent System!")
            print("🚪 Exiting...")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()