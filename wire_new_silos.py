import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# The 10 NEW local Hubs
HUBS = [
    "hialeah-painting",
    "homestead-painting",
    "north-miami-painting",
    "palmetto-bay-painting",
    "sunny-isles-beach-painting",
    "surfside-painting",
    "bal-harbour-painting",
    "south-miami-painting",
    "miami-lakes-painting",
    "sunset-painting"
]

SERVICES = [
    "residential-painting",
    "commercial-painting",
    "exterior-painting",
    "cabinet-refinishing",
    "interior-painting",
    "epoxy-flooring",
    "pressure-washing",
    "drywall-repair"
]

def wire_new_silos():
    for hub in HUBS:
        hub_path = os.path.join(BASE_DIR, hub)
        
        if not os.path.exists(hub_path):
            continue

        # 1. Wire the Hub Index file
        hub_idx = os.path.join(hub_path, "index.html")
        if os.path.exists(hub_idx):
            with open(hub_idx, 'r', encoding='utf-8') as f:
                content = f.read()

            # Rewrite top-level service links to point inside the hub
            for svc in SERVICES:
                # content = content.replace(f'href="/{svc}/"', f'href="/{hub}/{svc}/"') # Already replaced previously
                # Actually, these pages are cloned from root where links are `href="/residential-painting/"`
                content = content.replace(f'href="/{svc}/"', f'href="/{hub}/{svc}/"')
                content = content.replace(f"href='/{svc}/'", f"href='/{hub}/{svc}/'")

            with open(hub_idx, 'w', encoding='utf-8') as f:
                f.write(content)

        # 2. Wire the 8 nested service files
        for svc in SERVICES:
            svc_path = os.path.join(hub_path, svc, "index.html")
            
            if not os.path.exists(svc_path):
                continue

            with open(svc_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Fix all cross-links between services
            for inner_svc in SERVICES:
                content = content.replace(f'href="/{inner_svc}/"', f'href="/{hub}/{inner_svc}/"')
                content = content.replace(f"href='/{inner_svc}/'", f"href='/{hub}/{inner_svc}/'")

            # Fix the return-to-hub link
            content = content.replace('href="/"', f'href="/{hub}/"')

            with open(svc_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Wired completely insulated Silo: /{hub}/{svc}/")

if __name__ == "__main__":
    wire_new_silos()
