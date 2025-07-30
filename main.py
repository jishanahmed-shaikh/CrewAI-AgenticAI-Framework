from crewai import Agent, Task, Crew

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

def get_dev_task(choice):
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

def get_doc_task(choice):
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

def main():
    print("🤖 Welcome to the AI Agent System!")
    print("\nSelect an agent:")
    print("1. Dev Agent (Python Development)")
    print("2. Doc Agent (Documentation)")
    
    try:
        agent_choice = int(input("\nEnter your choice (1 or 2): "))
        
        if agent_choice == 1:
            print("\n🐍 Dev Agent Selected!")
            print("Choose a task:")
            print("1. Function to Reverse a String in Python")
            print("2. Function to Check if the number is palindrome")
            
            task_choice = int(input("\nEnter your choice (1 or 2): "))
            
            if task_choice in [1, 2]:
                task = get_dev_task(task_choice)
                crew = Crew(
                    agents=[dev_agent],
                    tasks=[task],
                    verbose=True
                )
            else:
                print("❌ Invalid choice! Please select 1 or 2.")
                return
                
        elif agent_choice == 2:
            print("\n📝 Doc Agent Selected!")
            print("Choose a task:")
            print("1. Report on Computer")
            print("2. Report on Internet")
            
            task_choice = int(input("\nEnter your choice (1 or 2): "))
            
            if task_choice in [1, 2]:
                task = get_doc_task(task_choice)
                crew = Crew(
                    agents=[doc_agent],
                    tasks=[task],
                    verbose=True
                )
            else:
                print("❌ Invalid choice! Please select 1 or 2.")
                return
        else:
            print("❌ Invalid choice! Please select 1 or 2.")
            return
        
        # Run the selected crew
        print(f"\n🚀 Starting task execution...")
        result = crew.kickoff()
        print("\n✅ Final Output:")
        print(result)
        
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()