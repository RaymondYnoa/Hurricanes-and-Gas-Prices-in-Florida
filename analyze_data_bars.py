import pandas as pd
import matplotlib.pyplot as plt

# List of CSV file names
csv_files = [
    'eia_gasoline_prices_irma.csv',
    'eia_gasoline_prices_michael.csv',
    'eia_gasoline_prices_sally.csv',
    'eia_gasoline_prices_ian.csv',
    'eia_gasoline_prices_nicole.csv'
]

# Set hurricane date ranges and names for each file
hurricane_info = {
    'eia_gasoline_prices_irma.csv': ('2017-09-04', '2017-09-11', 'Hurricane Irma'),
    'eia_gasoline_prices_michael.csv': ('2018-10-07', '2018-10-11', 'Hurricane Michael'),
    'eia_gasoline_prices_sally.csv': ('2020-09-11', '2020-09-16', 'Hurricane Sally'),
    'eia_gasoline_prices_ian.csv': ('2022-09-23', '2022-09-30', 'Hurricane Ian'),
    'eia_gasoline_prices_nicole.csv': ('2022-11-07', '2022-11-11', 'Hurricane Nicole')
}

def calculate_averages(df, start_date, end_date):
    # Convert the period column to datetime format
    df['period'] = pd.to_datetime(df['period'])

    # Calculate average total price
    avg_total_price = df['value'].mean()

    # Calculate average price during hurricane
    mask_hurricane = (df['period'] >= start_date) & (df['period'] <= end_date)
    avg_hurricane_price = df.loc[mask_hurricane, 'value'].mean() if not df.loc[mask_hurricane].empty else 0

    return avg_total_price, avg_hurricane_price

def plot_bar_charts_to_png():
    # Initialize lists to hold the data
    labels = []
    avg_total_prices = []
    avg_hurricane_prices = []

    for csv_file in csv_files:
        try:
            df_prices = pd.read_csv(csv_file)

            # Get hurricane dates and name for the current file
            if csv_file in hurricane_info:
                highlight_start_date, highlight_end_date, hurricane_name = hurricane_info[csv_file]
            else:
                print(f"No hurricane info defined for {csv_file}")
                continue

            # Calculate averages
            avg_total_price, avg_hurricane_price = calculate_averages(df_prices, highlight_start_date, highlight_end_date)

            # Store the results
            labels.append(hurricane_name)
            avg_total_prices.append(avg_total_price)
            avg_hurricane_prices.append(avg_hurricane_price)

        except Exception as e:
            print(f"Error processing {csv_file}: {e}")

    # Plot all data on a single graph
    x = range(len(labels))  # Position of bars

    plt.figure(figsize=(14, 7))
    plt.bar(x, avg_total_prices, width=0.4, color='blue', label='Average Price Between 4 Weeks', align='center')
    plt.bar([p + 0.4 for p in x], avg_hurricane_prices, width=0.4, color='red', label='Average Price During Hurricane', align='center')

    # Add labels and title
    plt.xlabel('Hurricane')
    plt.ylabel('Price (USD)')
    plt.title('Average Gasoline Prices in Florida')
    plt.xticks([p + 0.2 for p in x], labels, rotation=45)
    plt.legend()

    # Save and show the plot
    plt.tight_layout()
    plt.savefig('combined_eia_gasoline_prices.png')
    plt.close()

# Generate and save the combined bar chart
plot_bar_charts_to_png()