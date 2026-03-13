import os
import shutil
import glob
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

def migrate_and_update_links():
    # 1. Gather all HTML files in the base directory
    all_html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    
    # Files to ignore during the move process (we want index.html to stay at the root)
    # Also ignore our terms/privacy pages if they exist, or anything else that should stay top level.
    # The user specifically requested this for the service/location silos.
    FILES_TO_MOVE = [f for f in all_html_files if os.path.basename(f) != "index.html"]

    # 2. Iterate and create folders, then move
    for filepath in FILES_TO_MOVE:
        filename = os.path.basename(filepath)
        folder_name = filename.replace(".html", "") # e.g., "exterior-painting"
        
        target_folder = os.path.join(BASE_DIR, folder_name)
        target_path = os.path.join(target_folder, "index.html")

        # Create folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)
        
        # Move and rename the file
        shutil.move(filepath, target_path)
        print(f"Moved: {filename} -> {folder_name}/index.html")

    # 3. Now we must update ALL internal links in ALL html files (including the newly moved ones and the root index)
    # Re-gather all HTML files (they are now in subfolders + root)
    all_new_html_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
    
    for filepath in all_new_html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # We are looking for anything linking to: `href="/something.html"` or `href="something.html"`
        # We want to change those to `href="/something/"` so it loads the index.html inside that folder
        
        # href="[optional /][any page name].html"
        # Group 1: Quote (' or ")
        # Group 2: The actual page name without leading slash or .html
        pattern = r'href=([\'"])/?([a-zA-Z0-9_-]+)\.html\1'
        
        def link_replacer(match):
            full_match = match.group(0) # e.g. href="/residential-painting.html"
            quote = match.group(1)      # e.g. "
            page_name = match.group(2)  # e.g. residential-painting
            
            # If the link is strictly going to index.html, leave it alone.
            if page_name == "index":
                return f'href={quote}/index.html{quote}'
            
            # Return the new cleaned absolute path structure: href="/residential-painting/"
            return f'href={quote}/{page_name}/{quote}'

        updated_content = re.sub(pattern, link_replacer, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Updated links inside: {os.path.relpath(filepath, BASE_DIR)}")

if __name__ == "__main__":
    migrate_and_update_links()
