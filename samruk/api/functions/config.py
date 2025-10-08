chrome_version = '140'


nav_string = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36"
    "20030107"
    "Netscape"
    "Mozilla"
)


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/json",
    "Origin": "https://zakup.sk.kz",
    "Referer": "https://zakup.sk.kz/",
    "Priority": "u=1, i",
    f"User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
    "Sec-CH-UA": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "App-Code-Name": "Mozilla",
    "App-Name": "Netscape",
    "Product-Sub": "20030107",
    "Language": "ru",
}

headers_put = {
    'Accept':'application/json, text/plain, */*',
    'App-Code-Name':'Mozilla',
    'App-Name':'Netscape',
    'Authorization':None,
    'Content-Type':'application/json',
    'Language':'ru',
    'E-tag':None,
    'sec-ch-ua-mobile':'?0',
    'Product-Sub':'20030107',
    'User-Agent':f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'host':'zakup.sk.kz',
    'tor':None,
}
