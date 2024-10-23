import requests

r = requests.get('http://172.25.0.29/index.php')

web_headers = r.headers
print('Here are the headers returned from the page:')
print(web_headers)

web_html = r.text 
print('Here is the HTML returned from the page:')
print(web_html)

web_status_code = r.status_code
print('Here is the HTTP status code returned from the page:')
print(web_status_code)

web_cookies = r.cookies
print('Here are the cookies returned from the page:')
print(web_cookies)