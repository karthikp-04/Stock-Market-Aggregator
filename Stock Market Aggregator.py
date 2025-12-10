# Min-Heap for tracking the lowest stock price
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, stock):
        self.heap.append(stock)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_stock = self.heap.pop()
        self._heapify_down(0)
        return min_stock

    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Max-Heap for tracking the highest stock price
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, stock):
        self.heap.append((-stock[0], stock[1]))  # Store negative price for max-heap behavior
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_stock = self.heap.pop()
        self._heapify_down(0)
        return (-max_stock[0], max_stock[1])

    def peek(self):
        return (-self.heap[0][0], self.heap[0][1]) if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent][0]:  # Compare by negative prices for max-heap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Segment Tree for efficient range queries
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.tree[pos << 1] + self.tree[pos << 1 | 1]

    def query(self, left, right):
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]
            left >>= 1
            right >>= 1
        return result

    def average(self, left, right):
        total = self.query(left, right)
        count = right - left
        return total / count if count > 0 else 0

# Stock Market Aggregator for tracking stocks and calculating various statistics
class StockMarketAggregator:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.price_data = []  # Store (price, stock_name, date) tuples
        self.stock_alerts = {}

    def add_stock_price(self, stock_name, price, date):
        self.price_data.append((price, stock_name, date))
        self.min_heap.push((price, stock_name))
        self.max_heap.push((price, stock_name))

        # Check alerts
        if stock_name in self.stock_alerts:
            threshold = self.stock_alerts[stock_name]
            if price < threshold:
                print(f"Alert: {stock_name} has dropped below the threshold of {threshold}! Current price: {price}")

    def set_alert(self, stock_name, threshold):
        self.stock_alerts[stock_name] = threshold

    def get_lowest_stock(self):
        return self.min_heap.peek()

    def get_highest_stock(self):
        return self.max_heap.peek()

    def get_average_price(self, stock_name, start_date, end_date):
        filtered_data = [price for price, name, date in self.price_data
                         if name == stock_name and start_date <= date <= end_date]
        if filtered_data:
            return sum(filtered_data) / len(filtered_data)
        else:
            return 0

    def get_maximum_price(self, stock_name, start_date, end_date):
        filtered_data = [price for price, name, date in self.price_data
                         if name == stock_name and start_date <= date <= end_date]
        return max(filtered_data) if filtered_data else None

    def get_rolling_average(self, stock_name, start_date, end_date):
        filtered_data = [price for price, name, date in self.price_data
                         if name == stock_name and start_date <= date <= end_date]
        if not filtered_data:
            return []
        return [sum(filtered_data[:i + 1]) / (i + 1) for i in range(len(filtered_data))]

# Example Usage with User Input
if __name__ == "__main__":
    aggregator = StockMarketAggregator()

    # Set number of stock prices to add
    num_prices = int(input("Enter the number of stock prices to add: "))

    # Add stock prices with user input
    for _ in range(num_prices):
        stock_name = input("Enter stock name: ")
        price = float(input(f"Enter the price for {stock_name}: "))
        date = input(f"Enter the date for {stock_name} (YYYY-MM-DD): ")
        aggregator.add_stock_price(stock_name, price, date)

    # Set alerts
    set_alerts = input("Do you want to set price alerts? (yes/no): ").lower()
    if set_alerts == 'yes':
        stock_name = input("Enter stock name for alert: ")
        threshold = float(input(f"Set the alert threshold for {stock_name}: "))
        aggregator.set_alert(stock_name, threshold)

    # Get the lowest stock price
    print("Lowest Stock:", aggregator.get_lowest_stock())

    # Get the highest stock price
    print("Highest Stock:", aggregator.get_highest_stock())

    # Get average price for a stock in a user-specified date range
    stock_name = input("Enter stock name for average price: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    average_price = aggregator.get_average_price(stock_name, start_date, end_date)
    print(f"Average Price of {stock_name}:", average_price)

    # Get maximum price for a stock in a user-specified date range
    stock_name = input("Enter stock name for maximum price: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    max_price = aggregator.get_maximum_price(stock_name, start_date, end_date)
    print(f"Max Price of {stock_name}:", max_price)

    # Get rolling average for a stock in a user-specified date range
    stock_name = input("Enter stock name for rolling average: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    rolling_average = aggregator.get_rolling_average(stock_name, start_date, end_date)
    print(f"Rolling Average of {stock_name}:", rolling_average)
