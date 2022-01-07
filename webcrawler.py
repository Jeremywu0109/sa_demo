import requests
web_url='https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f'
r = requests.get(web_url)
with open('./路外停車資訊.json','wb') as f:
  f.write(r.content)