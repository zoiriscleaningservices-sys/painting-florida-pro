import os
import shutil

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
SOURCE_FILE = os.path.join(BASE_DIR, "index.html")

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

def build_hubs():
    for folder, city_name in NEW_CITIES.items():
        hub_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(hub_path):
            os.makedirs(hub_path)
            
        target_file = os.path.join(hub_path, "index.html")
        shutil.copy2(SOURCE_FILE, target_file)
        
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Title & Meta
        content = content.replace("<title>Painting Florida Pros | Miami's Premier Painting Contractors</title>", 
                                  f"<title>Painting Contractors {city_name} FL | Residential & Commercial Experts</title>")
        content = content.replace('content="Top-rated residential and commercial painting contractors in Miami. Specializing in high-end interior, exterior, and protective coatings against humidity."',
                                  f'content="Top-rated residential and commercial painting contractors in {city_name} FL. Specializing in high-end interior, exterior, and protective coatings against humidity."')
                                  
        # 2. Schema
        content = content.replace('"name": "Painting Florida Pros - Miami Headquarters",', f'"name": "Painting Florida Pros - {city_name} Branch",')
        content = content.replace('"addressLocality": "Miami",', f'"addressLocality": "{city_name}",')
        content = content.replace('"url": "https://paintingfloridapros.com",', f'"url": "https://paintingfloridapros.com/{folder}/",')
        
        # 3. Hero Text
        content = content.replace("MIAMI'S ELITE PAINTING CONTRACTORS", f"{city_name.upper()}'S ELITE PAINTING CONTRACTORS")
        content = content.replace("Florida's Premier<br />", "PREMIER<br />")
        content = content.replace("Painting <span", "PAINTING <span")
        content = content.replace('className="text-gradient">Contractors</span>', 'className="text-gradient">CONTRACTORS</span>')

        content = content.replace('Painting <span className="text-gradient">Contractors</span> <br />\n                                    in Miami.', 
                                  f'PAINTING <span className="text-gradient">CONTRACTORS</span> <br />\n                                    IN {city_name.upper()}.')
        
        content = content.replace("Elite residential and commercial painting services protecting Miami properties", 
                                  f"Elite residential and commercial painting services protecting {city_name} properties")
                                  
        # 4. Services Subheader
        content = content.replace('OUR EXPERTISE', f"{city_name.upper()}'S EXPERTISE")
        
        # 5. FAQs
        content = content.replace("Top answers for Miami property owners.", f"Top answers for {city_name} property owners.")
        content = content.replace("house in Miami", f"house in {city_name}")
        content = content.replace("painting services in Miami-Dade?", f"painting services near {city_name}?")
        
        # Write back
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Generated Hub: /{folder}/")

if __name__ == "__main__":
    build_hubs()
