from jira import JIRA
from dotenv import load_dotenv
import os

load_dotenv()

def extract_jira_stories(jira_url, email, api_token, project_key="PROJECT_KEY", max_results=50):
    # Authenticate with Jira
    jira = JIRA(server=jira_url, basic_auth=(email, api_token))

    # Build JQL query
    jql_query = f"project = {project_key}"
    
    # Fetch issues
    issues = jira.search_issues(jql_query, maxResults=max_results)

    stories = []
    for issue in issues:
        stories.append({
            "key": issue.key,
            "summary": issue.fields.summary,
            "description": issue.fields.description,
            "status": issue.fields.status.name
        })

    return stories









# only to check code is working or not
''' 
if __name__ == "__main__":
    jira_url = os.getenv("JIRA_URL")
    email = os.getenv("JIRA_EMAIL")
    api_token = os.getenv("JIRA_API_TOKEN")
    project_key = os.getenv("PROJECT_KEY", "PROJECT_KEY")  # Replace or set in .env

    if not all([jira_url, email, api_token]):
        raise ValueError("Missing one or more required environment variables: JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN")

    stories = extract_jira_stories(jira_url, email, api_token, project_key)

    print(f"✅ Total stories found: {len(stories)}")
    for story in stories:
        print(f"- {story['key']}: {story['summary']} (Status: {story['status']})")

'''