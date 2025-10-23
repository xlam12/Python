import argparse
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime

#How to run it: 
# python read_stock_data.py stock_data.csv

def show_investment_analysis(mos_pct, threshold=25):
    if mos_pct >= threshold:
        return "Undervalued"
    elif -threshold < mos_pct < threshold:
        return "Fairly Valued"
    else:
        return "Overvalued"

def compute_margin_of_safety(intrinsic_value, current_price):
    mos_usd = intrinsic_value - current_price
    mos_pct = (mos_usd / intrinsic_value) * 100 if intrinsic_value else None
    return mos_pct, mos_usd

def compute_benjamin_graham_intrinsic_value(row):
    estimate_growth_rate = row['growth_rate'] if not np.isnan(row['growth_rate']) else row['last_5yrs_growth']

    if row['EPS'] and estimate_growth_rate:
        return row['EPS'] * (8.5 + 2 * estimate_growth_rate)
    return None


def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'EPS': info.get('trailingEps'),
            'currentPrice': info.get('currentPrice')
        }
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return {'EPS': None, 'currentPrice': None}

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Data Fetching started at: {timestamp}")

    parser = argparse.ArgumentParser(description='Read stock data from file')
    parser.add_argument('filename', type=str, help='Path to the data file (CSV, JSON, Parquet)')
    args = parser.parse_args()
    try:
        if args.filename.endswith('.csv'):
            df = pd.read_csv(args.filename)
        # elif args.filename.endswith('.json'):
        #     df = pd.read_json(args.filename)
        # elif args.filename.endswith('.parquet'):
        #     df = pd.read_parquet(args.filename)
        else:
            print("Unsupported file format")
            return

        df['ticker'] = df['ticker'].str.upper()
        # print(df)

        df['growth_rate'] = pd.to_numeric(df['growth_rate'], errors='coerce')
        df['last_5yrs_growth'] = pd.to_numeric(df['last_5yrs_growth'], errors='coerce')
        
        # df['growth_rate'] = df['growth_rate'].combine_first(df['last_5yrs_growth'])
        # df['effective_growth_rate'] = np.where( np.isnan(df['growth_rate']), df['last_5yrs_growth'], df['growth_rate'])

        df[['EPS', 'currentPrice']] = df['ticker'].apply(lambda x: pd.Series(fetch_stock_data(x)))

        df['intrinsic_value'] = df.apply(compute_benjamin_graham_intrinsic_value, axis=1)
    
        # print(df)


        df[['MoS_pct', 'MoS_usd']] = df.apply(
            lambda row: pd.Series(compute_margin_of_safety(row['intrinsic_value'], row['currentPrice']))
            if row['intrinsic_value'] and row['currentPrice'] else pd.Series([None, None]),
            axis=1
        )

        df['Analysis'] = df['MoS_pct'].apply(
            lambda x: show_investment_analysis(x) if x is not None else None
        )

        print(df)

        undervalued_df = df[df['Analysis'] == "Undervalued"]
        print(f"Undervalued Tickers: {undervalued_df['ticker'].tolist()}")
        print(f"Current prices: {undervalued_df['currentPrice'].tolist()}")

    except FileNotFoundError:
        print(f"File '{args.filename}' not found.")
        return

    except Exception as e:
        print(f"Error reading file '{args.filename}': {e}")
        return

if __name__ == '__main__':
    main()