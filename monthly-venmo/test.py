from venmo_api import Client
client = Client(access_token="c72fd7e8b20cdafcfcea3634e0b094e9a047f3fdd356c288605d3b3f58066ab5")

# Search for users. You get a maximum of 50 results per request.

# Or pass a callback to make it multi-threaded
def callback(users):
   for user in users:
       print(user.username)

client.user.search_for_users(query="Frumin",
                            callback=callback,
                            limit=10)
