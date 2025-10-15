import argparse
import csv
import os
from datetime import datetime

def graham_intrinsic_value(eps_ttm, growth_rate_percent):
    return eps_ttm * (8.5 + 2 * growth_rate_percent)

def margin_of_safety_percent(intrinsic_value, market_price):
    return (intrinsic_value - market_price) / intrinsic_value * 100

def margin_of_safety_dollar(intrinsic_value, market_price):
    return intrinsic_value - market_price

def investment_analysis(mos_percent, threshold=10):
    if mos_percent >= threshold:
        return "Undervalued"
    elif -threshold < mos_percent < threshold:
        return "Fairly Valued"
    else:
        return "Overvalued"

def write_result_to_file(filename, row):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(
        description="Calculate intrinsic value and margin of safety using the Benjamin Graham formula"
    )
    parser.add_argument("ticker", type=str, help="Stock ticker symbol (e.g., AAPL)")
    parser.add_argument("eps", type=float, help="Earnings Per Share (TTM)")
    parser.add_argument("growth", type=float, help="Expected EPS growth rate (3–5 years, as a percentage)")
    parser.add_argument("price", type=float, help="Current market price of the stock")

    args = parser.parse_args()

    intrinsic = graham_intrinsic_value(args.eps, args.growth)
    mos_percent = margin_of_safety_percent(intrinsic, args.price)
    mos_dollar = margin_of_safety_dollar(intrinsic, args.price)
    analysis = investment_analysis(mos_percent)

    print("\n📊 Graham Valuation Summary")
    print("-----------------------------")
    print(f"Stock Ticker:          {args.ticker.upper()}")
    print(f"Stock Price:           ${args.price:.2f}")
    print(f"EPS (TTM):             ${args.eps:.2f}")
    print(f"Expected Growth Rate:  {args.growth:.2f}%")
    print(f"Intrinsic Value:       ${intrinsic:.2f}")
    print(f"Margin of Safety:      {mos_percent:.2f}%")
    print(f"Margin of Safety ($):  ${mos_dollar:.2f}")
    print(f"📈 Investment Analysis: {analysis}")
    print("-----------------------------")

    result_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "stock": args.ticker.upper(),
        "stock_price": round(args.price, 2),
        "EPS": round(args.eps, 2),
        "EGR": round(args.growth, 2),
        "Intrinsic": round(intrinsic, 2),
        "MoS_pct": round(mos_percent, 2),
        "MoS_usd": round(mos_dollar, 2),
        "analysis": analysis
    }

    output_file = "graham_valuation_results.csv"
    write_result_to_file(output_file, result_row)
    print(f"✅ Result appended to '{output_file}'")

if __name__ == "__main__":
    main()
