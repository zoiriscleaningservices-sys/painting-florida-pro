import os
import re

def inject_seo(base_dir):
    site_url = "https://www.paintingfloridapros.com"
    count = 0
    errors = 0
    
    robots_meta = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n'
    
    for root, dirs, files in os.walk(base_dir):
        # Skip git and other non-content directories
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            # We only want to target HTML files
            if not file.endswith('.html'):
                continue
            
            filepath = os.path.join(root, file)
            
            # Calculate the canonical URL
            # Replace Windows backslashes with forward slashes for URLs
            rel_dir = os.path.relpath(root, base_dir).replace('\\', '/')
            
            if rel_dir == '.':
                if file == 'index.html':
                    canonical_url = f"{site_url}/"
                else:
                    canonical_url = f"{site_url}/{file}"
            else:
                if file == 'index.html':
                    canonical_url = f"{site_url}/{rel_dir}/"
                else:
                    canonical_url = f"{site_url}/{rel_dir}/{file}"

            canonical_tag = f'<link rel="canonical" href="{canonical_url}">\n'
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                
                # Clean out existing canonical and robots tags to prevent duplicates
                content = re.sub(r'<link\s+rel=["\']canonical["\'].*?>\n?', '', content, flags=re.IGNORECASE)
                content = re.sub(r'<meta\s+name=["\']robots["\'].*?>\n?', '', content, flags=re.IGNORECASE)
                
                # Insert the new tags exactly before </head>
                insertion = f'    {canonical_tag}    {robots_meta}</head>'
                content = re.sub(r'</head>', insertion, content, count=1, flags=re.IGNORECASE)
                
                # Only write back if actual changes happened (which should be true for all)
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                errors += 1
                print(f"Error processing {filepath}: {e}")
                
    print(f"✅ Successfully patched {count} HTML files with advanced SEO tags.")
    if errors > 0:
        print(f"⚠️ Encountered {errors} errors during processing.")

if __name__ == '__main__':
    # Execute injection exactly at the project root
    inject_seo(r'.')
