import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# We now have 13 files total
ALL_FILES = [
    "index.html",
    "residential-painting.html",
    "commercial-painting.html",
    "exterior-painting.html",
    "cabinet-refinishing.html",
    "coral-gables-painting.html",
    "miami-beach-painting.html",
    "brickell-painting.html",
    "coconut-grove-painting.html",
    "interior-painting.html",
    "epoxy-flooring.html",
    "pressure-washing.html",
    "drywall-repair.html"
]

# The block to search for to know where to inject our new links (Index & Silos)
TARGET_BLOCK_1 = """                                <ul className="space-y-4 text-brand-dark/60 text-sm">
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/residential-painting.html" className="transition-colors">Residential Painting</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/commercial-painting.html" className="transition-colors">Commercial Painting</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/exterior-painting.html" className="transition-colors">Exterior Painting</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/cabinet-refinishing.html" className="transition-colors">Cabinet Refinishing</a>
                                    </motion.li>"""

# The block to search for in the inner service pages
TARGET_BLOCK_2 = """                                <ul className="space-y-4 text-brand-dark/60 text-sm">
                                    {['Residential Painting', 'Commercial Painting', 'Interior Painting', 'Exterior Painting', 'Cabinet Refinishing', 'Industrial Coatings'].map((link) => (
                                        <motion.li key={link} whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                            <a href="#services" className="transition-colors">{link}</a>
                                        </motion.li>
                                    ))}"""

# On the inner service pages, we must REPLACE TARGET_BLOCK_2 with TARGET_BLOCK_1 + NEW_LINKS
# On the index and silos, we just append NEW_LINKS to TARGET_BLOCK_1

# The new links to insert right after the target block
NEW_LINKS = """
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/interior-painting.html" className="transition-colors">Interior Painting</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/epoxy-flooring.html" className="transition-colors">Epoxy & Concrete</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/pressure-washing.html" className="transition-colors">Pressure Washing</a>
                                    </motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                        <a href="/drywall-repair.html" className="transition-colors">Drywall Repair</a>
                                    </motion.li>"""

def update_footers():
    for f in ALL_FILES:
        filepath = os.path.join(BASE_DIR, f)
        if not os.path.exists(filepath):
            print(f"Skipping {f}, file not found.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Inject the new column
        if TARGET_BLOCK_1 in content and "/interior-painting.html" not in content:
            updated_content = content.replace(TARGET_BLOCK_1, TARGET_BLOCK_1 + NEW_LINKS)
        
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(updated_content)
                
            print(f"Successfully appended footer SERVICES array in {f}")
        elif TARGET_BLOCK_2 in content:
            # Overwrite the old inner array with the new master list
            updated_content = content.replace(TARGET_BLOCK_2, TARGET_BLOCK_1 + NEW_LINKS)
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(updated_content)
            print(f"Successfully replaced footer SERVICES array in {f}")
        else:
            print(f"Pattern not found or already applied in {f}")

if __name__ == "__main__":
    update_footers()
