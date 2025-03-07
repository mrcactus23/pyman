# config.py
import json

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Jira Configuration
JIRA_SERVER = config.get("jira_server", "https://mrcactus23.atlassian.net/jira/")
JIRA_USERNAME = config.get("jira_username", "username")
JIRA_PASSWORD = config.get("jira_password", "password")

# Jenkins Configuration
JENKINS_SERVER = config.get("jenkins_server", "http://localhost:8080/")
JENKINS_USERNAME = config.get("jenkins_username", "username")
JENKINS_PASSWORD = config.get("jenkins_password", "password")

# Newman Configuration
COLLECTIONS = config.get("collections", {})
ENV_MAPPING = config.get("env_mapping", {})