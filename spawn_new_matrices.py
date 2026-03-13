import os
import shutil

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

NEW_CITIES = {
    "hialeah-painting": "Hialeah",
    "homestead-painting": "Homestead",
    "north-miami-painting": "North Miami",
    "palmetto-bay-painting": "Palmetto Bay",
    "sunny-isles-beach-painting": "Sunny Isles Beach",
    "surfside-painting": "Surfside",
    "bal-harbour-painting": "Bal Harbour",
    "south-miami-painting": "South Miami",
    "miami-lakes-painting": "Miami Lakes",
    "sunset-painting": "Sunset"
}

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

def generate_matrices():
    for hub_folder, city in NEW_CITIES.items():
        for svc in SERVICES:
            src_file = os.path.join(BASE_DIR, svc, "index.html")
            dest_dir = os.path.join(BASE_DIR, hub_folder, svc)
            dest_file = os.path.join(dest_dir, "index.html")
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            shutil.copy2(src_file, dest_file)
            print(f"Spawned: /{hub_folder}/{svc}/")
            
if __name__ == '__main__':
    generate_matrices()
