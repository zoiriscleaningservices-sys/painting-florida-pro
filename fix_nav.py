import os
import glob
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

def fix_nav_links():
    # Gather all HTML files (they are now in subfolders + root)
    all_html_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
    
    for filepath in all_html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the main NAV_ITEMS array which is hardcoded in React
        # Old: { label: 'Home', href: 'index.html' }
        # New: { label: 'Home', href: '/' }
        content = content.replace("{ label: 'Home', href: 'index.html' }", "{ label: 'Home', href: '/' }")
        
        # Update the Mobile Nav which has a different structure
        # Old: href="index.html"
        # New: href="/" (but ONLY within the nav logo link, NOT the generic regex we ran before)
        content = content.replace('<a href="index.html" className="flex items-center gap-3">', '<a href="/" className="flex items-center gap-3">')
        content = content.replace('<a href="/index.html" className="flex items-center gap-3">', '<a href="/" className="flex items-center gap-3">')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Patched NAV items in: {os.path.relpath(filepath, BASE_DIR)}")

if __name__ == "__main__":
    fix_nav_links()
