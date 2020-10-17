import requests
from fake_useragent import UserAgent

ua=UserAgent(verify_ssl=False)
print(f'浏览器:{ua.chrome}')

header={'user_agent':ua.random}
url='https://www.shicimingju.com/book/shiji.html'
response=requests.get(url,headers=header)
print(response.text)

