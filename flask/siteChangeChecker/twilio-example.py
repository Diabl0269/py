from twilio.rest import Client
from client import *

# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)

if __name__ == "__main__":
    while True:
        print("Checking site")
        new_site = check_site()

        if old_site != "" and old_site != new_site:
            client.messages \
                .create(
                body="Site has changed",
                from_='+123456789',
                to='+123456789'
            )
            print("Site has changed!")

        old_site = new_site
        time.sleep(5)
