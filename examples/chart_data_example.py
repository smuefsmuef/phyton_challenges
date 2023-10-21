# Petra Kohler, a01762430@tec.mx

# Create a visualization board that shows how the pandemic has affected the airline company United. Your Python
# program should load the information from the Excel file into a Dataframe of the Pandas library and make two graphs
# (through the matplotlib library) of different types that clearly show how the pandemic has affected the United
# company. You choose what criteria you will show in your charts.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("ChartData.xlsx", engine="openpyxl")

# as a test only to check that the data is read correctly,
data.info()
# print the first entry of the document
print(data.head(1))


# group months (to have a bit less data)
def extract_month_year(date):
    # convert str date to date object
    date = pd.to_datetime(date)
    return "{:04d}.{:02d}".format(date.year, date.month)


data['Year-Month'] = data['Date'].apply(extract_month_year)

# calculate the average stock market closing price for each month
monthly_avg_close = data.groupby('Year-Month')['Close/Price'].mean()

# sort the data by year ascending
monthly_avg_close = monthly_avg_close.sort_index(ascending=True)

# plot chart - average closing price
plt.figure(figsize=(12, 12))
plt.plot(monthly_avg_close.index, monthly_avg_close.values, marker='+', linestyle='-', color='orange', linewidth=2)
plt.title("Average Closing Price of the United Airlines stock during the Pandemic", fontsize=16,
          fontdict={'fontweight': 'bold'})
plt.xlabel("Period", fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.ylabel("Price ($)", fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xticks(rotation=45)
plt.grid(True)
# Highlight the pandemic timerange
plt.axvspan("2019.12", "2020.06", alpha=0.1, color='grey')


### second plot


# Stock transactions over time
monthly_volume = data.groupby('Year-Month')['Volume'].sum()
monthly_volume_in_Billions = monthly_volume.sort_index(ascending=True)

# bar chart - transactions
plt.figure(figsize=(12, 10))
plt.bar(monthly_volume_in_Billions.index, monthly_volume_in_Billions.values / 1000000, color='lightgreen', alpha=0.7,
        linewidth=2)
plt.title("Monthly Transactions of United Airlines Stocks during the Pandemic", fontsize=16,
          fontdict={'fontweight': 'bold'})
plt.xlabel("Period", fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.ylabel("Transactions (in Billions)", fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xticks(rotation=45)
plt.grid(axis='y')
# Highlight the pandemic timerange
plt.axvspan("2019.12", "2020.06", alpha=0.1, color='grey')


plt.show()
