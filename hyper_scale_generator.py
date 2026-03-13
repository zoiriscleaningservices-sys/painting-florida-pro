import os
import shutil
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
SOURCE_FILE = os.path.join(BASE_DIR, "index.html")
LOC_FILE = os.path.join(BASE_DIR, "south_florida_locations.txt")

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

def scrub_m(text, city_name):
    """Aggressively replaces instances of 'Miami' with the specific loc name."""
    text = text.replace("Miami-Dade", "___MIAMIDADE___")
    text = text.replace("MIAMI-DADE", "___MIAMIDADE_UPPER___")
    text = text.replace("Miami Beach", "___MIAMIBEACH___")
    
    text = re.sub(r'\bMIAMI\b', city_name.upper(), text)
    text = re.sub(r'\bMiami\b', city_name, text)
    
    text = text.replace("___MIAMIDADE___", "Miami-Dade")
    text = text.replace("___MIAMIDADE_UPPER___", "MIAMI-DADE")
    text = text.replace("___MIAMIBEACH___", "Miami Beach")
    
    return text

def build_hyper_scale():
    # 1. Load Locations
    with open(LOC_FILE, 'r', encoding='utf-8') as f:
        raw_cities = f.read().splitlines()
        
    print(f"Loaded {len(raw_cities)} target locations...")
    
    # Pre-read source index template
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        master_idx = f.read()

    # Pre-read the 8 service templates from root
    service_templates = {}
    for svc in SERVICES:
        tpath = os.path.join(BASE_DIR, svc, "index.html")
        with open(tpath, 'r', encoding='utf-8') as f:
            service_templates[svc] = f.read()
            
    hubs_created = 0
    pages_created = 0
    
    # Skip locations we already generated manually earlier (e.g. coral-gables-painting, aventrua-painting, etc)
    EXISTING_HUBS = [
        "coral-gables", "miami-beach", "brickell", "coconut-grove",
        "aventura", "pinecrest", "doral", "key-biscayne", "kendall", "wynwood",
        "hialeah", "homestead", "north-miami", "palmetto-bay", "sunny-isles-beach",
        "surfside", "bal-harbour", "south-miami", "miami-lakes", "sunset"
    ]
    
    for city_name in raw_cities:
        if not city_name.strip(): continue
        
        folder_name = city_name.lower().replace(" ", "-") + "-painting"
        
        if any(folder_name.startswith(xhub) for xhub in EXISTING_HUBS):
            continue # We already built these thoroughly.

        hub_path = os.path.join(BASE_DIR, folder_name)
        
        if not os.path.exists(hub_path):
            os.makedirs(hub_path)
            
        # A. BUILD HUB INDEX
        target_file = os.path.join(hub_path, "index.html")
        
        content = master_idx
        content = content.replace("<title>Painting Florida Pros | Miami's Premier Painting Contractors</title>", 
                                  f"<title>Painting Contractors {city_name} FL | Residential & Commercial Experts</title>")
        content = content.replace('content="Top-rated residential and commercial painting contractors in Miami. Specializing in high-end interior, exterior, and protective coatings against humidity."',
                                  f'content="Top-rated residential and commercial painting contractors in {city_name} FL. Specializing in high-end interior, exterior, and protective coatings against humidity."')
        content = content.replace('"name": "Painting Florida Pros - Miami Headquarters",', f'"name": "Painting Florida Pros - {city_name} Branch",')
        content = content.replace('"addressLocality": "Miami",', f'"addressLocality": "{city_name}",')
        content = content.replace('"url": "https://paintingfloridapros.com",', f'"url": "https://paintingfloridapros.com/{folder_name}/",')
        
        content = content.replace("MIAMI'S ELITE PAINTING CONTRACTORS", f"{city_name.upper()}'S ELITE PAINTING CONTRACTORS")
        content = content.replace("Florida's Premier<br />", "PREMIER<br />")
        content = content.replace('Painting <span className="text-gradient">Contractors</span> <br />\n                                    in Miami.', 
                                  f'PAINTING <span className="text-gradient">CONTRACTORS</span> <br />\n                                    IN {city_name.upper()}.')
        content = scrub_m(content, city_name)
        
        # Wire Silo inside the Hub Index
        for svc in SERVICES:
            content = content.replace(f'href="/{svc}/"', f'href="/{folder_name}/{svc}/"')
            
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        pages_created += 1

        # B. BUILD 8 NESTED SERVICES
        for svc in SERVICES:
            svc_dir = os.path.join(hub_path, svc)
            if not os.path.exists(svc_dir):
                os.makedirs(svc_dir)
                
            svc_content = service_templates[svc]
            svc_content = scrub_m(svc_content, city_name)
            svc_content = svc_content.replace('OUR EXPERTISE', f"{city_name.upper()}'S EXPERTISE")
            svc_content = svc_content.replace(f"Painting Florida Pros - {city_name} Headquarters", f"Painting Florida Pros - {city_name} Branch")
            
            # Wire linking
            for inner_svc in SERVICES:
                svc_content = svc_content.replace(f'href="/{inner_svc}/"', f'href="/{folder_name}/{inner_svc}/"')
            svc_content = svc_content.replace('href="/"', f'href="/{folder_name}/"')
            
            svc_target = os.path.join(svc_dir, "index.html")
            with open(svc_target, 'w', encoding='utf-8') as f:
                f.write(svc_content)
                
            pages_created += 1
            
        hubs_created += 1
        if hubs_created % 50 == 0:
            print(f"Status: Built {hubs_created} hubs ({pages_created} pages)...")

    print(f"\n✅ GENERATION COMPLETE")
    print(f"Successfully spawned {hubs_created} local city hubs.")
    print(f"Successfully deployed {pages_created} tightly-woven SEO HTML files.")

if __name__ == '__main__':
    build_hyper_scale()
