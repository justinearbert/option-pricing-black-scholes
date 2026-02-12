
import yfinance as yf 
import numpy as np

def historical_volatility(ticker,start_date,end_date):
    #1.Telecharger les données de prix de cloture ajustés 
    data = yf.download(ticker,start=start_date, end=end_date)
    close_prices = data["Adj Close"]

    #2.Calculer les rendements journaliers en log
    log_returns = np.log(close_prices/close_prices.shift(1)).dropna()

    #3.Volatilité quotidienne = ecart-type des rendements journaliers 
    daily_vol = log_returns.std().item()

    #4.Annualiser la volatilité (252 jours de bourse par an)
    annual_vol = daily_vol*np.sqrt(252)

    return annual_vol,log_returns

#exemple 

if __name__ == "__main__":
    ticker = "AAPL" #apple 
    start_date = "2023-06-01"
    end_date = "2023-12-31"

    vol_annuelle,log_returns= historical_volatility(ticker,start_date,end_date)
print(f"Volatilité historique annualisée de AAPL : {vol_annuelle:.2%}")


