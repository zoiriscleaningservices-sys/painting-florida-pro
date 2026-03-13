import os
import shutil
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# The 4 Local Hubs where we want the services to live
HUBS = [
    "coral-gables-painting",
    "miami-beach-painting",
    "brickell-painting",
    "coconut-grove-painting"
]

# The mapping of formal City Names for Title/H1 replacements
CITY_NAMES = {
    "coral-gables-painting": "Coral Gables",
    "miami-beach-painting": "Miami Beach",
    "brickell-painting": "Brickell",
    "coconut-grove-painting": "Coconut Grove"
}

# The 8 Services we want to copy *into* every Hub
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

def build_insulated_silos():
    for hub in HUBS:
        city_name = CITY_NAMES[hub]
        hub_path = os.path.join(BASE_DIR, hub)
        
        # Ensure the hub exists
        if not os.path.exists(hub_path):
            print(f"Error: Hub not found at {hub_path}")
            continue

        for service in SERVICES:
            # Source: The global service index file (e.g., /interior-painting/index.html)
            source_file = os.path.join(BASE_DIR, service, "index.html")
            
            # Destination: The localized silo path (e.g., /brickell-painting/interior-painting/index.html)
            dest_folder = os.path.join(hub_path, service)
            dest_file = os.path.join(dest_folder, "index.html")
            
            if not os.path.exists(source_file):
                print(f"Warning: Source service file not found: {source_file}")
                continue

            # Create the nested service folder
            os.makedirs(dest_folder, exist_ok=True)
            
            # Copy the logic and layout
            shutil.copy2(source_file, dest_file)
            
            # Now, open the newly copied file and "Localize" it
            with open(dest_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Localize H1 Tag (e.g., IN MIAMI FLORIDA -> IN [CITY NAME] FLORIDA)
            # All global services currently say "IN MIAMI FLORIDA." at the end of their H1 block.
            content = content.replace("IN MIAMI FLORIDA.", f"IN {city_name.upper()} FLORIDA.")

            # 2. Localize Title Tag
            # We want to replace "Miami" with the specific city name in the title
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                old_title = title_match.group(1)
                new_title = old_title.replace("Miami", city_name).replace("MIAMI", city_name)
                content = content.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>')
                
            # 3. Localize Meta Description
            desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)">', content)
            if desc_match:
                old_desc = desc_match.group(1)
                new_desc = old_desc.replace("Miami's", f"{city_name}'s").replace("Miami", city_name)
                content = content.replace(f'<meta name="description" content="{old_desc}">', f'<meta name="description" content="{new_desc}">')
                
            # 4. Update the schema URL to point to this new exact page
            # Global: "url": "https://www.paintingfloridapros.com/interior-painting/",
            # New Local: "url": "https://www.paintingfloridapros.com/brickell-painting/interior-painting/",
            content = content.replace(
                f'"url": "https://www.paintingfloridapros.com/{service}/",', 
                f'"url": "https://www.paintingfloridapros.com/{hub}/{service}/",'
            )
            # Also catch older schema URL patterns just in case
            content = content.replace(
                f'"url": "https://www.paintingfloridapros.com/{service}.html",',
                f'"url": "https://www.paintingfloridapros.com/{hub}/{service}/",'
            )

            # Save the localized child page
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Generated: /{hub}/{service}/")

if __name__ == "__main__":
    build_insulated_silos()
