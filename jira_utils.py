from jira import JIRA

def create_jira_ticket(summary, description, issue_type='Task', project_key='PYM'):
    """
    Create a Jira ticket with the given summary, description, and issue type.
    :param summary: Summary of the Jira ticket
    :param description: Description of the Jira ticket
    :param issue_type: Type of the Jira ticket (e.g., 'Task', 'Bug')
    :param project_key: Key of the Jira project (e.g., 'AP')
    :return: Key of the created Jira ticket (e.g., 'AP-123')
    """
    jira = JIRA(
        server='https://mrcactus23.atlassian.net',  # Replace with your Jira instance URL
        basic_auth=('mrcactus', 'ATATT3xFfGF0AdRegy5SJNbQo22FYMBtFtlEeeDPqFKKsupS1yQpYhqH6xaHCNfLj1mJq-tw-PS5WcSnbZr2UtgDHLxMabZchr9bT9srYOdlO5__GKvXu4lbzAL8oprK3YccJm9NjPKtdO7PsZHJjgQo02XCLedGpUTrLXFSmNXa3Zn2m1G7vso=92118796')  # Replace with your Jira credentials
    )

    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},  # Set issue type to 'Task'
    }

    new_issue = jira.create_issue(fields=issue_dict)
    print(f"Created Jira ticket: {new_issue.key}")
    return new_issue.key

def update_jira_status(issue_key, status):
    """
    Update the status of a Jira ticket.
    :param issue_key: Key of the Jira ticket (e.g., 'AP-123')
    :param status: New status to set (e.g., 'To Do', 'In Progress', 'Done')
    """
    jira = JIRA(
        server='https://mrcactus23.atlassian.net',  # Replace with your Jira instance URL
        basic_auth=('mrcactus', 'ATATT3xFfGF0AdRegy5SJNbQo22FYMBtFtlEeeDPqFKKsupS1yQpYhqH6xaHCNfLj1mJq-tw-PS5WcSnbZr2UtgDHLxMabZchr9bT9srYOdlO5__GKvXu4lbzAL8oprK3YccJm9NjPKtdO7PsZHJjgQo02XCLedGpUTrLXFSmNXa3Zn2m1G7vso=92118796')  # Replace with your Jira credentials
    )

    transitions = jira.transitions(issue_key)
    for transition in transitions:
        if transition['name'] == status:
            jira.transition_issue(issue_key, transition['id'])
            print(f"Updated Jira ticket {issue_key} to status: {status}")
            break