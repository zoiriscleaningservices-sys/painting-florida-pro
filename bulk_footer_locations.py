import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# We have 9 files total
ALL_FILES = [
    "index.html",
    "residential-painting.html",
    "commercial-painting.html",
    "exterior-painting.html",
    "cabinet-refinishing.html",
    "coral-gables-painting.html",
    "miami-beach-painting.html",
    "brickell-painting.html",
    "coconut-grove-painting.html"
]

# The block to search for to know where to inject our new column
TARGET_BLOCK = """                            <motion.div 
                                initial={{ opacity: 0, y: 30 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                transition={{ duration: 0.8, delay: 0.4 }}
                                className="text-center sm:text-left"
                            >
                                <h4 className="font-bold mb-8 text-sm uppercase tracking-widest text-brand-dark">EXPLORE</h4>
                                <ul className="space-y-4 text-brand-dark/60 text-sm">
                                    {[{name: 'Home', link: '#'}, {name: 'Our Services', link: '#services'}, {name: 'Get A Quote', link: '#contact'}, {name: 'Sitemap', link: '#'}, {name: 'Privacy Policy', link: '#'}].map((item) => (
                                        <motion.li key={item.name} whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer">
                                            <a href={item.link} className="transition-colors">{item.name}</a>
                                        </motion.li>
                                    ))}
                                </ul>
                            </motion.div>"""

# The new block to insert right after the target block
NEW_COLUMN = """

                            <motion.div 
                                initial={{ opacity: 0, y: 30 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                transition={{ duration: 0.8, delay: 0.5 }}
                                className="text-center sm:text-left"
                            >
                                <h4 className="font-bold mb-8 text-sm uppercase tracking-widest text-brand-dark">MIAMI LOCATIONS</h4>
                                <ul className="space-y-4 text-brand-dark/60 text-sm">
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/coral-gables-painting.html" className="transition-colors">Coral Gables</a></motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/miami-beach-painting.html" className="transition-colors">Miami Beach</a></motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/brickell-painting.html" className="transition-colors">Brickell</a></motion.li>
                                    <motion.li whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/coconut-grove-painting.html" className="transition-colors">Coconut Grove</a></motion.li>
                                </ul>
                            </motion.div>"""


def update_footers():
    for f in ALL_FILES:
        filepath = os.path.join(BASE_DIR, f)
        if not os.path.exists(filepath):
            print(f"Skipping {f}, file not found.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # First update grid columns in the footer setup to fit the extra column
        # Original: grid sm:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-16
        # New: grid sm:grid-cols-2 lg:grid-cols-5 gap-12 lg:gap-16
        grid_target = 'className="grid sm:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-16 mb-16 sm:mb-24"'
        new_grid_target = 'className="grid sm:grid-cols-3 lg:grid-cols-5 gap-8 lg:gap-12 mb-16 sm:mb-24"'
        content = content.replace(grid_target, new_grid_target)

        # Inject the new column
        if TARGET_BLOCK in content and "MIAMI LOCATIONS" not in content:
            # We want to insert the NEW_COLUMN right after the TARGET_BLOCK
            updated_content = content.replace(TARGET_BLOCK, TARGET_BLOCK + NEW_COLUMN)
        
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(updated_content)
                
            print(f"Successfully updated footer links in {f}")
        else:
            print(f"Pattern not found or already applied in {f}")

if __name__ == "__main__":
    update_footers()
