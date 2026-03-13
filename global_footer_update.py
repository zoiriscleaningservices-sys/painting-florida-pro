import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# We have exactly 20 hubs: 4 originals, 6 from phase 6, 10 from phase 7.
# We want to replace whatever <ul> block exists with a new <div className="grid grid-cols-2 gap-x-4 gap-y-3 text-brand-dark/60 text-sm">

NEW_FOOTER_BLOCK = """<div className="grid grid-cols-2 gap-x-4 gap-y-3 text-brand-dark/60 text-sm">
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/coral-gables-painting/" className="transition-colors truncate block">Coral Gables</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/miami-beach-painting/" className="transition-colors truncate block">Miami Beach</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/brickell-painting/" className="transition-colors truncate block">Brickell</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/coconut-grove-painting/" className="transition-colors truncate block">Coconut Grove</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/aventura-painting/" className="transition-colors truncate block">Aventura</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/pinecrest-painting/" className="transition-colors truncate block">Pinecrest</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/doral-painting/" className="transition-colors truncate block">Doral</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/key-biscayne-painting/" className="transition-colors truncate block">Key Biscayne</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/kendall-painting/" className="transition-colors truncate block">Kendall</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/wynwood-painting/" className="transition-colors truncate block">Wynwood</a></motion.div>
                                    
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/hialeah-painting/" className="transition-colors truncate block">Hialeah</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/homestead-painting/" className="transition-colors truncate block">Homestead</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/north-miami-painting/" className="transition-colors truncate block">North Miami</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/palmetto-bay-painting/" className="transition-colors truncate block">Palmetto Bay</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/sunny-isles-beach-painting/" className="transition-colors truncate block">Sunny Isles</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/surfside-painting/" className="transition-colors truncate block">Surfside</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/bal-harbour-painting/" className="transition-colors truncate block">Bal Harbour</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/south-miami-painting/" className="transition-colors truncate block">South Miami</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/miami-lakes-painting/" className="transition-colors truncate block">Miami Lakes</a></motion.div>
                                    <motion.div whileHover={{ x: 5, color: '#F27D26' }} className="cursor-pointer"><a href="/sunset-painting/" className="transition-colors truncate block">Sunset</a></motion.div>
                                </div>"""

def update_footers():
    updated = 0
    # The existing blocks could be either the old 4-item UL or the 10-item UL.
    # regex should find any <ul className="space-y-4 text-brand-dark/60 text-sm"> that contains coral-gables-painting and ends with </ul>
    pattern_ul = re.compile(r'<ul className="space-y-4 text-brand-dark/60 text-sm">.*?<a href="/coral-gables-painting/".*?</ul>', re.DOTALL)
    
    # Just in case we already ran a partial update or there's a typo, let's also detect if we already have the div block
    pattern_div = re.compile(r'<div className="grid grid-cols-2 gap-x-4 gap-y-3 text-brand-dark/60 text-sm">.*?<a href="/coral-gables-painting/".*?</div>', re.DOTALL)
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                has_changes = False
                
                # Try finding UL block
                if re.search(pattern_ul, content):
                    content = re.sub(pattern_ul, NEW_FOOTER_BLOCK, content)
                    has_changes = True
                
                # Or try finding DIV block to force-update
                elif re.search(pattern_div, content):
                    content = re.sub(pattern_div, NEW_FOOTER_BLOCK, content)
                    has_changes = True

                if has_changes:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated += 1

    print(f"\nSuccessfully rewrote the footer design in {updated} files with the massive 20-city grid.")

if __name__ == "__main__":
    update_footers()
