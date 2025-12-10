Stock Market Aggregator

Stock Market Aggregator is a Python program designed to track stock prices, calculate key statistics, and provide real-time alerts. It efficiently handles large datasets and allows users to query historical stock data over custom date ranges.

Features

Track Stock Prices
Add stock prices along with their dates and names.

Efficient Min/Max Tracking
Uses MinHeap and MaxHeap data structures to quickly retrieve the lowest and highest stock prices.

Alerts
Set price thresholds for stocks and get notifications if a stock price drops below the threshold.

Range Queries & Averages
Uses a Segment Tree for efficient calculation of:

Average price of a stock over a date range

Maximum price of a stock over a date range

Rolling averages for trend analysis

Interactive CLI
Users can input stock prices, set alerts, and request statistical information directly from the command line.

How It Works

Adding Stocks: Stock prices are added along with their date and name. Heaps are updated for quick retrieval of min/max prices.

Alerts: When a new stock price is added, it checks if the price violates any user-set thresholds and triggers an alert.

Querying Statistics:

get_average_price() → calculates the average price in a date range.

get_maximum_price() → finds the maximum price in a date range.

get_rolling_average() → computes cumulative averages to show trends.

Data Structures Used

MinHeap / MaxHeap: For O(1) retrieval of lowest/highest stock prices.

Segment Tree: For efficient range sum, average, and update operations.
