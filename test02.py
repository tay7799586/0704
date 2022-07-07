import requests
url="https://www.nkust.edu.tw/p/403-1000-1363-1.php"
html=requests.get(url).text
print(html)