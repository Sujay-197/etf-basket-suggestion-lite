import sqlite3
import os
import csv
import json

categories = [
  "Large-Cap", "Mid-Cap", "Small-Cap", "Growth", "Value", "Dividend", "High Yield",
  "Technology", "Healthcare", "Financials", "Energy", "Oil & Gas", "Industrials",
  "Consumer Staples", "Consumer Discretionary", "Utilities", "Real Estate", "REITs",
  "Artificial Intelligence", "Cloud Computing", "Cybersecurity", "Clean Energy",
  "EVs", "Batteries", "Biotechnology", "Robotics",
  "US", "Europe", "India", "China", "Emerging Markets", "Global", "World",
  "Gold", "Silver", "Oil", "Natural Gas", "Agriculture",
  "Government Bonds", "Corporate Bonds", "Municipal Bonds",
  "Short-Term Bonds", "Long-Term Bonds",
  "ESG", "Sustainability", "Inflation-Protected", "TIPS",
  "Hedge ETFs", "Inverse ETFs", "Currency ETFs"
]

tickers = [
  'GLD', 'IAU', 'SGDM', 'GDX', 'GDXJ', 'SIL', 'SILJ', 'SLVP', 'RING', 'AUMI',
  'XLE', 'VDE', 'IXC', 'USO', 'OIH', 'XLK', 'VGT', 'QQQ', 'SMH', 'AIQ',
  'GREK', 'EPOL', 'EWZS', 'EWY', 'EWT', 'SHLD', 'ITA', 'EUAD', 'PPA', 'DFEN',
  'VOO', 'VTI', 'SPY', 'SCHX', 'IWB', 'VIG', 'SCHD', 'CGDV', 'VYMI', 'IDV',
  'IEFA', 'VEA', 'VXUS', 'IEMG', 'EEM', 'XLF', 'XLV', 'XLY', 'XLP', 'XLU',
  'RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK', 'HAL', 'BEL',
  'ADANIGREEN', 'TATAPOWER', 'HINDUNILVR', 'ITC', 'MARUTI', 'LT', 'DMART',
  'DRREDDY', 'SUNPHARMA', 'ZOMATO', 'PAYTM', 'NAZARA', 'RRPSEMICON',
  'ELITECON', 'KOTHARIIND'
]

def create_hm():
  # Initialize hashmap
  etf_map = {ticker: {cat: 0.0 for cat in categories} for ticker in tickers}

  # -----------------------------
  # Gold ETFs
  for t in ["GLD","IAU","SGDM"]:
      etf_map[t]["Gold"] = 1.0
      etf_map[t]["Hedge ETFs"] = 0.6
      etf_map[t]["US"] = 0.3
      etf_map[t]["Global"] = 0.2

  # Gold Miners
  for t in ["GDX","GDXJ"]:
      etf_map[t]["Gold"] = 0.9
      etf_map[t]["Energy"] = 0.2
      etf_map[t]["US"] = 0.4
      etf_map[t]["Global"] = 0.3

  # Silver ETFs
  for t in ["SIL","SILJ","SLVP"]:
      etf_map[t]["Silver"] = 1.0
      etf_map[t]["Hedge ETFs"] = 0.4
      etf_map[t]["US"] = 0.3

  # Oil & Energy ETFs
  for t in ["XLE","VDE","IXC","USO","OIH"]:
      etf_map[t]["Energy"] = 1.0
      etf_map[t]["Oil & Gas"] = 0.9
      etf_map[t]["US"] = 0.8
      etf_map[t]["Global"] = 0.3

  # Tech ETFs
  for t in ["XLK","VGT","QQQ","SMH","AIQ"]:
      etf_map[t]["Technology"] = 1.0
      etf_map[t]["Growth"] = 0.8
      etf_map[t]["US"] = 1.0
      if t=="AIQ":
          etf_map[t]["Artificial Intelligence"] = 1.0

  # Regional ETFs
  etf_map["GREK"]["Europe"] = 1.0
  etf_map["EPOL"]["Emerging Markets"] = 1.0
  etf_map["EWZS"]["Emerging Markets"] = 1.0
  etf_map["EWY"]["Emerging Markets"] = 1.0
  etf_map["EWT"]["Emerging Markets"] = 1.0
  etf_map["SHLD"]["Emerging Markets"] = 1.0
  etf_map["ITA"]["Europe"] = 1.0
  etf_map["EUAD"]["Europe"] = 1.0
  etf_map["PPA"]["Emerging Markets"] = 1.0
  etf_map["DFEN"]["Emerging Markets"] = 1.0

  # US Index ETFs
  for t in ["VOO","VTI","SPY","SCHX","IWB"]:
      etf_map[t]["Large-Cap"] = 1.0
      etf_map[t]["US"] = 1.0
  for t in ["VIG","SCHD"]:
      etf_map[t]["Large-Cap"] = 0.8
      etf_map[t]["Dividend"] = 1.0
      etf_map[t]["US"] = 1.0

  # International ETFs
  for t in ["IEFA","VEA","VXUS"]:
      etf_map[t]["Global"] = 1.0
  for t in ["IEMG","EEM"]:
      etf_map[t]["Emerging Markets"] = 1.0

  # Sector ETFs
  etf_map["XLF"]["Financials"] = 1.0
  etf_map["XLV"]["Healthcare"] = 1.0
  etf_map["XLY"]["Consumer Discretionary"] = 1.0
  etf_map["XLP"]["Consumer Staples"] = 1.0
  etf_map["XLU"]["Utilities"] = 1.0

  # Indian Stocks
  india_tech = ["TCS","INFY"]
  india_energy = ["RELIANCE","ADANIGREEN","TATAPOWER","HAL","BEL"]
  india_finance = ["HDFCBANK","ICICIBANK"]
  india_consumer = ["HINDUNILVR","ITC","MARUTI","DMART","ZOMATO","PAYTM","NAZARA"]
  india_health = ["DRREDDY","SUNPHARMA","RRPSEMICON"]
  india_industrial = ["ELITECON","KOTHARIIND","LT"]

  for t in tickers:
      if t in india_tech:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Technology"] = 1.0
      if t in india_energy:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Energy"] = 1.0
      if t in india_finance:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Financials"] = 1.0
      if t in india_consumer:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Consumer Discretionary"] = 0.6
          etf_map[t]["Consumer Staples"] = 0.4
      if t in india_health:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Healthcare"] = 1.0
      if t in india_industrial:
          etf_map[t]["India"] = 1.0
          etf_map[t]["Industrials"] = 1.0

  return etf_map

etfmap = create_hm()

def fetch_etf_map(ticker):
    return etfmap.get(ticker)

def create_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS etfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            histdata TEXT,
            weight TEXT
        )
    ''')
    
    conn.commit()
    return conn

def insert_etf(conn, name, histdata, weight):
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO etfs (name, histdata, weight) VALUES (?, ?, ?)', (name, histdata, weight))
    conn.commit()

def insert_historical_data(conn, etf_id, csv_path):
    # This function is not needed with the new schema and is left as a placeholder.
    pass
    

for ticker in tickers:
    etf_weights = fetch_etf_map(ticker)
    if etf_weights is None:
        print(f"No mapping found for {ticker}, skipping...")
        continue

    # Create or connect to the database
    db_path = "etfs_data.db"
    conn = create_db(db_path)

    # Insert ETF and get its ID
    hist_data = f"stocks_csv/{ticker}data.csv"
    
    # Convert etf_weights for current ticker to JSON string
    weight = json.dumps(etf_weights)

    # Insert category weights
    insert_etf(conn, ticker, hist_data, weight)

    conn.commit()
    conn.close()