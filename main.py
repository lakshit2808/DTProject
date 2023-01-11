from Functions import *
import plotly.express as px

while(True):
    print("\n----- Fundamental Stock Analysis System -----\n")
    print("- Know the Stock Price [1]\n")
    print("- View Company's Balance Sheet [2]\n")
    print("- Get the Financial Statement of a Company [3]\n")
    print("- Know the Cash Flow of the Company [4]\n")
    print("- Know the Company's Objective [5]\n")
    print("- Number of Employees working at Company [6]\n")
    print("- Know Company's Contact Number [7]\n")
    print("- Company's Address[8]\n") 
    print("- View Quaterly Chart with High Low of a Stock [9]\n")
    print("- View 6 Months Chart with High Low of a Stock [10]\n")
    print("- View 1 Year's Chart with High Low of a Stock [11]\n")
    print("- View 5 Year's Chart with High Low of a Stock [12]\n")

    print("Symbols to Try: AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA, ORCL, IBM\n")
    try:
        n = int(input("Enter Number [1 - 12] | type exit/EXIT to quit the program: "))

        while(n < 1 or n > 12):
            print("\nInvalid Input try again")
            n = int(input("Enter Number [1 - 12] | type exit/EXIT to quit the program: "))
    except:
        ex = input("Do you want to Exit the Program?[y/n]: ")
        if ex == 'y':
            break
        else:
            continue

    try:
        match n:
            case 1:
                print("\nStock Price Viewer\n")
                stock_symbol = input("Enter a Stock Symbol e.g AAPL: ").upper()
                print("\n")
                print(get_stockprice(stock_symbol))
            case 2:
                print("\nBalance Sheet Viewer\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(get_balancesheet(stock_symbol))
            case 3:
                print("\nFinancial Statement of a Company\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(get_financials(stock_symbol))
            case 4:
                print("\nCash Flow of a Company\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(get_cashflow(stock_symbol))
            case 5:
                print("\nCompany Objective\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(get_companyinfo(stock_symbol,"longBusinessSummary"))
            case 6:
                print("\nNumber of Employees at Company\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(f"Number of Employees working at {stock_symbol} are {get_companyinfo(stock_symbol,'fullTimeEmployees')}")
            case 7:
                print("\nPhone Number of Company\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(f"Phone Number of {stock_symbol} is {get_companyinfo(stock_symbol,'phone')}")

            case 8:
                print("\nCompany's Address\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                print("\n")
                print(f"{stock_symbol} is located at {get_companyinfo(stock_symbol,'address1')}, {get_companyinfo(stock_symbol,'city')}, {get_companyinfo(stock_symbol,'state')}, {get_companyinfo(stock_symbol,'country')}, {get_companyinfo(stock_symbol,'zip')}")  
            case 9:
                print("\nView Quaterly Chart\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                fig = px.line(get_quaterly_data(stock_symbol), y="Adj Close", title=f"{stock_symbol} | {get_quaterly_high_low(stock_symbol)}")
                fig.show()   
            case 10:
                print("\nView 6 Month's Chart\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                fig = px.line(get_6months_data(stock_symbol), y="Adj Close", title=f"{stock_symbol} | {get_6months_high_low(stock_symbol)}")
                fig.show() 
            case 11:
                print("\nView 1 Year's Chart\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                fig = px.line(get_1year_data(stock_symbol), y="Adj Close", title=f"{stock_symbol} | {get_1year_high_low(stock_symbol)}")
                fig.show()    
            case 12:
                print("\nView 5 Years Chart\n")
                stock_symbol = input("Enter a Company's Symbol e.g TSLA: ").upper()
                fig = px.line(get_5years_data(stock_symbol), y="Adj Close", title=f"{stock_symbol} | {get_5years_high_low(stock_symbol)}")
                fig.show()
    except:
        print("Invalid Symbol Try Again")