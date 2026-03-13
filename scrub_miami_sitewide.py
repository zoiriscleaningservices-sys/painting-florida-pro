import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

HUBS = {
    "coral-gables-painting": "Coral Gables",
    "miami-beach-painting": "Miami Beach",
    "brickell-painting": "Brickell",
    "coconut-grove-painting": "Coconut Grove"
}

def scrub_m(text, city):
    # Safe shields first
    text = text.replace("Miami-Dade", "___MIAMIDADE___")
    text = text.replace("MIAMI-DADE", "___MIAMIDADE_UPPER___")
    
    # Shield Miami Beach because if city = Coral Gables, we don't want "Coral Gables Beach"
    text = text.replace("Miami Beach", "___MIAMIBEACH___")
    text = text.replace("MIAMI BEACH", "___MIAMIBEACH_UPPER___")
    text = text.replace("miami-beach", "___MIAMIBEACH_LOWER___")
    
    # Shield lowercase miami to avoid breaking URLs or image IDs
    # e.g. <img src="...miami...">
    # However we don't have many lowercase miamis in text. Let's shield to be safe
    # Wait, we can just use regex \bMiami\b and \bMIAMI\b which are case-sensitive!
    
    # Let's replace uppercase MIAMI first
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
                    if new_content != content:
                        with open(idx, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_updated += 1
                        
    print(f"Aggressively scrubbed Miami from {files_updated} localized files.")

if __name__ == '__main__':
    run()
