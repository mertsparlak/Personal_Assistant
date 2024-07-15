import pyttsx3
import yfinance as yf
import cryptocompare
import requests
import api_keys as api



def get_crypto_symbols():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    data = response.json()
    crypto_dict = {item['name'].lower(): item['symbol'].upper() for item in data}
    return crypto_dict


def get_crypto_price(crypto_symbol):
    price = cryptocompare.get_price(crypto_symbol, currency='USD')[crypto_symbol]['USD']
    return price

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'][0]
    return price


# yapay zekaya hazırlattım 50 nasdaq 50 bist hissesi
stock_symbols = {
    "apple": "AAPL",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "alphabet (google)": "GOOGL",
    "facebook (meta)": "META",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "paypal": "PYPL",
    "comcast": "CMCSA",
    "pepsi": "PEP",
    "netflix": "NFLX",
    "adobe": "ADBE",
    "intel": "INTC",
    "cisco": "CSCO",
    "broadcom": "AVGO",
    "qualcomm": "QCOM",
    "costco": "COST",
    "t-mobile": "TMUS",
    "amd": "AMD",
    "booking": "BKNG",
    "starbucks": "SBUX",
    "zoom": "ZM",
    "paypal": "PYPL",
    "moderna": "MRNA",
    "netflix": "NFLX",
    "ebay": "EBAY",
    "autodesk": "ADSK",
    "vertex": "VRTX",
    "jd.com": "JD",
    "baidu": "BIDU",
    "micron": "MU",
    "docusign": "DOCU",
    "marriott": "MAR",
    "charter": "CHTR",
    "tesla": "TSLA",
    "splunk": "SPLK",
    "biogen": "BIIB",
    "monster": "MNST",
    "seagen": "SGEN",
    "baidu": "BIDU",
    "idexx": "IDXX",
    "intuitive": "ISRG",
    "regeneron": "REGN",
    "t-mobile": "TMUS",
    "lululemon": "LULU",
    "analog": "ADI",
    "docuSign": "DOCU",
    "paypal": "PYPL",
    "baidu": "BIDU",
    "airbnb": "ABNB",
    "zoom": "ZM",
    "akbank": "AKBNK",
    "garanti": "GARAN",
    "is bankasi": "ISCTR",
    "turkcell": "TCELL",
    "turk hava yolları": "THYAO",
    "bim": "BIMAS",
    "aseasan": "ASELS",
    "eregl": "EREGL",
    "tupras": "TUPRS",
    "koç holding": "KCHOL",
    "sasa polyester": "SASA",
    "yatirim finansman": "YATAS",
    "ford otosan": "FROTO",
    "kardemir": "KRDMD",
    "petkim": "PETKM",
    "vakifbank": "VAKBN",
    "sabanci holding": "SAHOL",
    "turkiye sigorta": "TURSG",
    "sok marketler": "SOKM",
    "torunlar gmyo": "TRGYO",
    "zorlu enerji": "ZOREN",
    "tekfen holding": "TKFEN",
    "migros": "MGROS",
    "akenerji": "AKENR",
    "alarko holding": "ALARK",
    "cimsa": "CIMSA",
    "dogus oto": "DOAS",
    "hektas": "HEKTS",
    "is gmyo": "ISGYO",
    "sasary": "SARKY",
    "tupras": "TUPRS",
    "turk telekom": "TTKOM",
    "ulker": "ULKER",
    "vestel": "VESTL",
    "yapi kredi": "YKBNK",
    "zorlu holding": "ZOREN",
    "ziraat": "ZZTK",
    "ag anadolu grubu": "AGHOL",
    "isiklar": "ISKPL",
    "mersin liman": "MRSHL",
    "oyak çimento": "OYAKC",
    "park elektrık": "PRKME",
    "tat gıda": "TATGD",
    "trakya cam": "TRKCM",
    "tukaş": "TUKAS",
    "turcas petrol": "TRCAS",
    "verusa": "VERUS",
    "yatirim holding": "YAYLA",
    "yeni hisar": "YENI",
    "albaraka türk": "ALBRK"
}