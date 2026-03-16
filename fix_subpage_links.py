import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

def fix_subpage_links():
    updated_files = 0
    
    # We are looking for any href interpolation inside the map() loops that look like this on the deep deep subpages:
    # `href={`/west-shenandoah-painting/${service.title.toLowerCase().replace(' painting', '').replace(' ', '-').replace('property', 'painting')}-painting/`.replace('-painting-painting/', '-painting/').replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')} `
    
    # They are missing the rest of the replace chain!
    # (.replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')})
    
    search_pattern = re.compile(r"(\.replace\('cabinet-refinishing-painting/',\s*'cabinet-refinishing/'\))\}")
    
    replace_string = r"\1.replace('epoxy-flooring-painting/', 'epoxy-flooring/').replace('pressure-washing-painting/', 'pressure-washing/').replace('drywall-repair-painting/', 'drywall-repair/')}"

    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if ".replace('epoxy-flooring-painting/', 'epoxy-flooring/')" in content:
                        continue # Already updated

                    new_content, count = re.subn(search_pattern, replace_string, content)

                    if count > 0:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_files += 1
                        
                except Exception as e:
                    print(f"Error on {filepath}: {e}")

                if updated_files > 0 and updated_files % 1000 == 0:
                    print(f"Status: Updated {updated_files} files...")

    print(f"Complete. Fixed deep subpage links in {updated_files} HTML files sitewide.")

if __name__ == '__main__':
    fix_subpage_links()
