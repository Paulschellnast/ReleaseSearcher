#better use libtorrent :)
from qbittorrent import Client
import requests
import time

qb = Client('http://127.0.0.1:8080/')

search_url = 'https://api.xrel.to/v2/search/releases.json'
error_20 = {'error': 'No results found', 'error_code': 20}
xrel_error = {'total': 0, 'results': []}

def downloader():
    qb.login

print("1: Search for releases and magnet links")

y = input("Choose option: ")

if y == "1":
    keyword = input("Enter search term:")
    keyword_ = keyword.replace(" ", "_")
    
    
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
    time.sleep(1)
    ms = requests.get('https://torrentapi.org/pubapi_v2.php?app_id=DIEAPPID&mode=search&search_string='+keyword_+'&token='+id, headers=headers).json()
    if ms == error_20:
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
        
        #Download
        u = input("Download this Torrent? Press 1 to download.")
        
        if(u == "1") :
            downloader()
            qb.download_from_link(ms["torrent_results"][0]["download"])
            time.sleep(10)
            print(qb.torrents())
        

        
    
    
