import pandas as pd

# Read in ticklist
tickList = pd.read_csv("tickList.csv", encoding='latin-1')

# Get first two columns of ticklist
tickList = tickList.iloc[:, 0].tolist()

# Remove bad tickers which are also used in common language
badTicks = ["S", "AI", "CD", "ET", "FREE", "UK", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "T", "U", "W", "X", "Y", "Z"]
for tick in badTicks:
    if tick in tickList:
        tickList.remove(tick)