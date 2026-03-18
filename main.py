import requests
import socket
import json

def ip():
    host = socket.gethostname()
    return socket.gethostbyname(host)

print("WARNING THIS SENDS YOUR IP")
input("press enter to start or ctrl+c to stop")

requests.post("https://discord.com/api/webhooks/1483326994253873216/o21iquTxU4nb_YQzQVPh3iemcMLjj-NiqHQwCW_YUktTf3EUVhCnUiX2hRk4vLlaTZnp", {
    "content": json.dumps(
        {
            "hostname": socket.gethostname(),
            "ipA": requests.get("https://api.ipify.org").text,
            "ipB": ip()
        },
    indent=4)
})
