from jira import JIRA
from jira.exceptions import JIRAError
from requests import RequestException

def create_jira_ticket(summary, description, issue_type='Task', project_key='PYM'):
    try:
        print(f"Attempting to create Jira ticket with summary: {summary}")
        jira = JIRA('https://mrcactus23.atlassian.net', basic_auth=('najihahrohmat@gmail.com', 'ATATT3xFfGF0xwxa02H-pXfw03arms4CC9l4fQVJM3N-2Ej8WwQnAEpZDDb1yOtX-c9jrjqjKOE11wnMJqpET91kVmK6YdfqwywKxVe65bkvaq_CIX53U6gT_pj14feG919VYrWFdvjAs6NOQdQl_Xm4r7ydkDnqqm3YqLAoxGhJie5DiYwjBzU=002E89AB'))
        print("Connected to Jira successfully!")

        print("Creating Jira ticket...")
        new_issue = jira.create_issue(project=project_key,
                              summary=summary,
                              description=description,
                              issuetype={'name': issue_type})
        print(f"✅ Created Jira ticket: {new_issue.key}")
        return new_issue.key 
    except JIRAError as e:
        print(f"❌ Error creating Jira ticket: {e}")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None
    except RequestException as e:
        print('Response from jira: ' + str(jira))

def update_jira_status(issue_key, status):
    try:
        print(f"Attempting to update Jira ticket {issue_key} to status: {status}")
        jira = JIRA('https://mrcactus23.atlassian.net', basic_auth=('najihahrohmat@gmail.com', 'ATATT3xFfGF0xwxa02H-pXfw03arms4CC9l4fQVJM3N-2Ej8WwQnAEpZDDb1yOtX-c9jrjqjKOE11wnMJqpET91kVmK6YdfqwywKxVe65bkvaq_CIX53U6gT_pj14feG919VYrWFdvjAs6NOQdQl_Xm4r7ydkDnqqm3YqLAoxGhJie5DiYwjBzU=002E89AB'))
        print("Connected to Jira successfully!")

        transitions = jira.transitions(issue_key)
        print(f"Available transitions: {[t['name'] for t in transitions]}")

        for transition in transitions:
            if transition['name'] == status:
                print(f"Transitioning issue {issue_key} to {status}...")
                jira.transition_issue(issue_key, transition['id'])
                print(f"✅ Updated Jira ticket {issue_key} to status: {status}")
                break
    except JIRAError as e:
        print(f"❌ Error updating Jira ticket {issue_key}: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# # Add this to test the script when run directly
# if __name__ == "__main__":
#     print("Running jira_utils.py directly...")
    
#     # Test Jira connection
#     if test_jira_connection():
#         # Test creating a Jira ticket
#         issue_key = create_jira_ticket("Test Summary", "Test Description")
#         if issue_key:
#             # Test updating the Jira ticket status
#             update_jira_status(issue_key, "Done")