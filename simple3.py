import requests, sys, json, uuid, time, os
from colorama import init, Fore, Back, Style

os.system('cls' if os.name=='nt' else 'clear')
init(autoreset=True)  # Initialize colorama
API="https://zefame-free.com/api_free.php?action=config"

video_id = "7559620502021606664"
video_link = "https://vt.tiktok.com/ZSynJ4R2N/"
selected = "3"
data = requests.get("https://zefame-free.com/api_free.php?action=config").json()
services = data.get('data', {}).get('tiktok', {}).get('services', [])
selected = services[4]

order = requests.post("https://zefame-free.com/api_free.php?action=order", data={"service": selected.get('id'), "link": video_link, "uuid": str(uuid.uuid4()), "videoId": video_id})
result = order.json()
print(f"{Fore.GREEN}{json.dumps(result, separators=(',',':'))}{Style.RESET_ALL}")
