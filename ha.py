import requests

url = "https://a.asd.homes/home3/"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 15; RMX3890 Build/AQ3A.240812.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.122 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "",
  'upgrade-insecure-requests': "1",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "none",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'sec-ch-ua': "\"Android WebView\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'referer': "https://www.google.com/",
  'accept-language': "ar-EG,ar;q=0.9,en-EG;q=0.8,en-US;q=0.7,en;q=0.6",
  'if-modified-since': "Sat, 01 Nov 2025 08:37:50 GMT",
  'priority': "u=0, i",
  'Cookie': "dom3ic8zudi28v8lr6fgphwffqoz0j6c=48c7f70d-725d-441e-ade7-a09397ab82c7%3A3%3A1; _ga=GA1.1.473610218.1759183229; sb_main_6f4f5c3f5bfa5f5651799c658cb3556b=1; pp_main_6710543788e9f02584f3584d5416d1e3=1; pp_sub_6710543788e9f02584f3584d5416d1e3=1; sb_page_6f4f5c3f5bfa5f5651799c658cb3556b=3; sb_count_6f4f5c3f5bfa5f5651799c658cb3556b=4; _ga_D8NNSFR7SN=GS2.1.s1761986229$o21$g1$t1761986238$j51$l0$h0"
}

response = requests.get(url, headers=headers)

print(response.text)
