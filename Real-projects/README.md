
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

#### Python program: Calculate the intrinsic value of a stock
- Initial implementation
- - calculate_intrinsic_value, given EPS and expected growth rate (i.e. Forward EPS long term growth (3-5 yrs))
- Modify to add result to an output file
- Add a function to compute "Margin of Safety", given a stock's current market price (e.g. AAPL $249.54 as of 10/15)
- - Investment Analysis:
- - - Fairly valued (zero margin of safety)
- - - Undervalued (positive margin of safety) - Good buying opportunity
- - - Overvlued (negative margin of safety) - Potentially too expensive
