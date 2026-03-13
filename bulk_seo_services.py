import os

# Define the base directory
BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Data structures for the 4 pages
PAGE_DATA = {
    "residential-painting.html": {
        "services_array": """        const SERVICES = [
            { title: "Interior House Painting", description: "Flawless luxury finishes for living rooms, bedrooms, and entire home interiors.", icon: "Paintbrush", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Exterior Protection", description: "Weather-resistant coatings designed specifically to withstand harsh Miami sun and humidity.", icon: "Shield", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Kitchen Cabinets", description: "Give your kitchen a factory-new look with our specialized cabinet painting process.", icon: "Layers", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Drywall Repair", description: "Seamless patching and blending for water damage, cracks, and everyday wear and tear.", icon: "Wrench", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Wood Staining", description: "Enhance and protect exterior decks, fences, and pergolas from absolute sun decay.", icon: "Sun", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Color Consultation", description: "Expert design advice to pick the perfect palette for your Miami home's natural lighting.", icon: "Palette", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];""",
        "cta_text": "READY FOR A NEW INTERIOR?"
    },
    "commercial-painting.html": {
        "services_array": """        const SERVICES = [
            { title: "Office & Retail", description: "Low-odor, rapid-dry painting to keep your Miami storefront or office running smoothly.", icon: "Building", image: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=800" },
            { title: "High-Rise Exteriors", description: "Fully insured and equipped for complex, multi-story condominium and hotel painting.", icon: "Building2", image: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=800" },
            { title: "Industrial Epoxies", description: "Heavy-duty floor coatings for warehouses, showrooms, and manufacturing facilities.", icon: "Layers", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Anti-Graffiti", description: "Protective clear coats that allow you to easily wash away vandalism and tagging.", icon: "ShieldAlert", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "HOA Communities", description: "Large-scale cohesive painting plans for Miami-Dade townhomes and community associations.", icon: "Home", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Warehouse Coatings", description: "Direct-to-metal (DTM) paints and rust-inhibitive primers for structural steel.", icon: "Zap", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];""",
        "cta_text": "READY TO UPGRADE YOUR BUSINESS?"
    },
    "exterior-painting.html": {
        "services_array": """        const SERVICES = [
            { title: "Elastomeric Coating", description: "Thick, flexible waterproofing bridge that seals hairline stucco cracks from driving rain.", icon: "ShieldCheck", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Stucco Repair", description: "Expert patching and texturing to match your home's existing block or frame construction.", icon: "Wrench", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Coastal Proofing", description: "100% acrylic UV-resistant paints specifically formulated to combat fading and salt air.", icon: "Sun", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Power Washing", description: "High-PSI removal of chalking, mold, mildew, and salt residue prior to painting.", icon: "Droplets", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Trim & Fascia", description: "Detail-oriented painting of soffits, gutters, and trim for sharp architectural contrast.", icon: "Mails", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Deck Staining", description: "Deep penetrating oils to protect your pool deck and wooden patios from water rot.", icon: "Layers", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];""",
        "cta_text": "READY TO PROTECT YOUR EXTERIOR?"
    },
    "cabinet-refinishing.html": {
        "services_array": """        const SERVICES = [
            { title: "Solid Color Conversion", description: "Transform outdated dark oak or cherry wood into modern, bright white or custom colors.", icon: "Palette", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Factory Finish", description: "Sprayed industrial-grade urethane enamels for a hard, smooth, chip-resistant shell.", icon: "Shield", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Custom Built-ins", description: "Refinishing for library shelves, entertainment centers, and custom closet millwork.", icon: "LayoutTemplate", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Vanity Refinishing", description: "Moisture-resistant bathroom vanity upgrades that withstand high Florida humidity.", icon: "Thermometer", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Hardware Upgrades", description: "Drilling and filling for brand new handle and pull placements to complete the modern look.", icon: "Wrench", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Stain Blocking", description: "Heavy-duty shellac and oil primers to guarantee dark wood tannins never bleed through.", icon: "XCircle", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];""",
        "cta_text": "READY FOR A NEW KITCHEN?"
    }
}

def process_files():
    for filename, data in PAGE_DATA.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Replace SERVICES array
        # Find the start of the SERVICES array
        start_idx = content.find("const SERVICES = [")
        if start_idx != -1:
            # Find the end of the array by looking for ];
            end_idx = content.find("];", start_idx) + 2
            if end_idx > 1:
                # Replace the entire block
                content = content[:start_idx] + data["services_array"] + content[end_idx:]

        # 2. Update all LEARN MORE links in the SERVICES sections to drop to #contact instead of dynamic .html
        # Replace desktop link
        old_desktop_link = "href={`/${service.title.toLowerCase().replace(' painting', '').replace(' ', '-').replace('property', 'painting')}-painting.html`.replace('-painting-painting', '-painting').replace('cabinet-refinishing-painting', 'cabinet-refinishing')}"
        new_desktop_link = 'href="#contact"'
        content = content.replace(old_desktop_link, new_desktop_link)
        
        # Replace mobile link (it was using the same dynamic link string)
        
        # 3. Replace Contact Header
        content = content.replace("FRESH START?", data["cta_text"])

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully optimized: {filename}")

if __name__ == "__main__":
    process_files()
