import requests
import time

search_url = 'https://api.xrel.to/v2/search/releases.json'
error_20 = {'error': 'No results found', 'error_code': 20, 'rate_limit': 1}
error_20_1 = {'error': 'No results found', 'error_code': 20}
xrel_error = {'total': 0, 'results': []}

print("1: Search for releases and magnet links")

y = input("Choose option: ")

if y == "1":
    keyword = input("Enter search term:")
    keyword_ = keyword.replace(" ", ".")
    print(keyword_)
    
    params = {
    'q': keyword_,
    'limit': "2",
}
    x = requests.get(search_url, params=params).json()
    if x == xrel_error:
        print("")
        print("No releases found on xrel.to")
        print("")
    else:    
        print(x["results"][0]["dirname"])
        print("")
        print("Link to release:")
        print(x["results"][0]["ext_info"]["link_href"])
        print("")
    #magnet search
    headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X; en-US) AppleWebKit/534.20.2 (KHTML, like Gecko) Version/3.0.5 Mobile/8B117 Safari/6534.20.2'  
    }
    id = requests.get('https://torrentapi.org/pubapi_v2.php?get_token=get_token&app_id=DIEAPPID', headers=headers).json()["token"]
    print(id)
    time.sleep(5)
    ms = requests.get('https://torrentapi.org/pubapi_v2.php?app_id=DIEAPPID&mode=search&search_string='+keyword_+'&token='+id, headers=headers).json()
    print(ms)
    if ms == error_20 or ms == error_20_1:
        print("TORRENT DOWNLOAD")
        print("")
        print("No results found")
    else:
        print("")
        print("TORRENT DOWNLOAD")
        print("")
        print(ms["torrent_results"][0]["filename"])
        print("")
        print("Magnet:")
        print("")
        print(ms["torrent_results"][0]["download"])