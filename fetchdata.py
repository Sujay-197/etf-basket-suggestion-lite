import yfinance as yf
import os

def fetch_historical_data(symbol, period="ytd"):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period)
    os.makedirs("stocks_csv", exist_ok=True)
    csv_filename = f"stocks_csv/{symbol}data.csv"
    data.to_csv(csv_filename)
    print(f"Data saved to {csv_filename}")
    return data[["Open", "Close", "High", "Low", "Volume"]]



etfs = [
    # Precious Metals / Gold
    "GLD",   # SPDR Gold Shares
    "IAU",   # iShares Gold Trust
    "SGDM",  # Sprott Gold Miners
    "GDX",   # VanEck Gold Miners
    "GDXJ",  # VanEck Junior Gold Miners
    
    # Silver & Other Metals
    "SIL",   # Global X Silver Miners
    "SILJ",  # Amplify Junior Silver Miners
    "SLVP",  # iShares Silver Miners
    "RING",  # iShares Global Gold Miners
    "AUMI",  # Themes Gold Miners
    
    # Oil & Energy
    "XLE",   # Energy Select Sector SPDR
    "VDE",   # Vanguard Energy ETF
    "IXC",   # iShares Global Energy
    "USO",   # United States Oil Fund
    "OIH",   # VanEck Oil Services
    
    # Technology
    "XLK",   # Technology Select Sector
    "VGT",   # Vanguard Information Tech
    "QQQ",   # Nasdaq-100
    "SMH",   # VanEck Semiconductors
    "AIQ",   # Global X AI & Tech
    
    # Regional / Country
    "GREK",  # Greece
    "EPOL",  # Poland
    "EWZS",  # Brazil Small-Cap
    "EWY",   # South Korea
    "EWT",   # Taiwan
    
    # Defense & Aerospace
    "SHLD",  # Global X Defense Tech
    "ITA",   # iShares U.S. Aerospace & Defense
    "EUAD",  # Europe Aerospace & Defense
    "PPA",   # Invesco Aerospace & Defense
    "DFEN",  # Leveraged Aerospace & Defense
    
    # U.S. Core Index
    "VOO",   # Vanguard S&P 500
    "VTI",   # Vanguard Total Market
    "SPY",   # SPDR S&P 500
    "SCHX",  # Schwab U.S. Large Cap
    "IWB",   # Russell 1000
    
    # Dividends
    "VIG",   # Dividend Appreciation
    "SCHD",  # Schwab Dividend
    "CGDV",  # Capital Group Dividend
    "VYMI",  # International High Dividend
    "IDV",   # iShares International Dividends
    
    # International / Emerging
    "IEFA",  # MSCI EAFE (Developed ex-US)
    "VEA",   # Vanguard Developed Markets
    "VXUS",  # Vanguard Total International
    "IEMG",  # Emerging Markets
    "EEM",   # iShares Emerging Markets
    
    # U.S. Sector Diversification
    "XLF",   # Financials
    "XLV",   # Healthcare
    "XLY",   # Consumer Discretionary
    "XLP",   # Consumer Staples
    "XLU",   # Utilities
]

indian_stocks = [
    # Conglomerate / Diversified
    "RELIANCE",     # Reliance Industries
    # IT / Technology
    "TCS", "INFY",
    # Banking & Financial Services
    "HDFCBANK", "ICICIBANK",
    # Defense & Aerospace
    "HAL", "BEL",
    # Renewable Energy / Power
    "ADANIGREEN", "TATAPOWER",
    # Consumer Goods / FMCG
    "HINDUNILVR", "ITC",
    # Automotive
    "MARUTI",
    # Infrastructure & Engineering
    "LT",           # Larsen & Toubro
    # Retail
    "DMART",        # Avenue Supermarts
    # Pharma / Healthcare
    "DRREDDY", "SUNPHARMA",
    # Emerging / Tech-Fintech
    "ZOMATO", "PAYTM", "NAZARA",
    # High-Momentum Mid/Small Caps
    # (From notable 2025 rally reports)
    "RRPSEMICON", "ELITECON", "KOTHARIIND"
]

for i in indian_stocks:
    fetch_historical_data(i)
    
