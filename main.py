# main.py
import sys
from api_test import run_postman_test
from jira_integration import create_jira_issue, update_jira_issue
from jenkins_integration import trigger_jenkins_job

def main():
    # Get user input for collection, environment, and folder
    collection_choice = sys.argv[1] if len(sys.argv) > 1 else None
    env_choice = sys.argv[2] if len(sys.argv) > 2 else "SIT"
    folder_choice = sys.argv[3] if len(sys.argv) > 3 else None

    # Step 1: Run Postman tests
    test_success = run_postman_test(collection_choice, env_choice, folder_choice)

    # Step 2: Trigger Jenkins job if tests are successful
    if test_success:
        trigger_jenkins_job("your-jenkins-job", parameters={"COLLECTION": collection_choice, "ENV": env_choice})

    # Step 3: Update Jira issue
    if test_success:
        issue_key = create_jira_issue(
            summary=f"Automated test for {collection_choice}",
            description=f"Tests for {collection_choice} on {env_choice} environment completed successfully.",
            project_key="PROJ"
        )
        update_jira_issue(issue_key, "Done")
    else:
        print("❌ Tests failed. Skipping Jenkins and Jira updates.")

if __name__ == "__main__":
    main()