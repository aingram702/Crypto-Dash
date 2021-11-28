import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")
st.subheader("you can add more crypto in code </>")


# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Cardano = 'ADA-USD'
ShibaInu = 'SHIB-USD'
Dogecoin = 'DOGE-USD'
Uniswap = 'UNI3-USD'
Decentraland = 'MANA-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
ADA_Data = yf.Ticker(Cardano)
SHIB_Data = yf.Ticker(ShibaInu)
DOGE_Data = yf.Ticker(Dogecoin)
UNI_Data = yf.Ticker(Uniswap)
DEC_Data = yf.Ticker(Decentraland)

#Fetch history data from Yahoo Finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
ADAHis = ADA_Data.history(period="max")
SHIBHis = SHIB_Data.history(period="max")
DOGHis = DOGE_Data.history(period="max")
UNIHis = UNI_Data.history(period='max')
DECHis = DEC_Data.history(period='max')

# Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, period="max", interval="1d")
ETH = yf.download(Ethereum, period="max", interval="1d")
ADA = yf.download(Cardano, period="max", interval="1d")
SHIB = yf.download(ShibaInu, period="max", interval="1d")
DOGE = yf.download(Dogecoin, period="max", interval="1d")
UNI = yf.download(Uniswap, period="max", interval="1d")
DEC = yf.download(ShibaInu, period="max", interval="1d")

#Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
#Display image
st.image(imageBTC)
#Display dataframe
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)

#Ethereum
st.write("ETHEREUM ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
#Display image
st.image(imageETH)
#Display dataframe
st.table(ETH)
#Display a chart
st.bar_chart(ETHHis.Close)

#Cardano
st.write("CARDANO ($)")
imageADA = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'))
#Display image
st.image(imageADA)
#Display dataframe
st.table(ADA)
#Display a chart
st.bar_chart(ADAHis.Close)

#Shiba Inu
st.write("SHIBA INU ($)")
imageSHIB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png'))
#Display image
st.image(imageSHIB)
#Display dataframe
st.table(SHIB)
#Display a chart
st.bar_chart(SHIBHis.Close)

#Dogecoin
st.write("DogeCoin ($)")
imageDOGE = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'))
#Display image
st.image(imageDOGE)
#Display dataframe
st.table(DOGE)
#Display a chart
st.bar_chart(DOGHis.Close)

#Uniswap
st.write("Uniswap ($)")
imageUNI = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/7083.png'))
#Display image
st.image(imageUNI)
#Display dataframe
st.table(UNI)
#Display a chart
st.bar_chart(UNIHis.Close)

#Decentraland
st.write("Decentraland ($)")
imageDec = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1966.png'))
#Display image
st.image(imageDec)
#Display dataframe
st.table(DEC)
#Display a chart
st.bar_chart(DECHis.Close)