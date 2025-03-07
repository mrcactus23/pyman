from jira_client import JiraClient
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 jira_utils.py <command> [args]", file=sys.stderr)
        print("Commands: create <summary> <description> | update <issue_key> <status>", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    # Jira credentials
    server = 'https://mrcactus23.atlassian.net'
    email = 'najihahrohmat@gmail.com'
    api_token = 'ATATT3xFfGF0xwxa02H-pXfw03arms4CC9l4fQVJM3N-2Ej8WwQnAEpZDDb1yOtX-c9jrjqjKOE11wnMJqpET91kVmK6YdfqwywKxVe65bkvaq_CIX53U6gT_pj14feG919VYrWFdvjAs6NOQdQl_Xm4r7ydkDnqqm3YqLAoxGhJie5DiYwjBzU=002E89AB'

    # Initialize Jira client
    jira_client = JiraClient(server, email, api_token)

    if command == 'create':
        if len(sys.argv) < 4:
            print("Usage: python3 jira_utils.py create <summary> <description>", file=sys.stderr)
            sys.exit(1)

        summary = sys.argv[2]
        description = sys.argv[3]

        # Test Jira connection
        if jira_client.connect():
            # Create a Jira ticket
            issue_key = jira_client.create_issue(
                project_key='PYM',
                summary=summary,
                description=description,
                issue_type='Task'
            )
            if issue_key:
                print(issue_key)  # Print ONLY the issue key for Jenkins to capture
            else:
                sys.exit(1)  # Exit with error if ticket creation fails

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python3 jira_utils.py update <issue_key> <status>", file=sys.stderr)
            sys.exit(1)

        issue_key = sys.argv[2]
        status = sys.argv[3]

        # Test Jira connection
        if jira_client.connect():
            # Update the Jira ticket status
            jira_client.update_issue_status(issue_key, status)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()