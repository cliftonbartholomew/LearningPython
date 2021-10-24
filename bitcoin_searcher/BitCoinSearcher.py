import json
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()




def save_coins_to_file(file):
    f = open(file, "w", encoding="utf-8")

    for i in range(20):
        #https://github.com/man-c/pycoingecko/blob/8b7a8451cc8911eff5a7f268c885da4bc1570c3f/pycoingecko/api.py#L111
        #https://www.coingecko.com/en/api
        #above links show how gecko api works
        list = cg.get_coins_markets(vs_currency= "usd", per_page=250, page=i)
        for coin in list:
            #json dumps formats the dictionary to print one key:value pair per line
            #instead of all on one line.
            #f.write(json.dumps(coin,sort_keys=False, indent=4) + "\n\n")
            #print(coin["market_cap_rank"])
            if(coin["market_cap_rank"] != None):
                if(coin["market_cap"]*0.0001 < 1000 and coin["market_cap_rank"] < 1000 and coin["market_cap_rank"] > 200):
                    print(coin["symbol"] + str(coin["market_cap_rank"]) + "\n")


    f.close()


save_coins_to_file("coins.txt")
