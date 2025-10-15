import argparse

def graham_intrinsic_value(eps_ttm, growth_rate_percent):
    """
    Calculate intrinsic value using the Benjamin Graham formula.
    
    Formula: Intrinsic Value = EPS × (8.5 + 2 × growth rate)
    """
    intrinsic_value = eps_ttm * (8.5 + 2 * growth_rate_percent)
    return intrinsic_value

def margin_of_safety(intrinsic_value, market_price):
    """
    Calculate the margin of safety as a percentage.
    """
    return (intrinsic_value - market_price) / intrinsic_value * 100

def main():
    parser = argparse.ArgumentParser(
        description="Calculate intrinsic value and margin of safety using Benjamin Graham formula"
    )
    parser.add_argument("eps", type=float, help="Earnings per Share (TTM)")
    parser.add_argument("growth", type=float, help="Expected EPS growth rate (3–5 years, as a percentage)")
    parser.add_argument("price", type=float, help="Current market price of the stock")

    args = parser.parse_args()

    intrinsic = graham_intrinsic_value(args.eps, args.growth)
    mos = margin_of_safety(intrinsic, args.price)

    print(f"Intrinsic Value:     ${intrinsic:.2f}")
    print(f"Current Stock Price: ${args.price:.2f}")
    print(f"Margin of Safety:    {mos:.2f}%")

if __name__ == "__main__":
    main()

