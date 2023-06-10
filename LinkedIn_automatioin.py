import requests
from linkedin import linkedin

client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "your_redirect_uri"

# Step 1: Get the authorization code
authorization_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=w_member_social"
print("Please authorize the application by visiting the following URL:")
print(authorization_url)

authorization_code = input("Enter the authorization code: ")

# Step 2: Exchange the authorization code for an access token
access_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri
}

response = requests.post(access_token_url, data=payload)
access_token = response.json()["access_token"]

print("Access token:", access_token)



access_token = "your_access_token"

application = linkedin.LinkedInApplication(token=access_token)

post_data = {
    "author": "urn:li:person:your_profile_id",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello, LinkedIn!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

application.submit_share(**post_data)
