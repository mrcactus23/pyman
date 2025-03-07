# jira_integration.py
from jira import JIRA
from config import JIRA_SERVER, JIRA_USERNAME, JIRA_PASSWORD

# Connect to Jira
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

def create_jira_issue(summary, description, project_key, issue_type="Task"):
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    new_issue = jira.create_issue(fields=issue_dict)
    return new_issue.key

def update_jira_issue(issue_key, status):
    jira.transition_issue(issue_key, status)
    print(f"Updated Jira issue {issue_key} to status: {status}")