# Import packages
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

print("----- MENU -----")
print("1. visualize stock market data for only one tickers")
print("2. visualize stock market data for multiple tickers")
print("3. Exit ")
print()

# Taking the choice from the user
choice = input("Choice : ")

# Check if input is numeric or not
while not choice.isnumeric():
    print("Wrong input! Enter choice again!")
    choice = input("Choice : ")

# converting string into integer
choice = int(choice)

if choice == 1:
    try:
        # Taking the ticker symbol from the user
        Ticker = input("Enter companies ticker symbol of which you want to check stock price : ")

        # It will rapidly download the data
        data = yf.download(Ticker, period='1d', interval='1m')

        # print(data)

        # Plot the adjusted close price
        data['Adj Close'].plot(figsize=(10, 7))

        # Define the label for the title of the figure
        plt.title(f"Adjusted Close Price of {Ticker}", fontsize=16)

        # Define the labels for x-axis and y-axis
        plt.ylabel('Price', fontsize=14)
        plt.xlabel('Minutes', fontsize=14)

        # Plot the grid lines
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

        # Show the plot
        plt.show()

    except:
        print("You're sending too many requests from same ip address in short period of time!")

elif choice == 2:
    try:
        # Taking input from the user
        n = input("How many companies of stock market you want to check : ")

        # Check if input is numeric or not
        while not n.isnumeric():
            print("Wrong input! Enter again!")
            n = input()

        # Converting into int
        n = int(n)

        # create blank list
        List = []

        # Define the ticker list
        for i in range(0, n):
            Ticker = input("Enter ticker symbol : ")
            List.append(Ticker)

        # Create placeholder for data
        info = pd.DataFrame(columns=List)

        # Fetch the data
        for ticker in info:
            info[ticker] = yf.download(ticker, period='1d', interval='1m')['Adj Close']

        # print(data)

        # Plot all the close prices
        info.plot(figsize=(10, 7))

        # Show the legend
        plt.legend()

        # Define the label for title of the figure
        plt.title("Adjusted close prices ", fontsize=16)

        # Define the label for x-axis and y-axis
        plt.xlabel('Price', fontsize=14)
        plt.ylabel('Minutes', fontsize=14)

        # Plot the grid lines
        plt.grid(which="major", color="green", linestyle="--", linewidth=0.5)

        # show the plot
        plt.show()

    except:
        print("You're sending too many requests from same ip address in short period of time!")

else:
    print("Exited the program!")
