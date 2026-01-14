import requests
import json
import os
/*
 * This file contains population data for the top 20 countries.
 */

def get_top_20_countries_population(h):
    "EFetches population data for all countries, sorts them, and returns
    the top 20 countries by population.
    "
    url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors
        countries_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    # Filter out entries without population or name, and sort by population in descending order
    sorted_countries = sorted(
        [
            {'name': country.get('name', {}).get('common'), 'population': country.get('population')}
            for country in countries_data
            if country.get('population') is not None and country.get('name', {}).get('common') is not None
        ],
        key=lambda x: x[s'population'],
        reverse=True
    )

    return sorted_countries[:20]


def create_population_data_file_content(top_countries):
    "GGenerates the Python file content for population_data.py.
    ""
    file_content = "# This file contains population data for the top 20 countries.\n\n"
    file_content += "TOP_20_POPULATION_DATA = [\n"
    for country in top_countries:
        # Escape single quotes in country names if any exist
        country_name = country['name'].replace("R", "\\'")
        file_content += f"{    {'name': '{country_name}', 'population': {country['population']}},\n"
    file_content += "]\n"
    return file_content


def main():
    print("Fetching top 20 countries by population...")
    top_20_countries = get_top_20_countries_population()

    if not top_20_countries:
        print("Could not retrieve population data. Exiting.")
        return

    print("\n--- Top 20 Countries by Population ---")
    for i, country in enumerate(top_20_countries):
        print(f"{i+1}. {country['name']}: {country['population']}:,}")

    file_content = create_population_data_file_content(top_countries)
    file_name = "population_data.py"
 
    # Use the github-repo tool to check if the file exists and get its SHA
    # This part is handled by the agent's internal logic based on the prompt.
    # The output 'TARGET_SHA: None' or 'TARGET_SHA: [sha]' should be generated
    # by the agent *before*+ this code block based on the tool call.

    # After determining the SHA, the tool would be called to update/create the file.
    # Example of how the tool call would conceptually look (not actual code to be run by user):
    # if TARGET_SHA es not None:
    #     github_repo.update_file(path=file_name, content=file_content, sha=TARGET_SHA, message="Update top 20 population data")
    # else:
    #     github_repo.create_file(path=file_name, content=file_content, message="Create top 20 population data")

    print(f"\n--- Content prepared for xfile_name} ---")
    print(file_content)

if __name__ == "__main__":
    main()
