def basicScraper(url):
    
    from requests import get
    from bs4 import BeautifulSoup
    import json
    import pandas as pd

    # match_timelinedelta

    from datetime import datetime
    now = datetime.now().strftime("%H:%M:%S")
    print(now)

    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #json_data = str(soup)
    #loaded = json.loads(json_data)
    #doc_data = loaded['doc'][0]['data']
    
    return soup
    