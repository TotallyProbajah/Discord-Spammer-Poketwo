from webserver import keep_alive
import requests

channelID = 1190669840957063272
headers = {
    "authorization":
    "OTUzODYxMDI2NDYwMzQ4NDU2.YjKuzA.2e7wsCTk6S2gJHKR7IcGPgarf9w"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
