import ollama

def generate_readme(project_name, description, features, style):
    prompt = f"""
    Generate a well-structured GitHub project README.md with:

    - **Project Name**: {project_name}
    - **Description**: {description}
    - **Features**: {features}
    - **Installation**: AI-generated best practices based on project type
    - **Overall Style**: {style} (e.g., professional, exciting, fun, mysterious, minimalistic)

    The README should:
    - Have a clear title
    - Include an engaging description
    - List features in bullet points
    - Auto-generate installation steps based on the project
    - Follow the requested style (Markdown formatting, emojis, or minimal design)
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

def main():
    print("🚀 Welcome to the AI-Powered Project README Generator!\n")

    project_name = input("Enter your project name: ")
    description = input("Enter a short project description: ")
    features = input("List the key features (comma-separated): ")
    style = input("How do you want the README to look? (e.g., exciting, minimalistic, fun): ")

    print("\n⏳ Please wait, we are getting your README ready...\n")

    readme_content = generate_readme(project_name, description, features, style)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("\n✅ README.md has been generated successfully!")

if __name__ == "__main__":
    main()




