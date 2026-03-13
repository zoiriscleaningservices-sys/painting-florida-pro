import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# The 4 Local Hubs where the 32 service files live
HUBS = [
    "coral-gables-painting",
    "miami-beach-painting",
    "brickell-painting",
    "coconut-grove-painting"
]

# The formal City Names for text replacement
CITY_NAMES = {
    "coral-gables-painting": "Coral Gables",
    "miami-beach-painting": "Miami Beach",
    "brickell-painting": "Brickell",
    "coconut-grove-painting": "Coconut Grove"
}

# The 8 internal child services to update inside each hub
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

def deep_localize():
    for hub in HUBS:
        city_name = CITY_NAMES[hub]
        hub_path = os.path.join(BASE_DIR, hub)
        
        if not os.path.exists(hub_path):
            continue

        for service in SERVICES:
            # We are rewriting the content INSIDE the localized silo folders
            # e.g., /brickell-painting/interior-painting/index.html
            filepath = os.path.join(hub_path, service, "index.html")
            
            if not os.path.exists(filepath):
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Update the Hero Paragraph
            # From: "From Brickell high-rises to Coral Gables estates..." (Generic Miami copy)
            # To: "From [City] high-rises to luxury estates..."
            hero_p_pattern = r'From Brickell high-rises to Coral Gables estates, we provide elite painting services designed to withstand the Miami sun and humidity.'
            new_hero_p = f'From {city_name} high-rises to luxury estates, we provide elite painting services designed to perfectly withstand the South Florida sun and humidity.'
            content = content.replace(hero_p_pattern, new_hero_p)
            
            # The original interior pages might have the generic Miami text if they cloned index.html
            hero_p_pattern_2 = r'From Brickell high-rises to luxury estates, we provide elite interior painting services designed to withstand the Miami sun and humidity.'
            content = content.replace(hero_p_pattern_2, new_hero_p.replace("painting services", "interior painting services"))

            # 2. Update the Sub-Header Tagline
            # From: OUR EXPERTISE
            # To: [CITY]'S EXPERTISE
            content = content.replace('OUR EXPERTISE', f"{city_name.upper()}'S EXPERTISE")

            # 3. Update the FAQ Title
            # From: Top answers for Miami property owners.
            # To: Top answers for [City] property owners.
            content = content.replace('Top answers for Miami property owners.', f'Top answers for {city_name} property owners.')

            # 4. Update the actual FAQ answers (JSON array payload inside the React component)
            # We must be careful to only target the FAQ text block, not random code.
            # Example: "The cost to paint a house in Miami varies..."
            # Note: We use regex since the text format can vary slightly
            content = content.replace('in Miami varies', f'in {city_name} varies')
            content = content.replace('in Miami-Dade county.', f'in {city_name} and the surrounding county.')
            content = content.replace("Miami's climate", f"South Florida's climate")
            content = content.replace('Miami businesses', f'{city_name} businesses')

            # 5. Fix up the title tag just to be absolutely certain it doesn't say Miami in the first half
            # The previous script changed "Miami" to the city name, but let's ensure it reads perfectly.
            # e.g. <title>Interior Painting Contractors Brickell FL</title>
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Deep localized: /{hub}/{service}/")

if __name__ == "__main__":
    deep_localize()
