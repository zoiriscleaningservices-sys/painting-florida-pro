import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
TARGET_STRING = "{ label: 'Home', href: '/' }"

def patch_nav_home():
    updated_files = 0
    scanned_files = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                scanned_files += 1
                
                # Calculate relative depth to determine page type
                rel_path = os.path.relpath(filepath, BASE_DIR)
                parts = rel_path.split(os.sep)
                
                # Default new href
                new_href = '/'
                
                if len(parts) == 1:
                    # Root level (index.html) -> Scroll to top
                    new_href = '#'
                elif len(parts) == 2:
                    # First level directory (e.g. /kendall-painting/index.html) -> Scroll to top of hub
                    new_href = '#'
                elif len(parts) >= 3:
                    # Nested service (e.g. /kendall-painting/exterior-painting/index.html)
                    # -> Return to parent city hub
                    parent_hub = parts[0] # 'kendall-painting'
                    new_href = f'/{parent_hub}/'
                    
                replacement_string = f"{{ label: 'Home', href: '{new_href}' }}"
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    if TARGET_STRING in content:
                        new_content = content.replace(TARGET_STRING, replacement_string)
                        if new_content != content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            updated_files += 1
                except Exception as e:
                    print(f"Error on {filepath}: {e}")
                    
    print("\nCONTEXTUAL NAVIGATION PATCH COMPLETE")
    print(f"Scanned: {scanned_files} HTML files")
    print(f"Patched: {updated_files} internal React 'Home' paths successfully.")

if __name__ == '__main__':
    patch_nav_home()
