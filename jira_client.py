from jira import JIRA
from jira.exceptions import JIRAError

class JiraClient:
    def __init__(self, server, email, api_token):
        self.server = server
        self.email = email
        self.api_token = api_token
        self.jira = None

    def connect(self):
        try:
            print("Connecting to Jira...")
            self.jira = JIRA(server=self.server, basic_auth=(self.email, self.api_token))
            print("✅ Successfully connected to Jira!")
            return True
        except JIRAError as e:
            print(f"❌ Failed to connect to Jira: {e}")
            return False
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            return False

    def create_issue(self, project_key, summary, description, issue_type='Task'):
        if not self.jira:
            print("❌ Not connected to Jira. Call connect() first.")
            return None

        try:
            print(f"Creating Jira ticket with summary: {summary}")
            issue_dict = {
                'project': {'key': project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': issue_type},
            }
            new_issue = self.jira.create_issue(fields=issue_dict)
            print(f"✅ Created Jira ticket: {new_issue.key}")
            return new_issue.key
        except JIRAError as e:
            print(f"❌ Error creating Jira ticket: {e}")
            return None
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            return None

    def update_issue_status(self, issue_key, status):
        if not self.jira:
            print("❌ Not connected to Jira. Call connect() first.")
            return

        try:
            print(f"Updating Jira ticket {issue_key} to status: {status}")
            transitions = self.jira.transitions(issue_key)
            print(f"Available transitions: {[t['name'] for t in transitions]}")

            for transition in transitions:
                if transition['name'] == status:
                    print(f"Transitioning issue {issue_key} to {status}...")
                    self.jira.transition_issue(issue_key, transition['id'])
                    print(f"✅ Updated Jira ticket {issue_key} to status: {status}")
                    break
        except JIRAError as e:
            print(f"❌ Error updating Jira ticket {issue_key}: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")