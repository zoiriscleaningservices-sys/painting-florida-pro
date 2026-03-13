import os
import shutil
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
SOURCE_FILE = os.path.join(BASE_DIR, "index.html")

# The data for building out the 4 localized silos
NEIGHBORHOODS = {
    "coral-gables-painting.html": {
        "title": "Top Painting Contractors Coral Gables FL | Elite Home Painters",
        "description": "Coral Gables' #1 rated painting contractors. We specialize in high-end historic residential, commercial, and interior painting designed for the local climate.",
        "schema_locality": "Coral Gables",
        "schema_lat": "25.7215",
        "schema_lon": "-80.2684",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                TOP RATED <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN CORAL GABLES.
                            </h1>""",
        "tagline": "CORAL GABLES' #1 RATED PAINTING CONTRACTORS"
    },
    "miami-beach-painting.html": {
        "title": "Best Painters in Miami Beach FL | Coastal Painting Experts",
        "description": "Expert Miami Beach painting contractors specializing in salt-air resistant exterior coatings, luxury condo interiors, and local commercial painting.",
        "schema_locality": "Miami Beach",
        "schema_lat": "25.7906",
        "schema_lon": "-80.1300",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                TOP RATED <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN MIAMI BEACH.
                            </h1>""",
        "tagline": "MIAMI BEACH'S ELITE PAINTING CONTRACTORS"
    },
    "brickell-painting.html": {
        "title": "Brickell Painting Services | High-Rise & Luxury Condo Painters",
        "description": "Brickell's premier residential and commercial painters. We are fully insured and specialized in high-rise luxury condo interior painting and corporate offices.",
        "schema_locality": "Brickell",
        "schema_lat": "25.7582",
        "schema_lon": "-80.1931",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                FINANCIAL DISTRICT <br />
                                <span className="text-gradient">
                                    PAINTING SERVICES
                                </span> <br />
                                IN BRICKELL.
                            </h1>""",
        "tagline": "BRICKELL'S HIGH-RISE PAINTING EXPERTS"
    },
    "coconut-grove-painting.html": {
        "title": "Coconut Grove Painters | Professional Interior & Exterior",
        "description": "Top-rated painting services in Coconut Grove. We offer flawless interior finishes and weather-resistant exterior painting for historic Grove properties.",
        "schema_locality": "Coconut Grove",
        "schema_lat": "25.7123",
        "schema_lon": "-80.2452",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                PROFESSIONAL <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN COCONUT GROVE.
                            </h1>""",
        "tagline": "COCONUT GROVE'S PREMIER PAINTERS"
    }
}

def build_silos():
    if not os.path.exists(SOURCE_FILE):
        print(f"Source file not found: {SOURCE_FILE}")
        return

    for filename, data in NEIGHBORHOODS.items():
        dest_path = os.path.join(BASE_DIR, filename)
        
        # 1. Copy index.html as the foundation for the neighborhood file
        shutil.copy2(SOURCE_FILE, dest_path)
        
        with open(dest_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 2. Inject Localized Title & Meta Description
        # Use regex to find and replace the title and description tags safely
        title_pattern = r'<title>.*?</title>'
        desc_pattern = r'<meta\s+name="description"\s+content=".*?"\s*>'
        
        content = re.sub(title_pattern, f'<title>{data["title"]}</title>', content, count=1)
        content = re.sub(desc_pattern, f'<meta name="description" content="{data["description"]}">', content, count=1)
        
        # 3. Inject Localized JSON-LD Schema
        # We need to swap the Locality, Lat, and Lon strings specifically
        content = content.replace('"addressLocality": "Miami",', f'"addressLocality": "{data["schema_locality"]}",')
        content = content.replace('"latitude": 25.7617,', f'"latitude": {data["schema_lat"]},')
        content = content.replace('"longitude": -80.1918', f'"longitude": {data["schema_lon"]}')
        
        # Change the Schema Name to include the neighborhood explicitly
        content = content.replace('"name": "Painting Florida Pros - Miami",', f'"name": "Painting Florida Pros - {data["schema_locality"]}",')
        
        # Add the specific neighborhood file to the Schema URL
        content = content.replace('"url": "https://paintingfloridapros.com",', f'"url": "https://paintingfloridapros.com/{filename}",')
        
        # 4. Inject Localized H1 Array (The Hero Section exactly)
        old_h1 = """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                TOP RATED <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>"""
        content = content.replace(old_h1, data["h1"])
        
        # 5. Inject Localized Tagline string inside the Hero element specific to the neighborhood
        old_tagline = r'MIAMI\'S #1 RATED PAINTING CONTRACTORS'
        content = content.replace(old_tagline, data["tagline"])

        # 6. Save the perfectly mirrored, hyper-localized SEO version
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully generated silo: {filename}")

if __name__ == "__main__":
    build_silos()
