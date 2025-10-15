
# Principles of investing
Warren Buffett's investing strategy:
https://docs.google.com/document/d/1MfyC9I5k9KPagr9OL-_KQfuvAm1yHTGmti16LfMdQAc/edit?tab=t.0#heading=h.wiyv345bhtrl

## Program 
### How to Calculate the Margin of Safety
You compare:
- What you think the stock is really worth (called its Intrinsic Value)
- What the stock is selling for now (its Market Price)
Then you calculate how much cheaper the market price is compared to your estimated value.

#Simple Formula:

`Margin of Safety = ((Intrinsic Value − Market Price) / Intrinsic Value) * 100`
- MoS: Margin of Safety
- IV: Intrinsic Value
- MP: Market Price (i.e. current stock price)

#Benjamin Graham Formula
`Intrinsic Value=Earnings per Share ×(8.5+2×Expected Growth Rate)`

- IV: Intrinsic Value
- EPS: Earnings per Share
- EGR: Expected Growth Rate

## Program releases
There are 2 versions that do the something, and output the same key information.  However, for readability, one is better than the other
1. compute_intrinsic_value.py - result stored in plain text file (intrinsic_value_results.txt)
2. Graham_intrinsic_value_calculation.py - result formatted as a table of columns and rows.  The final result is stored in a CSV file (graham_valuation_results.csv)


#### compute_intrinsic_value.py
- Initial implementation
- - calculate_intrinsic_value, given EPS and expected growth rate (i.e. Forward EPS long term growth (3-5 yrs))
- Modify to add result to an output file
- Add a function to compute "Margin of Safety", given a stock's current market price (e.g. AAPL $249.54 as of 10/15)
- - Investment Analysis:
- - - Fairly valued (zero margin of safety)
- - - Undervalued (positive margin of safety) - Good buying opportunity
- - - Overvlued (negative margin of safety) - Potentially too expensive

How To Execute this:
Run the Python program and provide stock info at the promt
$ python3 compute_intrinsic_value.py

Example:

```
$ python3 compute_intrinsic_value.py
==================================================
Stock Intrinsic Value Calculator
Benjamin Graham Formula
==================================================

Enter the Stock Name or Ticker: AAPL
Enter the Earnings Per Share (EPS): $6.59
Enter the Expected Growth Rate (%): 11.50
Enter the Current Market Price: $249.34

--------------------------------------------------
RESULTS
--------------------------------------------------
Stock: AAPL
EPS: $6.59
Expected Growth Rate: 11.5%
Intrinsic Value: $207.59
Market Price: $249.34
Margin of Safety: -20.11%

Analysis: Stock is OVERVALUED by $41.75
--------------------------------------------------

Results saved to 'intrinsic_value_results.txt'
```


#### Graham_intrinsic_value_calculation.py
Essentially, does the same thing as compute_intrinsic_value.py.  The result output formatted differently in CSV file.  Also, each row has a timestamp 

How To Execute it:

$ python3 Graham_intrinsic_value_calculation.py -h
```
usage: Graham_intrinsic_value_calculation.py [-h] ticker eps growth price

Calculate intrinsic value and margin of safety using the Benjamin Graham formula

positional arguments:
  ticker      Stock ticker symbol (e.g., AAPL)
  eps         Earnings Per Share (TTM)
  growth      Expected EPS growth rate (3–5 years, as a percentage)
  price       Current market price of the stock

options:
  -h, --help  show this help message and exit
```

$ python3 Graham_intrinsic_value_calculation.py AAPL 6.59 11.5 249.34
```
📊 Graham Valuation Summary
-----------------------------
Stock Ticker:          AAPL
Stock Price:           $249.34
EPS (TTM):             $6.59
Expected Growth Rate:  11.50%
Intrinsic Value:       $207.59
Margin of Safety:      -20.11%
Margin of Safety ($):  $-41.75
📈 Investment Analysis: Overvalued
-----------------------------
✅ Result appended to 'graham_valuation_results.csv'
```
