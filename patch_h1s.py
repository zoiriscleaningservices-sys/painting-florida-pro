import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

HUBS = [
    "coral-gables-painting",
    "miami-beach-painting",
    "brickell-painting",
    "coconut-grove-painting"
]

CITY_NAMES = {
    "coral-gables-painting": "Coral Gables",
    "miami-beach-painting": "Miami Beach",
    "brickell-painting": "Brickell",
    "coconut-grove-painting": "Coconut Grove"
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

def patch_missed_h1s():
    for hub in HUBS:
        city_name = CITY_NAMES[hub]
        hub_path = os.path.join(BASE_DIR, hub)
        
        if not os.path.exists(hub_path):
            continue

        for service in SERVICES:
            filepath = os.path.join(hub_path, service, "index.html")
            
            if not os.path.exists(filepath):
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # The original script looked for "IN MIAMI FLORIDA."
            # But Residential/Commercial H1s say "CONTRACTORS IN MIAMI."
            content = content.replace("IN MIAMI.", f"IN {city_name.upper()}.")
            
            # Catch the little Star Badge above the H1
            # "MIAMI'S ELITE RESIDENTIAL PAINTERS" -> "[CITY]'S ELITE RESIDENTIAL PAINTERS"
            content = content.replace("MIAMI'S ELITE", f"{city_name.upper()}'S ELITE")
            content = content.replace("MIAMI'S EXPERT", f"{city_name.upper()}'S EXPERT")
            
            # Catch the Hero Paragraph text "protecting Miami homes" -> "protecting [City] homes"
            content = content.replace("protecting Miami homes", f"protecting {city_name} homes")
            content = content.replace("Miami businesses", f"{city_name} businesses")
            content = content.replace("protecting Miami roofs", f"protecting {city_name} roofs")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Patched H1 in: /{hub}/{service}/")

if __name__ == "__main__":
    patch_missed_h1s()
