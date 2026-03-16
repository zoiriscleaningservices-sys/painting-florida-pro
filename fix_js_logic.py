import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Looking at index.html line 593 right now:
# <a href={`/${service.title.toLowerCase().replace(' painting', '').replace(' ', '-').replace('property', 'painting')}-painting/`.replace('-painting-painting/', '-painting/').replace('cabinet-refinishing/', 'cabinet-refinishing/').replace('epoxy-flooring/', 'epoxy-flooring/').replace('pressure-washing/', 'pressure-washing/').replace('drywall-repair/', 'drywall-repair/')} 

# The issue is the replace strings: .replace('cabinet-refinishing/', 'cabinet-refinishing/')
# It should be: .replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')

def fix_js_logic():
    updated = 0
    
    # We will search and replace those ineffective replace commands.
    bad_replaces = [
        (".replace('cabinet-refinishing/', 'cabinet-refinishing/')", ".replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')"),
        (".replace('epoxy-flooring/', 'epoxy-flooring/')", ".replace('epoxy-flooring-painting/', 'epoxy-flooring/')"),
        (".replace('pressure-washing/', 'pressure-washing/')", ".replace('pressure-washing-painting/', 'pressure-washing/')"),
        (".replace('drywall-repair/', 'drywall-repair/')", ".replace('drywall-repair-painting/', 'drywall-repair/')")
    ]

    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    for bad, good in bad_replaces:
                        content = content.replace(bad, good)

                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated += 1
                        
                except Exception as e:
                    print(f"Error on {filepath}: {e}")

                if updated > 0 and updated % 1000 == 0:
                    print(f"Status: Updated {updated} files...")

    print(f"Complete. Fixed JS replace logic in {updated} files sitewide.")

if __name__ == '__main__':
    fix_js_logic()
