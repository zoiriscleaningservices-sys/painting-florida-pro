import os
import re

def inject_favicon(base_dir):
    count = 0
    errors = 0
    
    # We look for the existing 32x32 favicon link
    search_pattern = re.compile(r'<link\s+rel=["\']icon["\']\s+type=["\']image/png["\']\s+sizes=["\']32x32["\']\s+href=["\']/favicon\.png["\']\s*>\n?', re.IGNORECASE)
    
    # New compliant favicon tags
    new_favicon_tags = '<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">\n<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">\n'
    
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            if not file.endswith('.html'):
                continue
            
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                
                # Replace the old tag with the new tags
                content = search_pattern.sub(new_favicon_tags, content, count=1)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                errors += 1
                
    print(f"✅ Successfully patched {count} HTML files with compliant favicon tags.")
    if errors > 0:
        print(f"⚠️ Encountered {errors} errors during processing.")

if __name__ == '__main__':
    inject_favicon(r'.')
