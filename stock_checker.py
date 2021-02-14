import csv
import main
my_stocks = ['t', 'atvi', 'amzn', 'aal', 'bac', 'brk-b', 'ba', 'bkng', 'net', 'ddog', 'docu', 'ea', 'fb', 'intc', 'jpm', 'jblu', 'ma', 'okta', 'pltr', 'pfe', 'work', 'luv', 'save', 'vtrs', 'v', 'dis', 'wfc', 'zm']
new_stocks = ["unit", "sq", "gm", "spot", "hubs"]
def stock_checker(list_of_stocks):
    header = ["company_name", "stock_price", "growth3m", "recommendation", "market_cap", "pe", "pb", "rev_growth", "ern_growth", "profit_margin", "debt2equity"]
    portfolio = []
    stock_list = []
    for stock in list_of_stocks:
        x = main.data(stock) #pulling data from Yahoo Finance API
        y = main.format_data(x) #formatting them to be readable when printed
        stock_list.append(x)
        portfolio.append(y)
    f = open("my_stocks.csv", "w")
    f_writer = csv.writer(f)
    f_writer.writerow(header)
    f_writer.writerows(portfolio)
    f.close()
    print(header)
    print(main.print_stock_list(stock_list))
    print("I SAVED THE OVERVIEW IN CSV TO YOUR CURRENT FOLDER") #facts about portfolio
    print(f"Average marker cap of your companies is {main.average_mar_cap(stock_list):,}")
    print(f"Your portfolio changed in the past 3 months by {main.three_months_avrg(stock_list):.2%}")
    print(f"Average PE of profitable (= {main.companies_with_pe(stock_list)}) companies in your portfolio is {main.average_pe(stock_list):,.2f}")
    print(f"{main.companies_with_pe(stock_list)} companies out of {len(stock_list)} from your portfolio are making profit ")
    print(f"Recommendations overview of your stocks: {main.recomendation(stock_list)}")
    return "OK"

print(stock_checker(new_stocks))