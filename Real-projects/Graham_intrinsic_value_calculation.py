def graham_intrinsic_value(eps_ttm, growth_rate_percent):
    """
    Calculate intrinsic value using the Benjamin Graham formula.
    
    Formula: Intrinsic Value = EPS × (8.5 + 2 × growth rate)
    """
    g = growth_rate_percent
    intrinsic_value = eps_ttm * (8.5 + 2 * g)
    return intrinsic_value

def margin_of_safety(intrinsic_value, market_price):
    """
    Calculate the margin of safety as a percentage.
    """
    mos = (intrinsic_value - market_price) / intrinsic_value * 100
    return mos

# === Example Inputs ===
eps_ttm = 6.59                 # Example: AAPL EPS
growth_rate = 11.5             # Forward EPS growth rate (%)
current_price = 249.00         # Current market price

# === Calculations ===
iv = graham_intrinsic_value(eps_ttm, growth_rate)
mos = margin_of_safety(iv, current_price)

# === Output ===
print(f"Intrinsic Value: ${iv:.2f}")
print(f"Current Price:   ${current_price:.2f}")
print(f"Margin of Safety: {mos:.2f}%")
