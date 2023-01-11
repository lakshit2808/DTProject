from yahoo_fin import stock_info
import yfinance as yf
import yfinance as finance
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_stockprice(symbol):
    stock_price = round(stock_info.get_live_price(symbol),2)
    return f"{symbol} stock price is {stock_price}"

def get_balancesheet(symbol):
    balancesheet = finance.Ticker(symbol).balance_sheet
    return balancesheet

def get_financials(symbol):
    financials = finance.Ticker(symbol).financials
    return financials

def get_cashflow(symbol):
    cashflow = finance.Ticker(symbol).cashflow
    return cashflow

def get_companyinfo(symbol, toknow):
    info = finance.Ticker(symbol).get_info()
    return info[toknow]

def get_quaterly_high_low(symbol):
  qtr = datetime.now() - relativedelta(months = 3)
  data = yf.download(symbol,qtr.date())
  print('\n')
  return f"{symbol}'s Quaterly High is {round(data['High'].max(), 2)} and Low is {round(data['Low'].min(), 2)}"

def get_6months_high_low(symbol):
  qtr = datetime.now() - relativedelta(months = 6)
  data = yf.download(symbol,qtr.date())
  print('\n')
  return f"{symbol}'s Quaterly High is {round(data['High'].max(), 2)} and Low is {round(data['Low'].min(), 2)}"

def get_1year_high_low(symbol):
  qtr = datetime.now() - relativedelta(years = 1)
  data = yf.download(symbol,qtr.date())
  print("\n")
  return f"{symbol}'s Quaterly High is {round(data['High'].max(), 2)} and Low is {round(data['Low'].min(), 2)}"

def get_5years_high_low(symbol):
  qtr = datetime.now() - relativedelta(years = 5)
  data = yf.download(symbol,qtr.date())
  print("\n")
  return f"{symbol}'s Quaterly High is {round(data['High'].max(), 2)} and Low is {round(data['Low'].min(), 2)}"

def get_5years_data(name):
  qtr = datetime.now() - relativedelta(years = 5)
  data = yf.download(name,qtr.date())
  return data['Adj Close']

def get_1year_data(name):
  qtr = datetime.now() - relativedelta(years = 1)
  data = yf.download(name,qtr.date())
  return data['Adj Close']

def get_6months_data(name):
  qtr = datetime.now() - relativedelta(months= 6)
  data = yf.download(name,qtr.date())
  return data['Adj Close']

def get_quaterly_data(name):
  qtr = datetime.now() - relativedelta(months= 3)
  data = yf.download(name,qtr.date())
  return data['Adj Close']