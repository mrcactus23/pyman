# api_test.py
import sys
import subprocess
import os
import webbrowser
from config import COLLECTIONS, ENV_MAPPING

def run_postman_test(collection_choice, env_choice, folder_choice=None):

    print("run_postman_test", collection_choice, env_choice)
    
    # Validate collection choice
    if collection_choice not in COLLECTIONS:
        print(f"❌ Invalid collection name! Choose from: {', '.join(COLLECTIONS.keys())}")
        sys.exit(1)

    # Get collection and environment
    collection = COLLECTIONS[collection_choice]
    environment = ENV_MAPPING.get(env_choice.upper(), "sit_env.json")

    # Create a folder for the collection (if it doesn't exist)
    report_folder = f"reports/{collection_choice}"
    os.makedirs(report_folder, exist_ok=True)

    # Define report files
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
        subprocess.run(newman_command, check=True)
        print(f"✅ Postman test completed successfully for {collection} specifically folder: {folder_choice}.\n✅ Report saved at {report_file} & {html_report_file}")

        # Open the HTML report
        webbrowser.open('file://' + os.path.realpath(html_report_file))
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Postman test for {collection}:", e)
        return False
