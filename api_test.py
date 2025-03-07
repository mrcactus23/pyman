import sys
import subprocess
import json
import os
import webbrowser

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

collections = config["collections"]
env_mapping = config["env_mapping"]

# Get user input for collection, environment and folder/subfolder
collection_choice = sys.argv[1] if len(sys.argv) > 1 else None
env_choice = sys.argv[2] if len(sys.argv) > 2 else "SIT"
folder_choice = sys.argv[3] if len(sys.argv) > 3 else None

# Validate collection choice
if collection_choice not in collections:
    print(f"❌ Invalid collection name! Choose from: {', '.join(collections.keys())}")
    sys.exit(1)

# Get collection and environment
collection = collections[collection_choice]
environment = env_mapping.get(env_choice.upper(), "sit_env.json")

# Create a folder for the collection (if it doesn't exist)
report_folder = f"reports/{collection_choice}"
os.makedirs(report_folder, exist_ok=True)

# Function to run a specific Postman collection
def run_postman_test():
    report_file = f"{report_folder}/report_{collection_choice}.json"
    html_report_file = f"{report_folder}/report_{collection_choice}.html"

    print(f"🚀 Running Postman test for: {collection} on {env_choice} environment")
    print(f"🚀 Specifically running folder: {folder_choice}")
    print(f"📁 Saving JSON & HTML report in: {report_file} & {html_report_file}")

    newman_command = [
        'newman', 'run', collection,
        '-e', environment,
        '--reporters', 'cli,json,htmlextra',
        '--reporter-json-export', report_file,
        '--reporter-htmlextra-export', html_report_file,
        '--insecure'
    ]

    # Add --folder option if user provides a folder name
    if folder_choice:
        newman_command.extend(['--folder', folder_choice])

    try:
        subprocess.run(
            newman_command,
            check=True
        )
        print(f"✅ Postman test completed successfully for {collection} specifically folder: {folder_choice}.\n✅ Report saved at {report_file} & {html_report_file}")
        webbrowser.open('file://' + os.path.realpath(html_report_file))
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Postman test for {collection}:", e)
        return False

# Run the script
if __name__ == "__main__":
    success = run_postman_test()
    sys.exit(0 if success else 1)