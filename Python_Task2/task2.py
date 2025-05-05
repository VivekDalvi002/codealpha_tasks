import yfinance as yf

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            self.portfolio[ticker] += quantity
        else:
            self.portfolio[ticker] = quantity
        print(f"Added {quantity} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            if self.portfolio[ticker] >= quantity:
                self.portfolio[ticker] -= quantity
                print(f"Removed {quantity} shares of {ticker} from the portfolio.")
                if self.portfolio[ticker] == 0:
                    del self.portfolio[ticker]
            else:
                print("Not enough shares to remove.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nCurrent Portfolio:")
        for ticker, quantity in self.portfolio.items():
            stock_data = yf.Ticker(ticker)
            current_price = stock_data.info['regularMarketPrice']
            print(f"{ticker}: {quantity} shares, Current Price: ${current_price:.2f}, Total Value: ${current_price * quantity:.2f}")

def main():
    tracker = StockPortfolioTracker()

    while True:
        print("\nStock Portfolio Tracker Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity of shares: "))
            tracker.add_stock(ticker, quantity)
        elif choice == '2':
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity of shares to remove: "))
            tracker.remove_stock(ticker, quantity)
        elif choice == '3':
            tracker.view_portfolio()
        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
