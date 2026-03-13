import os
import datetime

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
DOMAIN = "https://paintingfloridapros.com"

SITEMAP_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""
SITEMAP_FOOTER = """\n</urlset>"""

def get_priority(url_path):
    # Root domain gets highest priority
    if url_path == "/":
        return "1.00"
        
    parts = [p for p in url_path.split("/") if p]
    
    # Hub pages (e.g. /doral-painting/) are highly important
    if len(parts) == 1:
        return "0.90"
        
    # Nested leaf service pages get standard priority
    return "0.80"

def build():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    urls = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Exclude git or hidden caches
        if '.git' in root or '.gemini' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                full_path = os.path.join(root, name)
                
                # We need to construct the relative URL
                rel_path = os.path.relpath(full_path, BASE_DIR)
                
                # Transform Windows path separators \ to Web /
                url_path = rel_path.replace("\\", "/")
                
                # Format rule: /index.html -> /
                if url_path == "index.html":
                    url_path = ""
                # Format rule: /doral-painting/index.html -> /doral-painting/
                elif url_path.endswith("/index.html"):
                    url_path = url_path.replace("index.html", "")
                    
                final_url = f"{DOMAIN}/{url_path}"
                priority = get_priority(f"/{url_path}")
                
                urls.append(f"""
    <url>
        <loc>{final_url}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>daily</changefreq>
        <priority>{priority}</priority>
    </url>""")
    
    # Write Srapmap
    sitemap_content = SITEMAP_HEADER + "".join(urls) + SITEMAP_FOOTER
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    
    with open(sitemap_path, "w", encoding='utf-8') as f:
        f.write(sitemap_content)
        
    print(f"Sitemap Generated at: {sitemap_path}")
    print(f"Total Pages Mapped: {len(urls)}")

if __name__ == '__main__':
    build()
