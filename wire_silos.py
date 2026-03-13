import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

HUBS = [
    "coral-gables-painting",
    "miami-beach-painting",
    "brickell-painting",
    "coconut-grove-painting"
]

def wire_silos():
    for hub in HUBS:
        # We need to update the HUB's index file, AND ALL of its 8 insulated child files
        # so that they ALL link exclusively to each other.
        # e.g., /brickell-painting/index.html MUST link to /brickell-painting/interior-painting/ rather than /interior-painting/
        
        hub_path = os.path.join(BASE_DIR, hub)
        hub_index = os.path.join(hub_path, "index.html")
        
        # All files we need to update within this silo:
        files_to_update = [hub_index]
        for service_folder in os.listdir(hub_path):
            service_path = os.path.join(hub_path, service_folder)
            if os.path.isdir(service_path):
                child_index = os.path.join(service_path, "index.html")
                if os.path.exists(child_index):
                    files_to_update.append(child_index)

        # Now update all of them to TRAP the user inside the silo
        for filepath in files_to_update:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Update the SERVICES React Grid
            # Old: href="/interior-painting/" 
            # New: href="/brickell-painting/interior-painting/"
            content = content.replace('href="/residential-painting/"', f'href="/{hub}/residential-painting/"')
            content = content.replace('href="/commercial-painting/"', f'href="/{hub}/commercial-painting/"')
            content = content.replace('href="/interior-painting/"', f'href="/{hub}/interior-painting/"')
            content = content.replace('href="/exterior-painting/"', f'href="/{hub}/exterior-painting/"')
            content = content.replace('href="/cabinet-refinishing/"', f'href="/{hub}/cabinet-refinishing/"')
            content = content.replace('href="/epoxy-flooring/"', f'href="/{hub}/epoxy-flooring/"')
            content = content.replace('href="/pressure-washing/"', f'href="/{hub}/pressure-washing/"')
            content = content.replace('href="/drywall-repair/"', f'href="/{hub}/drywall-repair/"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Insulated links inside: {os.path.relpath(filepath, BASE_DIR)}")

if __name__ == "__main__":
    wire_silos()
