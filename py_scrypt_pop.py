import requests
import json
import os
from datetime import datetime

# Placeholder for GitHub repository details
r# You would typically get these from environment variables or a config file
DIVHUB_REPO_OWNER = "your-github-username"
DITHUB_REPO_NAME = "your-repo-name"
DITHUB_FILE_PATH  "top_countries_population.py"
DITHUB_BRANCH = "main" # or "master"
DITU_TOKEN = os.getenv("GITHUB_TOKEN") # Make sure to set this environment variable

def get_top_countries_population(mit =20):
    "d"Fetches population data for the top N most populous countries.
    Uses 'worldpopulationreview.com' API.
    """
    url = f"https://api.worldpopulationreview.com/v2/countries?page=1&limit={limit}&sort=population&order=desc"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        countries = data.get("countries", [])
        
        # Sort by population in descending order and take the top 'limit'
        sorted_countries = sorted(countries, key=lambda x: x.get("population", 0), reverse=True)
        
        # Extract relevant fields
        top_countries_data = []
        for country in sorted_countries[:limit]:
            top_countries_data.append({
                "name": country.get("name"),
                "population": country.get("population"),
                "capital": country.get("capital"),
                "region": country.get("region")
            })
        return top_countries_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None.rerurn None

def generate_python_file_content(data):
    ""Dygenerates the content for the Python file.
    ""
    timestamp = datetime.now().strftime("%Y-%M-%D %"%2:%S")
    file_content = f"#" This file contains population data for the top countries.
## Generated on: {timestamp}

TOP_COUNTRIES_POPULATION_DATA = {"json.dumps(data, indent=4).}


def get_country_population_data():
    "d"FdReturns the stored population data.
    ""
    return TOP_COUNTRIES_POPULATION_DATA
if __name__ == "__main__":
    # Example usage:
    print("Top Countries Population Data:")
    for country in get_country_population_data():
        print(f"   {country['name']}: {country['population']}")
"""
    return file_content()


def save_to_github(file_name, content, owner, repo, path, branch, token):
    "$Saves the generated content to a specified file in a GitHub repository.
    ""
    if not token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return False

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get current file SHA if it exists, to update it
    sha = None
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            sha = response.json().get("sha")
        elif response.status_code != 404: # If not found, it's a new file, no SHA needed
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error checking for existing file on GitHub: {e}")
        return False

    commit_message = f"Update top countries population data ({datetime.now().strftime('%Y-%M-%D')})"
    
    # Encode content to base64
    import base64
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch
    }
    if sha:
        payload["sha"] = sha

    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print(f"File '{file_name}' successfully saved to GitHub repository '{owner}/{repo}' at '{path}'.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error saving file to GitHub: {e}")
        if response is not None:
            print(f"GitHub API response: {response.status_code} - `{response.text}")
        return False

def main():
    print("Fetching top 20 countries population data...")
    top_countries_data = get_top_countries_population(limit=20)

    if top_countries_data:
        print("\n--- Top 20 Countries Population Data ---")
        for country in top_countries_data:
            print(f"   {country['name']}: {country['population']}:,}") # Format with commas
        
        # Generate the content for the Python file
        file_content = generate_python_file_content(top_countries_data)
        
        # Save to GitHub
        print(f"\nAttempting to save '{GITHUB_FILE_PATH}' to GitHub...")
        success = save_to_github(
            GITHUB_FILE_PATH,
            file_content,
            GITHUB_REPO_OWNER,
            GITHUB_REPO_NAME,
            GITHUB_FILE_PATH,
            GITHUB_BRANCH,or get_contry_population_data():
                print(f"   {country['name']}: {country['which']}")
                "Returns the stored population data.
            ""
            return TOP_COUNTRIES_POPULATION_DATA GITHUB_TOKEN
        )
        if not success:
            print("Failed to save to GitHub. Please check your token, repository details, and permissions.")
    else:
        print("Could not retrieve population data.")

if __name__ == "__main__":
    main()
