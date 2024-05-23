import csv
import requests
import pandas as pd
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
import requests
import csv
import pandas as pd
from pycountry_convert import country_name_to_country_alpha2, country_alpha2_to_continent_code

def fetch_data_from_api(api_url, api_key):
    headers = {"X-API-Key": api_key}
    response = requests.post(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None

def clean_data(data):
    cleaned_data = []
    for entry in data:
        # Check if all fields are present in the entry
        if all(field in entry for field in entry.keys()):
            cleaned_data.append(entry)
    return cleaned_data

def write_to_csv(data, filename):
    if not data:
        print("No data to write.")
        return

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)
    print(f"Data written to {filename} successfully.")

def map_country_to_continent(country_name):
    try:
        country_code = country_name_to_country_alpha2(country_name)
        continent_code = country_alpha2_to_continent_code(country_code)
        return continent_code
    except:
        return 'Unknown'

def main():
    api_url = "https://my.api.mockaroo.com/olympics.json"
    api_key = "5adf4f80"
    data = fetch_data_from_api(api_url, api_key)
    if data:
        print("Data fetched successfully:")
        print(data)
        
        cleaned_data = clean_data(data)
        print("\nCleaned Data:")
        print(cleaned_data)

        # Specify the filename for CSV
        csv_filename = "olympics_data.csv"
        write_to_csv(cleaned_data, csv_filename)

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_filename)

        # Add a new column 'Continent' to the DataFrame
        df['Continent'] = df['Country'].apply(map_country_to_continent)

        # Drop rows with NaN values in the 'Continent' column
        df.dropna(subset=['Continent'], inplace=True)

        # Save the updated DataFrame back to a CSV file
        updated_csv_filename = 'updated_csv_file.csv'
        df.to_csv(updated_csv_filename, index=False)

if __name__ == "__main__":
    main()

