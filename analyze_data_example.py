import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the CSV file
df_prices = pd.read_csv('eia_gasoline_prices_example.csv')

# Convert the period column to datetime format
df_prices['period'] = pd.to_datetime(df_prices['period'])

# Define the date range for the plot
plot_start_date = '2022-09-12'
plot_end_date = '2022-10-10'

# Filter the DataFrame based on the plot date range
mask_plot = (df_prices['period'] >= plot_start_date) & (df_prices['period'] <= plot_end_date)
df_plot_filtered = df_prices[mask_plot]

# Define the date range to highlight in red
highlight_start_date = '2022-09-23'
highlight_end_date = '2022-09-30'

# Plot gasoline prices over the filtered date range
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_plot_filtered, x='period', y='value', label='Total Gasoline Price (EPM0)')

# Add a shaded region to highlight the specific date range
plt.axvspan(pd.to_datetime(highlight_start_date), pd.to_datetime(highlight_end_date), color='red', alpha=0.3, label='Hurricane Ian (Category 4)')

# Title and labels
plt.title(f'Weekly Retail Gasoline Prices (EPM0) in Florida from {plot_start_date} to {plot_end_date}')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Set x-axis limits
plt.xlim(pd.to_datetime(plot_start_date), pd.to_datetime(plot_end_date))

# Save and show the plot
plt.savefig('eia_gasoline_prices_example_plot.png')
plt.show()