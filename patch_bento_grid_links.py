import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

OLD_LINK_STR = "href={`/${service.title.toLowerCase().replace(' painting', '').replace(' ', '-').replace('property', 'painting')}-painting.html`.replace('-painting-painting', '-painting').replace('cabinet-refinishing-painting', 'cabinet-refinishing')}"

def patch_bento_grids():
    scanned = 0
    updated = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                scanned += 1
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if OLD_LINK_STR in content:
                    rel_path = os.path.relpath(root, BASE_DIR)
                    parts = rel_path.split(os.sep)
                    
                    silo_prefix = "/"
                    if parts[0] != '.':
                        silo_prefix = f"/{parts[0]}/"
                        
                    NEW_LINK_STR = f"href={{`{silo_prefix}${{service.title.toLowerCase().replace(' painting', '').replace(' ', '-').replace('property', 'painting')}}-painting/`.replace('-painting-painting/', '-painting/').replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')}}"

                    content = content.replace(OLD_LINK_STR, NEW_LINK_STR)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                    updated += 1
                    
    print(f"Scanned {scanned} files.")
    print(f"Updated {updated} Bento Grids.")

if __name__ == '__main__':
    patch_bento_grids()
