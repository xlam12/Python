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
        eps = float(input("\nEnter the Earnings Per Share (EPS): $"))
        growth_rate = float(input("Enter the Expected Growth Rate (%): "))
        
        # Calculate intrinsic value
        intrinsic_value = calculate_intrinsic_value(eps, growth_rate)
        
        # Display results
        print("\n" + "-" * 50)
        print("RESULTS")
        print("-" * 50)
        print(f"EPS: ${eps:.2f}")
        print(f"Expected Growth Rate: {growth_rate}%")
        print(f"Intrinsic Value: ${intrinsic_value:.2f}")
        print("-" * 50)
        
    except ValueError:
        print("\nError: Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()