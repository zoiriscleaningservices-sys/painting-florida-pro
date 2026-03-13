import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
OLD_DOMAIN = "https://www.paintingfloridapros.com"
NEW_DOMAIN = "https://www.paintingfloridapros.com"

# Common file types to analyze for the naked domain issue
VALID_EXTENSIONS = ('.html', '.xml', '.txt', '.py')

def patch_www_domain():
    updated_files = 0
    total_files_scanned = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Exclude internal version control and ide caches
        if '.git' in root or '.gemini' in root:
            continue
            
        for file in files:
            if file.endswith(VALID_EXTENSIONS):
                filepath = os.path.join(root, file)
                total_files_scanned += 1
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Target naked domain for replacement
                    if OLD_DOMAIN in content:
                        # Simple replacement
                        new_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
                        
                        # Failsafe: Prevent 'https://www.www.painting...' if old domain was already www
                        new_content = new_content.replace(
                            "https://www.paintingfloridapros.com", 
                            "https://www.paintingfloridapros.com"
                        )
                        
                        if new_content != content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            updated_files += 1
                            
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
                    
    print("\n✅ GLOBAL URL CANONICALIZATION COMPLETE")
    print(f"Scanned {total_files_scanned} files.")
    print(f"Successfully injected `www.` prefix into {updated_files} files across the architecture.")

if __name__ == '__main__':
    patch_www_domain()
