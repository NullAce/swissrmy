import requests
from sys import argv

page = requests.get(f'{argv[1]}')

print('Here are the headers returned from the page:')
print(page.headers)

print("", end="\n\n")

print('Here is the HTML returned from the page:')
print(page.txt)

print("", end="\n\n")

print('Here is the HTTP status code returned from the page:')
print(page.status_code)

print("", end="\n\n")

print('Here are the cookies returned from the page:')
print(page.cookies)
