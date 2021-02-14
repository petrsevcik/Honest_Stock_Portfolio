from yahooquery import Ticker
import datetime
import csv
#goal: prepare a script which will monitor stock portfolio and prepare overview into csv. Similar structure like https://www.macrotrends.net/stocks/stock-screener
#input format: List of tickers
# output - short comment about portfolio and full overview will save in csv to current folder. Structure of csv - Header [Ticker, company_name, stock_price,recommendation, market_cap, quarter_change, P/E, P/B, revenue_growth, earnings_growth, profit_margin, debt_equity]
#my_stocks = ['t', 'atvi', 'amzn', 'aal', 'bac', 'brk-b', 'ba', 'bkng', 'net', 'ddog', 'docu', 'ea', 'fb', 'intc', 'jpm', 'jblu', 'ma', 'okta', 'pltr', 'pfe', 'work', 'luv', 'save', 'vtrs', 'v', 'dis', 'wfc', 'zm']
#test_stocks = ["amzn", "fb"]
#stocks = ['zm', 'bac', 'ddog', 'nflx', 'goog']
def data(ticker): #pulling data about stock from Yahoo Finance API
    try:
        company_name = Ticker(ticker).quote_type[ticker]["shortName"]
    except KeyError:
        company_name = 0
    try:
        stock_price = Ticker(ticker).financial_data[ticker]["currentPrice"]
    except KeyError:
        stock_price = 0
    try:
        change = Ticker(ticker).history(interval='1mo', start=(datetime.datetime.today() - datetime.timedelta(days=90)), end=datetime.datetime.today())
        change = change["open"]
        growth_or_loose = ((change.iloc[-1] / change.iloc[0]) - 1)
    except:
        growth_or_loose = 0
    try:
        recommendation = Ticker(ticker).financial_data[ticker]["recommendationKey"]
    except KeyError:
        recommendation = 0
    try:
        market_cap = Ticker(ticker).summary_detail[ticker]["marketCap"]
    except KeyError:
        market_cap = 0
    #quarter_change =
    try:
        pe = Ticker(ticker).summary_detail[ticker]["trailingPE"]
    except KeyError:
        pe = 0
    try:
        pb = Ticker(ticker).key_stats[ticker]["priceToBook"]
    except KeyError:
        pb = 0
    try:
        rev_growth = Ticker(ticker).financial_data[ticker]["revenueGrowth"]
    except KeyError:
        rev_growth = 0
    try:
        ern_growth = Ticker(ticker).financial_data[ticker]["earningsGrowth"]
    except KeyError:
        ern_growth = 0
    profit_margin = Ticker(ticker).financial_data[ticker]["profitMargins"]
    try:
        debt2equity = Ticker(ticker).financial_data[ticker]["debtToEquity"]
    except KeyError:
        debt2equity = 0
    data =  company_name, stock_price, growth_or_loose,  recommendation, market_cap, pe, pb, rev_growth, ern_growth, profit_margin, debt2equity
    return list(data)

def format_data(data): #formating stock data to more readable format
    try:
        company_name = data[0]
    except ValueError:
        company_name = 0
    try:
        stock_price = str(data[1]) + "$"
    except ValueError:
        stock_price = 0
    try:
        growth_or_loose = f"{data[2]:.2%}"
    except ValueError:
        growth_or_loose = 0
    try:
        recommendation = data[3].upper()
    except ValueError:
        recommendation = 0
    try:
        market_cap = f"{data[4]:,}"
    except ValueError:
        market_cap = 0
    try:
        pe = f"{data[5]:,.2f}"
    except ValueError:
        pe = 0
    try:
        pb = f"{data[6]:,.2f}"
    except ValueError:
        pb = 0
    try:
        rev_growth = f"{data[7]:.2%}"
    except ValueError:
        rev_growth = 0
    try:
        ern_growth = f"{data[8]:.2%}"
    except ValueError:
        ern_growth = 0
    try:
        profit_margin = f"{data[9]:.2%}"
    except ValueError:
        profit_margin = 0
    try:
        debt2equity = f"{data[10]:,.2f}"
    except ValueError:
        debt2equity = 0
    new_format = company_name, stock_price, growth_or_loose, recommendation, market_cap, pe, pb, rev_growth, ern_growth, profit_margin, debt2equity
    return list(new_format)

def create_sotck_list(stocks):
    stock_list = []
    for stock in stocks:
        stock_list.append(data(stock))
    return stock_list

def average_mar_cap(stock_list): #average market cap of companies in poftfolio (not very valid data)
    average = []
    for stock in stock_list:
        average.append(stock[4])
    avrg_mar_cap = (sum(average) / len(average))
    return avrg_mar_cap

def three_months_avrg(stock_list): #3 months average growth = how your portfolio performed - counting with 1 stock per company.
    average3m = []
    for stock in stock_list:
        average3m.append(stock[2])
    avrg_thr_mon = (sum(average3m) / len(average3m))
    return avrg_thr_mon

def average_pe(stock_list): #average PE of companies making profit
    averagepe = []
    for stock in stock_list:
        if (float(stock[5])) > 0:
            averagepe.append(float(stock[5]))
        else:
            pass
    avrg_pe = (sum(averagepe)/len(averagepe))
    return avrg_pe

def companies_with_pe(stock_list): #how many companies are profitable in your portfolio
    averagepe = []
    for stock in stock_list:
        if (float(stock[5])) > 0:
            averagepe.append(float(stock[5]))
        else:
            pass
    comp_with_pe = len(averagepe)
    return comp_with_pe

def recomendation(stock_list): #dictionary with count of recomendations
    recomendations = []
    for stock in stock_list:
        recomendations.append(stock[3])
    output = {}
    for rec in recomendations:
        if rec in output.keys():
            output[rec] = output[rec]+1
        else:
            output[rec] = 1
    return output

def print_stock_list(stock_list):
    for stock in stock_list:
        print(format_data(stock))







