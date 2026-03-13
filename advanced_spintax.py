import os
import re
import random

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# --- SPINTAX DICTIONARIES ---

TITLE_FORMATS = [
    "<title>Top {service} in {city} | Painting Florida Pros</title>",
    "<title>{city} {service} Experts - Free Estimates</title>",
    "<title>#1 Rated {service} Company | {city}, FL</title>",
    "<title>Premium {service} Services in {city} Florida</title>",
    "<title>{city}'s Best {service} Contractors | Hire Pros</title>",
    "<title>Professional {service} Near {city} | Get a Quote</title>"
]

META_FORMATS = [
    '<meta name="description" content="Looking for elite {service_short} around {city}? Our licensed Florida contractors specialize in high-end finishes that resist humidity. Call today for a free estimate!"',
    '<meta name="description" content="Painting Florida Pros delivers top-tier {service_short} throughout {city}. We use premium coatings for lasting protection against the harsh Florida climate."',
    '<meta name="description" content="Need expert {service_short} in {city}? We offer residential and commercial property enhancements with a 100% satisfaction guarantee. Request your free quote now."',
    '<meta name="description" content="Upgrade your {city} property with our professional {service_short}. We are fully insured, highly rated, and ready to transform your space. Contact us today!"',
    '<meta name="description" content="Trusted {service_short} specialists serving {city} and surrounding areas. From precise prep work to flawless execution, we guarantee a perfect finish."'
]

HERO_FORMATS = [
    "From Brickell high-rises to Coral Gables estates, we provide elite painting services designed to withstand the {city} sun and humidity.",
    "We leverage decades of Florida expertise to deliver flawless finishes tailored specifically for the unique {city} climate, ensuring long-lasting protection.",
    "Whether you are remodeling a historic residential property or updating a modern commercial space, our team brings zero-defect precision to every project in {city}.",
    "Our licensed contractors utilize premium, moisture-resistant coatings engineered to thrive in the harsh coastal elements surrounding the {city} area.",
    "Experience the difference of true craftsmanship. We offer meticulous preparation, high-end materials, and unparalleled customer service to all our {city} clients."
]

# Map friendly service names based on folder
SERVICE_MAP = {
    "residential-painting": ("Residential Painting", "residential painting services"),
    "commercial-painting": ("Commercial Painting", "commercial painting"),
    "exterior-painting": ("Exterior Painting", "exterior painting"),
    "interior-painting": ("Interior Painting", "interior finishing"),
    "cabinet-refinishing": ("Cabinet Refinishing", "cabinet restoration"),
    "epoxy-flooring": ("Epoxy Flooring", "epoxy garage floors"),
    "pressure-washing": ("Pressure Washing", "power washing"),
    "drywall-repair": ("Drywall Repair", "drywall texturing")
}

def spin_hub_index(content, city_name):
    # Hub pages have slightly different context
    title = random.choice(TITLE_FORMATS).format(city=city_name, service="Painting Contractors")
    meta = random.choice(META_FORMATS).format(city=city_name, service_short="painting services")
    hero = random.choice(HERO_FORMATS).format(city=city_name)
    
    # 1. Regex out old title
    content = re.sub(r'<title>.*?</title>', title, content)
    # 2. Regex out old meta
    content = re.sub(r'<meta name="description" content=".*?">', meta + ">", content)
    # 3. Target the specific hero paragraph text
    old_hero = f"From Brickell high-rises to Coral Gables estates, we provide elite painting services designed to withstand the {city_name} sun and humidity."
    content = content.replace(old_hero, hero)
    
    return content

def spin_service_leaf(content, city_name, service_folder):
    service_title, service_short = SERVICE_MAP.get(service_folder, ("Painting Services", "painting services"))
    
    title = random.choice(TITLE_FORMATS).format(city=city_name, service=service_title)
    meta = random.choice(META_FORMATS).format(city=city_name, service_short=service_short)
    hero = random.choice(HERO_FORMATS).format(city=city_name)
    
    content = re.sub(r'<title>.*?</title>', title, content)
    content = re.sub(r'<meta name="description" content=".*?">', meta + ">", content)
    
    old_hero = f"From Brickell high-rises to Coral Gables estates, we provide elite painting services designed to withstand the {city_name} sun and humidity."
    content = content.replace(old_hero, hero)
    
    return content

def execute_spintax():
    files_spun = 0
    # Process only "-painting" hub folders
    for folder in os.listdir(BASE_DIR):
        if not folder.endswith("-painting"):
            continue
            
        hub_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(hub_path):
            continue
            
        # Infer city name from folder: 'hialeah-painting' -> 'Hialeah'
        city_raw = folder.replace("-painting", "")
        city_name = " ".join(word.capitalize() for word in city_raw.split("-"))
        
        # A. SPIN HUB INDEX
        hub_idx = os.path.join(hub_path, "index.html")
        if os.path.exists(hub_idx):
            with open(hub_idx, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = spin_hub_index(content, city_name)
            if new_content != content:
                with open(hub_idx, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_spun += 1

        # B. SPIN NESTED SERVICES
        for svc in SERVICE_MAP.keys():
            svc_path = os.path.join(hub_path, svc, "index.html")
            if os.path.exists(svc_path):
                with open(svc_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = spin_service_leaf(content, city_name, svc)
                if new_content != content:
                    with open(svc_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    files_spun += 1
                    
        if files_spun % 1000 == 0 and files_spun > 0:
            print(f"Status: Spun {files_spun} pages...")
            
    print(f"\n✅ SPINTAX ENGINE COMPLETE")
    print(f"Successfully violent-randomized the SEO text structures of {files_spun} HTML files.")

if __name__ == '__main__':
    execute_spintax()
