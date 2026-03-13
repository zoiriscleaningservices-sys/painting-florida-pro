import os
import re
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
DOMAIN = "https://www.paintingfloridapros.com"

def check_file(filepath):
    errors = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract all href attributes
    # Pattern looks for href="/something/" or href="https://..."
    links = re.findall(r'href=["\'](.*?)["\']', content)
    
    for link in links:
        # Ignore external links, mailto, tel, anchors
        if link.startswith("http") and DOMAIN not in link:
            continue
        if link.startswith(("mailto:", "tel:", "#")):
            continue
            
        # Strip domain if absolute
        if link.startswith(DOMAIN):
            link = link.replace(DOMAIN, "")
            
        # Resolution logic:
        # Example link: "/hialeah-painting/interior-painting/"
        # We need to test if BASE_DIR \ hialeah-painting \ interior-painting \ index.html exists
        
        # Clean the link
        clean_link = link.split('#')[0].split('?')[0]
        
        if clean_link == "" or clean_link == "/":
            # Points to root index.html
            target_path = os.path.join(BASE_DIR, "index.html")
        else:
            # Remove leading slash
            if clean_link.startswith("/"):
                clean_link = clean_link[1:]
                
            # Replace Web slashes with Windows backslashes
            local_rel = clean_link.replace("/", "\\")
            
            # The target could be a direct file (.html) or a folder (expecting index.html)
            if local_rel.endswith(".html"):
                target_path = os.path.join(BASE_DIR, local_rel)
            else:
                target_path = os.path.join(BASE_DIR, local_rel, "index.html")
                
        # Actually test existence
        if not os.path.exists(target_path):
            # Try to see if it's a raw directory without trailing slash
            fallback_dir = os.path.join(BASE_DIR, local_rel)
            if os.path.isdir(fallback_dir) and os.path.exists(os.path.join(fallback_dir, "index.html")):
                continue # It resolves to a folder index, so it's fine
                
            errors.append(f"BROKEN LINK in {os.path.relpath(filepath, BASE_DIR)}\n  => Target: {link} (Expected: {target_path})")
            
    return errors

def scan_matrix():
    all_html_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root:
            continue
        for f in files:
            if f.endswith(".html"):
                all_html_files.append(os.path.join(root, f))
                
    print(f"Crawler built. Scanning {len(all_html_files)} matrix pages...")
    
    total_errors = []
    
    # Multithreading for speed
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_file, all_html_files)
        for err_list in results:
            if err_list:
                total_errors.extend(err_list)
                
    if not total_errors:
        print("\nMATRIX INTEGRITY VERIFIED")
        print("0 Broken Links found across the entire architecture.")
    else:
        print(f"\nFOUND {len(total_errors)} BROKEN LINKS")
        with open(os.path.join(BASE_DIR, "broken_links_report.txt"), "w", encoding='utf-8') as f:
            for err in total_errors:
                f.write(err + "\n")
        print("Report saved to: broken_links_report.txt")
            
if __name__ == '__main__':
    scan_matrix()
