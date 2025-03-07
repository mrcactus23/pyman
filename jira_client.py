from jira import JIRA
from jira.exceptions import JIRAError
import sys

class JiraClient:
    def __init__(self, server, email, api_token):
        self.server = server
        self.email = email
        self.api_token = api_token
        self.jira = None

    def connect(self):
        try:
            print("Connecting to Jira...", file=sys.stderr)
            self.jira = JIRA(server=self.server, basic_auth=(self.email, self.api_token))
            print("✅ Successfully connected to Jira!", file=sys.stderr)
            return True
        except JIRAError as e:
            print(f"❌ Failed to connect to Jira: {e}", file=sys.stderr)
            return False
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)
            return False

    def create_issue(self, project_key, summary, description, issue_type='Task'):
        if not self.jira:
            print("❌ Not connected to Jira. Call connect() first.", file=sys.stderr)
            return None

        try:
            print(f"Creating Jira ticket with summary: {summary}", file=sys.stderr)
            issue_dict = {
                'project': {'key': project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': issue_type},
            }
            new_issue = self.jira.create_issue(fields=issue_dict)
            print(f"✅ Created Jira ticket: {new_issue.key}", file=sys.stderr)
            return new_issue.key
        except JIRAError as e:
            print(f"❌ Error creating Jira ticket: {e}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)
            return None

    def update_issue_status(self, issue_key, status):
        if not self.jira:
            print("❌ Not connected to Jira. Call connect() first.", file=sys.stderr)
            return None

        try:
            print(f"Updating Jira ticket {issue_key} to status: {status}", file=sys.stderr)
            transitions = self.jira.transitions(issue_key)
            print(f"Available transitions: {[t['name'] for t in transitions]}", file=sys.stderr)

            for transition in transitions:
                if transition['name'] == status:
                    print(f"Transitioning issue {issue_key} to {status}...", file=sys.stderr)
                    self.jira.transition_issue(issue_key, transition['id'])
                    print(f"✅ Updated Jira ticket {issue_key} to status: {status}", file=sys.stderr)
                    break
        except JIRAError as e:
            print(f"❌ Error updating Jira ticket {issue_key}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)