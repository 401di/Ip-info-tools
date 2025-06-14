import requests
import os
import time

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("""
╔════════════════════════════════╗
║      🛰️  IP INFO TOOL - v1      ║
║            by 401 😎           ║
╚════════════════════════════════╝
""")

def get_ip_info(ip=None):
    try:
        url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
        res = requests.get(url)
        data = res.json()

        print("📡 Résultat IP:\n")
        print(f"🌐 IP           : {data.get('ip', 'N/A')}")
        print(f"📍 Ville        : {data.get('city', 'N/A')}")
        print(f"🏙️  Région       : {data.get('region', 'N/A')}")
        print(f"🌍 Pays         : {data.get('country', 'N/A')}")
        print(f"📌 Localisation : {data.get('loc', 'N/A')}")
        print(f"🏢 Organisation : {data.get('org', 'N/A')}")
        print(f"⏰ Timezone     : {data.get('timezone', 'N/A')}")
        print(f"🔗 Hostname     : {data.get('hostname', 'N/A')}\n")

    except Exception as e:
        print(f"❌ Erreur : {e}")

def main():
    while True:
        clear()
        banner()
        print("1️⃣  Scanner mon IP")
        print("2️⃣  Scanner une IP cible")
        print("3️⃣  Quitter")
        choix = input("\n👉 Choix : ")

        if choix == '1':
            get_ip_info()
            input("\n🔁 Appuie sur Entrée pour revenir au menu...")
        elif choix == '2':
            ip = input("💡 Entre une IP cible : ")
            get_ip_info(ip)
            input("\n🔁 Appuie sur Entrée pour revenir au menu...")
        elif choix == '3':
            print("👋 À bientôt frérot !")
            time.sleep(1)
            break
        else:
            print("❗ Choix invalide")
            time.sleep(1)

if __name__ == "__main__":
    main()
