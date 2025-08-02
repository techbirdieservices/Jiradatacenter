import os
from dotenv import load_dotenv
from jira_extraction import extract_jira_stories

# Load environment variables
load_dotenv()

# Read environment values
jira_url = os.getenv("JIRA_URL")
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_API_TOKEN")
project_key = os.getenv("PROJECT_KEY")

# Extract stories
stories = extract_jira_stories(jira_url, email, api_token, project_key)

# Print output
for story in stories:
    print(f"{story['key']} - {story['summary']} [{story['status']}]")

