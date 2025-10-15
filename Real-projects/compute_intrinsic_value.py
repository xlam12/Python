#!/usr/bin/env python3


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
        
        # Calculate intrinsic value
        intrinsic_value = calculate_intrinsic_value(eps, growth_rate)
        
        # Display results
        print("\n" + "-" * 50)
        print("RESULTS")
        print("-" * 50)
        print(f"Stock: {stock_name}")
        print(f"EPS: ${eps:.2f}")
        print(f"Expected Growth Rate: {growth_rate}%")
        print(f"Intrinsic Value: ${intrinsic_value:.2f}")
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
            f.write("=" * 50 + "\n\n")
        
        print(f"\nResults saved to '{filename}'")
        
    except ValueError:
        print("\nError: Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()