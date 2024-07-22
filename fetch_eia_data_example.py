import requests
import pandas as pd

# Your EIA API key
api_key = 'INSERT_YOUR_API_KEY_HERE'

# EIA API URL with the API key and updated for Total Gasoline (EPM0) in Florida
# Note: EIA weekly frequency are every Monday of the week
api_url = f'https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key={api_key}&frequency=weekly&data[0]=value&facets[product][]=EPM0&facets[series][]=EMM_EPM0_PTE_SFL_DPG&start=2022-08-29&end=2022-10-03&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'

# Fetch the data from the API
response = requests.get(api_url)
data = response.json()

# Check if the API request was successful
if response.status_code != 200:
    print(f"Error fetching data: {response.status_code}")
    print(data)
    exit()

# Extract the data
if 'response' in data and 'data' in data['response']:
    records = data['response']['data']
else:
    print("No data found in API response.")
    exit()

# Check if the records are empty
if not records:
    print("No records found in the API response.")
    exit()

# Convert to pandas DataFrame
df_prices = pd.DataFrame(records)

# Debugging: Print the DataFrame
print(df_prices.head())

# Save the DataFrame to a CSV file
csv_file = 'eia_gasoline_prices_example.csv'
try:
    df_prices.to_csv(csv_file, index=False)
    print(f"Data fetched and saved to {csv_file}")
except Exception as e:
    print(f"Error saving data to CSV: {e}")