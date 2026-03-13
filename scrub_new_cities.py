import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

HUBS = {
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

def scrub_m(text, city):
    # Safe shields first
    text = text.replace("Miami-Dade", "___MIAMIDADE___")
    text = text.replace("MIAMI-DADE", "___MIAMIDADE_UPPER___")
    text = text.replace("Miami Beach", "___MIAMIBEACH___")
    text = text.replace("MIAMI BEACH", "___MIAMIBEACH_UPPER___")
    text = text.replace("miami-beach", "___MIAMIBEACH_LOWER___")
    
    # Replace uppercase MIAMI first
    text = re.sub(r'\bMIAMI\b', city.upper(), text)
    # Then title-case Miami
    text = re.sub(r'\bMiami\b', city, text)
    
    # Restore shields
    text = text.replace("___MIAMIDADE___", "Miami-Dade")
    text = text.replace("___MIAMIDADE_UPPER___", "MIAMI-DADE")
    text = text.replace("___MIAMIBEACH___", "Miami Beach")
    text = text.replace("___MIAMIBEACH_UPPER___", "MIAMI BEACH")
    text = text.replace("___MIAMIBEACH_LOWER___", "miami-beach")
    
    return text

def run():
    files_updated = 0
    for hub, city in HUBS.items():
        # Scour the hub index
        hub_idx = os.path.join(BASE_DIR, hub, "index.html")
        if os.path.exists(hub_idx):
            with open(hub_idx, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = scrub_m(content, city)
            
            # Since these were cloned directly from the ROOT files, they still hold exact matches to patch:
            new_content = new_content.replace(f"Painting Florida Pros - {city} Headquarters", f"Painting Florida Pros - {city} Branch")
            
            if new_content != content:
                with open(hub_idx, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                
        # Scour sub-services
        for svc in os.listdir(os.path.join(BASE_DIR, hub)):
            svc_path = os.path.join(BASE_DIR, hub, svc)
            if os.path.isdir(svc_path):
                idx = os.path.join(svc_path, "index.html")
                if os.path.exists(idx):
                    with open(idx, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = scrub_m(content, city)
                    
                    # Fix deep_localize specific patterns that might have been missed by strict word replace
                    new_content = new_content.replace('OUR EXPERTISE', f"{city.upper()}'S EXPERTISE")
                    
                    if new_content != content:
                        with open(idx, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_updated += 1
                        
    print(f"Aggressively scrubbed target keywords from {files_updated} newly generated localized files.")

if __name__ == '__main__':
    run()
