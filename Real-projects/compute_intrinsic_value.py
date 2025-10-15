def calculate_intrinsic_value(eps, growth_rate):
    """
    Calculate the intrinsic value of a stock using the Benjamin Graham formula.
    
    Formula: Intrinsic Value = EPS × (8.5 + 2 × Expected Growth Rate)
    
    Parameters:
    eps (float): Earnings Per Share
    growth_rate (float): Expected annual growth rate (as a percentage, e.g., 15 for 15%)
    
    Returns:
    float: The calculated intrinsic value
    """
    intrinsic_value = eps * (8.5 + 2 * growth_rate)
    return intrinsic_value


def calculate_margin_of_safety(intrinsic_value, market_price):
    """
    Calculate the margin of safety for a stock.
    
    Formula: Margin of Safety (%) = ((Intrinsic Value - Market Price) / Intrinsic Value) × 100
    
    Parameters:
    intrinsic_value (float): Calculated intrinsic value of the stock
    market_price (float): Current market price of the stock
    
    Returns:
    float: The margin of safety as a percentage
    """
    if intrinsic_value == 0:
        return 0
    margin_of_safety = ((intrinsic_value - market_price) / intrinsic_value) * 100
    return margin_of_safety


def main():
    print("=" * 50)
    print("Stock Intrinsic Value Calculator")
    print("Benjamin Graham Formula")
    print("=" * 50)
    
    try:
        # Get user input
        stock_name = input("\nEnter the Stock Name or Ticker: ")
        eps = float(input("Enter the Earnings Per Share (EPS): $"))
        growth_rate = float(input("Enter the Expected Growth Rate (%): "))
        market_price = float(input("Enter the Current Market Price: $"))
        
        # Calculate intrinsic value
        intrinsic_value = calculate_intrinsic_value(eps, growth_rate)
        
        # Calculate margin of safety
        margin_of_safety = calculate_margin_of_safety(intrinsic_value, market_price)
        
        # Display results
        print("\n" + "-" * 50)
        print("RESULTS")
        print("-" * 50)
        print(f"Stock: {stock_name}")
        print(f"EPS: ${eps:.2f}")
        print(f"Expected Growth Rate: {growth_rate}%")
        print(f"Intrinsic Value: ${intrinsic_value:.2f}")
        print(f"Market Price: ${market_price:.2f}")
        print(f"Margin of Safety: {margin_of_safety:.2f}%")
        
        # Investment recommendation
        if margin_of_safety > 0:
            print(f"\nAnalysis: Stock is UNDERVALUED by ${intrinsic_value - market_price:.2f}")
        elif margin_of_safety < 0:
            print(f"\nAnalysis: Stock is OVERVALUED by ${market_price - intrinsic_value:.2f}")
        else:
            print(f"\nAnalysis: Stock is fairly valued")
        
        print("-" * 50)
        
        # Save results to file
        filename = "intrinsic_value_results.txt"
        with open(filename, "a") as f:
            f.write("=" * 50 + "\n")
            f.write("Stock Intrinsic Value Calculation\n")
            f.write("=" * 50 + "\n")
            f.write(f"Stock: {stock_name}\n")
            f.write(f"EPS: ${eps:.2f}\n")
            f.write(f"Expected Growth Rate: {growth_rate}%\n")
            f.write(f"Intrinsic Value: ${intrinsic_value:.2f}\n")
            f.write(f"Market Price: ${market_price:.2f}\n")
            f.write(f"Margin of Safety: {margin_of_safety:.2f}%\n")
            
            if margin_of_safety > 0:
                f.write(f"Analysis: Stock is UNDERVALUED by ${intrinsic_value - market_price:.2f}\n")
            elif margin_of_safety < 0:
                f.write(f"Analysis: Stock is OVERVALUED by ${market_price - intrinsic_value:.2f}\n")
            else:
                f.write(f"Analysis: Stock is fairly valued\n")
            
            f.write("=" * 50 + "\n\n")
        
        print(f"\nResults saved to '{filename}'")
        
    except ValueError:
        print("\nError: Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()