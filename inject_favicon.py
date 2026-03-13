import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
FAVICON_TAG = '<link rel="icon" type="image/png" href="https://i.ibb.co/LdJySH38/956a318f-590e-48f6-a6ea-098fea818a4f-Picsart-Background-Remover.png">\n</head>'

def inject_favicon():
    updated = 0
    # Match the closing </head> tag case-insensitively
    head_pattern = re.compile(r'</head>', re.IGNORECASE)
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Always skip internal git or template caches
        if '.git' in root or '.gemini' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Skip if already injected to render script idempotent
                if 'rel="icon"' in content and 'Picsart-Background-Remover.png' in content:
                    continue
                    
                if re.search(head_pattern, content):
                    # Replace the existing </head> with the favicon + </head>
                    new_content = re.sub(head_pattern, FAVICON_TAG, content, count=1)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    updated += 1
                    
                if updated > 0 and updated % 1000 == 0:
                    print(f"Status: Injected favicon into {updated} pages...")

    print(f"\n✅ FAVICON DEPLOYMENT COMPLETE")
    print(f"Successfully injected the logo favicon into {updated} HTML files.")

if __name__ == '__main__':
    inject_favicon()
