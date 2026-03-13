import os
import shutil

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
SOURCE_FILE = os.path.join(BASE_DIR, "index.html")

# The data for building out the 4 dedicated service pages
SERVICES = {
    "interior-painting.html": {
        "title": "Interior Painting Contractors Miami FL | Professional House Painters",
        "description": "Miami's top-rated interior painting services. Expert prep-work, crisp lines, and premium drywall repair. Call today for a perfectly painted home.",
        "schema_type": "HousePainter",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                PROFESSIONAL <br />
                                <span className="text-gradient">
                                    INTERIOR PAINTING
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>""",
        "tagline": "MIAMI'S ELITE INTERIOR PAINTERS",
        "services_array": """        const SERVICES = [
            {
                title: "Living Room Painting",
                description: "Transform your main living spaces with perfect edges, smooth walls, and vibrant colors.",
                icon: "Armchair",
                image: "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Bedroom Design",
                description: "Create a relaxing oasis with our expert residential bedroom painting and color consultation.",
                icon: "Bed",
                image: "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Trim & Doors",
                description: "Flawless ultra-smooth finishes for baseboards, crown molding, and interior doors.",
                icon: "DoorOpen",
                image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Kitchen Painting",
                description: "Durable, washable paints designed specifically for high-traffic and high-humidity kitchen environments.",
                icon: "Utensils",
                image: "https://images.unsplash.com/photo-1556910103-1c02745a872f?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Vaulted Ceilings",
                description: "Expert equipment and scaffolding to safely paint high ceilings and hard-to-reach foyers.",
                icon: "ArrowUpToLine",
                image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=800"
            }
        ];"""
    },
    "epoxy-flooring.html": {
        "title": "Epoxy Garage Floor Coatings Miami | Concrete & Industrial Painters",
        "description": "Premium epoxy flooring and concrete coatings for Miami garages, warehouses, and commercial spaces. Highly durable, slip-resistant, and visually stunning.",
        "schema_type": "PaintingContractor",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                INDUSTRIAL <br />
                                <span className="text-gradient">
                                    EPOXY COATINGS
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>""",
        "tagline": "PREMIUM GARAGE & CONCRETE COATINGS",
        "services_array": """        const SERVICES = [
            {
                title: "Garage Floor Epoxy",
                description: "Transform your dirty garage into a clean, showroom-quality space that resists oil, tire marks, and chemicals.",
                icon: "Car",
                image: "https://images.unsplash.com/photo-1508215885820-4585e5610ec8?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Industrial Warehouses",
                description: "Heavy-duty polyaspartic and epoxy flooring designed for forklifts, high traffic, and safety compliance.",
                icon: "Factory",
                image: "https://images.unsplash.com/photo-1586528116311-ad8ed745d654?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Retail Spaces",
                description: "Beautiful, seamless metallic and flake epoxy options that impress customers and withstand heavy foot traffic.",
                icon: "Store",
                image: "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Concrete Sealing",
                description: "Protect your exterior driveways and patios from Miami rain, oil stains, and tire wear with our clear sealers.",
                icon: "Shield",
                image: "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Pool Decks",
                description: "Slip-resistant, UV-stable coatings designed specifically for Florida pool decks and outdoor living areas.",
                icon: "Waves",
                image: "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&q=80&w=800"
            }
        ];"""
    },
    "pressure-washing.html": {
        "title": "Pro Pressure Washing Miami FL | Driveway & Roof Cleaning",
        "description": "Miami's best pressure washing and exterior cleaning services. We remove mold, mildew, and dirt from roofs, driveways, patios, and commercial buildings.",
        "schema_type": "ProfessionalService",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                PROFESSIONAL <br />
                                <span className="text-gradient">
                                    PRESSURE WASHING
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>""",
        "tagline": "EXPERT DRIVEWAY & EXTERIOR CLEANING",
        "services_array": """        const SERVICES = [
            {
                title: "Driveway Cleaning",
                description: "Erase years of tire marks, oil spills, and embedded dirt from your concrete driveways and walkways.",
                icon: "Droplet",
                image: "https://images.unsplash.com/photo-1621252178223-951da6faba57?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Roof Soft Washing",
                description: "Safe, low-pressure soft washing that destroys algae and black streaks without damaging your roofing tiles.",
                icon: "Home",
                image: "https://images.unsplash.com/photo-1613531190412-1f48ed2d99db?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "House Exteriors",
                description: "Remove the green algae, dirt, and salt residue from your stucco or siding to restore its original color.",
                icon: "Sparkles",
                image: "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Patio & Deck Cleaning",
                description: "Restore your outdoor living spaces. We safely clean wood, composite, pavers, and stamped concrete.",
                icon: "Sun",
                image: "https://images.unsplash.com/photo-1599839619722-39751411ea63?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Commercial Lots",
                description: "Keep your business looking sharp with our heavy-duty commercial pressure washing and gum removal services.",
                icon: "Building",
                image: "https://images.unsplash.com/photo-1504307651254-35680f356fec?auto=format&fit=crop&q=80&w=800"
            }
        ];"""
    },
    "drywall-repair.html": {
        "title": "Expert Drywall Repair Miami | Patching & Texture Contractors",
        "description": "Seamless drywall repair, hole patching, and texture matching in Miami. We fix water damage and cracking plaster before painting for a flawless finish.",
        "schema_type": "HousePainter",
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                SEAMLESS <br />
                                <span className="text-gradient">
                                    DRYWALL REPAIR
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>""",
        "tagline": "FLAWLESS PATCHING & TEXTURE MATCHING",
        "services_array": """        const SERVICES = [
            {
                title: "Hole & Dent Patching",
                description: "We fix everything from doorknob holes to huge wall damage, leaving a perfectly smooth and paintable surface.",
                icon: "Hammer",
                image: "https://images.unsplash.com/photo-1585421514738-01798e348b17?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Water Damage Repair",
                description: "Florida humidity can ruin ceilings and walls. We cut out rotted/stained drywall and seamlessly install new panels.",
                icon: "Droplet",
                image: "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Texture Matching",
                description: "Orange peel, knock-down, or smooth—our experts can match any existing wall texture perfectly so the patch disappears.",
                icon: "PenTool",
                image: "https://images.unsplash.com/photo-1598300042247-d088f8ab3a91?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Popcorn Removal",
                description: "Modernize your home by safely removing outdated popcorn ceilings and refinishing them with a clean, smooth skim coat.",
                icon: "Wrench",
                image: "https://images.unsplash.com/photo-1620626011761-996317b8d101?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Plaster Repair",
                description: "Specialized repair techniques for historic homes and older plaster walls that are cracking or peeling.",
                icon: "Box",
                image: "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&q=80&w=800"
            }
        ];"""
    }
}

def build_service_pages():
    import re
    if not os.path.exists(SOURCE_FILE):
        print(f"Source file not found: {SOURCE_FILE}")
        return

    for filename, data in SERVICES.items():
        dest_path = os.path.join(BASE_DIR, filename)
        
        # 1. Copy index.html as the foundation for the new service file
        shutil.copy2(SOURCE_FILE, dest_path)
        
        with open(dest_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 2. Inject Title & Meta Description safely
        title_pattern = r'<title>.*?</title>'
        desc_pattern = r'<meta\s+name="description"\s+content=".*?"\s*>'
        
        content = re.sub(title_pattern, f'<title>{data["title"]}</title>', content, count=1)
        content = re.sub(desc_pattern, f'<meta name="description" content="{data["description"]}">', content, count=1)
        
        # 3. Swap the JSON Schema specifically
        # Switch PaintingBuilder to HousePainter/ProfessionalService where appropriate
        content = content.replace('"@type": "PaintingBuilder",', f'"@type": "{data["schema_type"]}",')
        # Add the specific filename to the Schema URL
        content = content.replace('"url": "https://www.paintingfloridapros.com",', f'"url": "https://www.paintingfloridapros.com/{filename}",')
        
        # 4. Inject EXACT MATCH H1 Hero Text
        old_h1 = """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                TOP RATED <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>"""
        content = content.replace(old_h1, data["h1"])
        
        # 5. Inject Tagline
        old_tagline = r'MIAMI\'S #1 RATED PAINTING CONTRACTORS'
        content = content.replace(old_tagline, data["tagline"])

        # 6. Swap out the entire SERVICES array so it only shows sub-services for this specific niche
        # We need to find the entire block from 'const SERVICES = [' to the closing '];'
        import re
        services_pattern = r'const SERVICES = \[.*?\];'
        content = re.sub(services_pattern, data["services_array"], content, flags=re.DOTALL)

        # 7. Save the page
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully generated service page: {filename}")

if __name__ == "__main__":
    build_service_pages()
