import requests

cookies = {
    'buvid3': '424D61C3-8690-F6C6-C695-6C1A50C22DA382725infoc',
    'b_nut': '1699520882',
    '_uuid': '3896B782-554B-CB5F-4E81-B83A9157D4F674634infoc',
    'enable_web_push': 'DISABLE',
    'header_theme_version': 'CLOSE',
    'rpdid': "|(~YRR~R|l)0J'uYmmY~m)mR",
    'DedeUserID': '1909782963',
    'DedeUserID__ckMd5': '23df1df488c2820b',
    'buvid4': 'FFABAAA2-B325-FFE2-A146-5533EF8CFB5184162-023110917-vXCzxafnl%2FrND6KHo%2BuRaQ%3D%3D',
    'buvid_fp_plain': 'undefined',
    'CURRENT_BLACKGAP': '0',
    'CURRENT_QUALITY': '80',
    'CURRENT_FNVAL': '4048',
    'FEED_LIVE_VERSION': 'V_HEADER_LIVE_NEW_POP',
    'PVID': '1',
    'fingerprint': 'c48dff21aeca800b220479018862f58d',
    'LIVE_BUVID': 'AUTO5517168988601520',
    'home_feed_column': '5',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk3NTgyOTYsImlhdCI6MTcxOTQ5OTAzNiwicGx0IjotMX0.xmNrdiIAxUZuwhrILRrKtId-GWf2QGIF0JSJxSAOUKk',
    'bili_ticket_expires': '1719758236',
    'SESSDATA': 'ed9c7e6b%2C1735051097%2Ceaf23%2A62CjBb6WHrz9oTC6K4MlpCCrRE1bqoAz4DpW5VpSD_Mo0nTnYblr6ptHdlV7o3yxiTU20SVnpOVjNOYnpSU19KRVBzSm9TeHREMENTclphSzRON3ZsbThTUmNtS0k3MHEzaU5kM2xpSHFUdUVqZmVHRlcxckhTeUxXWG1jcGhvbXVmVmtGbDdrTEpnIIEC',
    'bili_jct': 'b3d7065c5cabbd5ea7e3f5a52436af6d',
    'sid': 'qdrz1h78',
    'buvid_fp': '7f5efa6c387935831c230fb20a41d08c',
    'b_lsid': 'E101D4DB8_1905EF99098',
    'browser_resolution': '1536-776',
    'bp_t_offset_1909782963': '948081792567476224',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': "buvid3=424D61C3-8690-F6C6-C695-6C1A50C22DA382725infoc; b_nut=1699520882; _uuid=3896B782-554B-CB5F-4E81-B83A9157D4F674634infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; rpdid=|(~YRR~R|l)0J'uYmmY~m)mR; DedeUserID=1909782963; DedeUserID__ckMd5=23df1df488c2820b; buvid4=FFABAAA2-B325-FFE2-A146-5533EF8CFB5184162-023110917-vXCzxafnl%2FrND6KHo%2BuRaQ%3D%3D; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; CURRENT_QUALITY=80; CURRENT_FNVAL=4048; FEED_LIVE_VERSION=V_HEADER_LIVE_NEW_POP; PVID=1; fingerprint=c48dff21aeca800b220479018862f58d; LIVE_BUVID=AUTO5517168988601520; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk3NTgyOTYsImlhdCI6MTcxOTQ5OTAzNiwicGx0IjotMX0.xmNrdiIAxUZuwhrILRrKtId-GWf2QGIF0JSJxSAOUKk; bili_ticket_expires=1719758236; SESSDATA=ed9c7e6b%2C1735051097%2Ceaf23%2A62CjBb6WHrz9oTC6K4MlpCCrRE1bqoAz4DpW5VpSD_Mo0nTnYblr6ptHdlV7o3yxiTU20SVnpOVjNOYnpSU19KRVBzSm9TeHREMENTclphSzRON3ZsbThTUmNtS0k3MHEzaU5kM2xpSHFUdUVqZmVHRlcxckhTeUxXWG1jcGhvbXVmVmtGbDdrTEpnIIEC; bili_jct=b3d7065c5cabbd5ea7e3f5a52436af6d; sid=qdrz1h78; buvid_fp=7f5efa6c387935831c230fb20a41d08c; b_lsid=E101D4DB8_1905EF99098; browser_resolution=1536-776; bp_t_offset_1909782963=948081792567476224",
    'origin': 'https://search.bilibili.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://search.bilibili.com/all?keyword=%E7%88%AC%E8%99%AB&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=24',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'category_id': '',
    'search_type': 'video',
    'ad_resource': '5654',
    '__refresh__': 'true',
    '_extra': '',
    'context': '',
    'page': '2',
    'page_size': '42',
    'from_source': '',
    'from_spmid': '333.337',
    'platform': 'pc',
    'highlight': '1',
    'single_column': '0',
    'keyword': '爬虫',
    'qv_id': '0ZX1ReHvZc41MtQxOl1XPuSi4w9xXlLb',
    'source_tag': '3',
    'gaia_vtoken': '',
    'dynamic_offset': '24',
    'web_location': '1430654',
    'w_rid': 'ed3ccf90660c0bdf53d57a0e7edcb2f3',
    'wts': '1719580993',
}

response = requests.get(
    'https://api.bilibili.com/x/web-interface/wbi/search/type',
    params=params,
    cookies=cookies,
    headers=headers,
)

from pprint import pprint
pprint(response.json())