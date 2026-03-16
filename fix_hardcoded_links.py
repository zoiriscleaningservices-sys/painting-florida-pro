import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

def fix_hardcoded_links():
    updated_files = 0
    
    # We found that sub-service pages like 'west-shenandoah-painting/drywall-repair/index.html'
    # have hardcoded footer links that still end in -painting/ incorrectly:
    # <a href="/west-shenandoah-painting/epoxy-flooring-painting/"
    # <a href="/west-shenandoah-painting/pressure-washing-painting/"
    # <a href="/west-shenandoah-painting/drywall-repair-painting/"

    targets = [
        ('epoxy-flooring-painting/', 'epoxy-flooring/'),
        ('pressure-washing-painting/', 'pressure-washing/'),
        ('drywall-repair-painting/', 'drywall-repair/'),
        ('cabinet-refinishing-painting/', 'cabinet-refinishing/')
    ]

    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
            
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original = content
                    for bad, good in targets:
                        content = content.replace(bad, good)
                    
                    # Also there's one more case: The slider might be missing its replace string if it didn't match the huge regex
                    # The slider interpolation ends with:
                    # .replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')}
                    if ".replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')}" in content and ".replace('epoxy-flooring-painting/', 'epoxy-flooring/')" not in content:
                        content = content.replace(
                            ".replace('cabinet-refinishing-painting/', 'cabinet-refinishing/')}",
                            ".replace('cabinet-refinishing-painting/', 'cabinet-refinishing/').replace('epoxy-flooring-painting/', 'epoxy-flooring/').replace('pressure-washing-painting/', 'pressure-washing/').replace('drywall-repair-painting/', 'drywall-repair/')}"
                        )

                    if content != original:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated_files += 1
                        
                except Exception as e:
                    print(f"Error on {filepath}: {e}")

                if updated_files > 0 and updated_files % 1000 == 0:
                    print(f"Status: Updated {updated_files} files...")

    print(f"Complete. Fixed hardcoded HTML links in {updated_files} files sitewide.")

if __name__ == '__main__':
    fix_hardcoded_links()
