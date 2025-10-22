
def calculate_intrinsic_value(eps, growth_rate):

    intrinsic_value = eps * (8.5 + 2 * growth_rate)
    return intrinsic_value

def calculate_margin_of_safety(intrinsic_value, current_price):
    margin_of_safety_pct = (intrinsic_value - current_price) / intrinsic_value * 100
    return margin_of_safety_pct

def collect_stock_info():
    sticker = input("Stock sticker: ")
    eps = float(input("EPS (ttm): "))
    growth_rate = float(input("Expected growth rate (in 3-5 years): "))
    current_price = float(input("Current stock price: "))


    intrinsic_value = calculate_intrinsic_value(eps, growth_rate)
    margin_of_safety = calculate_margin_of_safety(intrinsic_value, current_price)
    stock=[sticker, eps, growth_rate, current_price, intrinsic_value, margin_of_safety]
    
    return stock

def main():
    stocks = []
    print("Collect stock info: ")
    while True:
        stock = collect_stock_info()
        stocks.append(stock)
        print("Do you want to add another stock? (y/n): ")
        choice = input().lower()
        if choice != 'y':
            break

    print("Collected stock information:")
    for stock in stocks:
        print(stock)

if __name__ == "__main__":
    main()
