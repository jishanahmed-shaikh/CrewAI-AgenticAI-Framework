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
    goal="Create professional, detailed, and emojified README.md files for projects",
    backstory="An expert technical writer specializing in creating engaging and comprehensive README files that help users understand and use projects effectively.",
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
            expected_output="Clean, well-commented Python code that solves the given problem with proper error handling and best practices.",
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

def get_project_details():
    """Collect project details from user"""
    print("\n📋 Please provide the following project details:")
    
    project_name = input("Project Name: ").strip()
    project_description = input("Project Description: ").strip()
    project_type = input("Project Type (e.g., Web App, CLI Tool, Library, etc.): ").strip()
    tech_stack = input("Technologies Used (e.g., Python, React, Node.js): ").strip()
    features = input("Key Features (comma-separated): ").strip()
    installation_notes = input("Installation Notes (optional): ").strip()
    usage_notes = input("Usage Notes (optional): ").strip()
    
    return {
        "name": project_name,
        "description": project_description,
        "type": project_type,
        "tech_stack": tech_stack,
        "features": features,
        "installation": installation_notes,
        "usage": usage_notes
    }

def create_readme_task(project_details, improvement_feedback=None):
    """Create README generation task"""
    base_description = f"""
    Create a professional, detailed, and emojified README.md file for a project with the following details:
    
    Project Name: {project_details['name']}
    Description: {project_details['description']}
    Type: {project_details['type']}
    Technologies: {project_details['tech_stack']}
    Features: {project_details['features']}
    Installation Notes: {project_details['installation']}
    Usage Notes: {project_details['usage']}
    
    The README should include:
    - Attractive title with emojis
    - Project description
    - Features list with emojis
    - Installation instructions
    - Usage examples
    - Technology stack
    - Contributing guidelines
    - License section
    - Contact information placeholder
    """
    
    if improvement_feedback:
        base_description += f"\n\nIMPROVEMENT REQUEST: {improvement_feedback}"
        base_description += "\nPlease address the feedback and improve the README accordingly."
    
    return Task(
        description=base_description,
        expected_output="A complete, professional README.md file content with proper markdown formatting, emojis, and comprehensive sections.",
        agent=readme_agent
    )

def handle_readme_generation():
    """Handle the interactive README generation process"""
    project_details = get_project_details()
    
    if not project_details['name'] or not project_details['description']:
        print("❌ Project name and description are required!")
        return
    
    while True:
        print("\n🚀 Generating README...")
        
        # Create and run the README generation task
        task = create_readme_task(project_details)
        crew = Crew(
            agents=[readme_agent],
            tasks=[task],
            verbose=True
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
        print("1. Yes - Save the file")
        print("2. No - Improve it")
        print("3. Exit")
        
        try:
            satisfaction = int(input("\nEnter your choice (1, 2, or 3): "))
            
            if satisfaction == 1:
                # User is satisfied, ask for save location
                save_location = input("\nEnter the path where you want to save README.md (or press Enter for current directory): ").strip()
                
                if not save_location:
                    save_location = "README.md"
                elif not save_location.endswith('.md'):
                    save_location = os.path.join(save_location, "README.md")
                
                try:
                    with open(save_location, 'w', encoding='utf-8') as f:
                        f.write(str(result))
                    print(f"✅ README.md saved successfully at: {save_location}")
                    break
                except Exception as e:
                    print(f"❌ Error saving file: {e}")
                    break
                    
            elif satisfaction == 2:
                # User wants improvements
                feedback = input("\n💭 What would you like to improve in the README? ").strip()
                if feedback:
                    project_details['improvement_feedback'] = feedback
                    print("\n🔄 Regenerating README with your feedback...")
                    continue
                else:
                    print("❌ Please provide specific feedback for improvement.")
                    continue
                    
            elif satisfaction == 3:
                # User wants to exit
                print("👋 Exiting README generator.")
                break
                
            else:
                print("❌ Invalid choice! Please select 1, 2, or 3.")
                continue
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
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