# 📊 **Stock Market Aggregator - Detailed Technical Overview**

## 🏗️ **Core Data Structure Architecture**

The system employs three specialized data structures working in concert: a **Min-Heap** for O(log n) retrieval of the lowest stock price, a **Max-Heap** (implemented cleverly by storing negative values in a min-heap) for O(log n) retrieval of the highest stock price, and a **Segment Tree** that enables O(log n) range queries for computing rolling averages and cumulative sums over date ranges. This hybrid approach balances the need for real-time extreme value detection with efficient historical data analysis.

## 🔄 **Real-Time Monitoring & Alert System**

The aggregator maintains a comprehensive price history database storing tuples of (price, stock_name, date) and implements an intelligent alert mechanism that automatically triggers notifications when stocks breach user-defined thresholds. The system processes new stock entries in O(log n) time for both heap insertions while simultaneously checking alert conditions against the stock_alerts dictionary for immediate user feedback.

## 📈 **Analytical Capabilities & Date-Range Operations**

Beyond basic tracking, the system provides sophisticated analytical functions including precise date-range filtering for computing averages, maximum prices within specific time windows, and rolling average calculations that show price trend evolution. The segment tree implementation ensures these range queries execute efficiently even as the dataset grows, while the heap structures guarantee constant-time access to current market extremes.

## 🎯 **Interactive Financial Dashboard**

Through a structured command-line interface, users can dynamically add stocks, set customized price alerts, and retrieve various metrics including lowest/highest performing stocks, time-weighted averages, and rolling price trends. The system demonstrates practical application of advanced data structures in financial technology, combining theoretical efficiency with real-world usability for informed investment decision-making.
