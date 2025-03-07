# jenkins_integration.py
import jenkins
from config import JENKINS_SERVER, JENKINS_USERNAME, JENKINS_PASSWORD

# Connect to Jenkins
jenkins_server = jenkins.Jenkins(JENKINS_SERVER, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)

def trigger_jenkins_job(job_name, parameters=None):
    jenkins_server.build_job(job_name, parameters=parameters)
    print(f"Triggered Jenkins job: {job_name}")