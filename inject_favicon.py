import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
FAVICON_TAG = '''<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>'''

def inject_favicon():
    updated = 0
    # Match the closing </head> tag case-insensitively
    head_pattern = re.compile(r'</head>', re.IGNORECASE)
    
    # Patterns to match existing favicons
    icon_pattern = re.compile(r'<link[^>]*rel=["\']icon["\'][^>]*>\n?', re.IGNORECASE)
    apple_icon_pattern = re.compile(r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>\n?', re.IGNORECASE)
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Always skip internal git or template caches
        if '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Skip if already injected to render script idempotent
                if '<link rel="icon" type="image/x-icon" href="/favicon.ico">' in content:
                    continue
                    
                # Remove any existing favicon tags to avoid duplicates
                content = re.sub(icon_pattern, '', content)
                content = re.sub(apple_icon_pattern, '', content)
                
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
