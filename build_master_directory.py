import os
import shutil

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
SOURCE_FILE = os.path.join(BASE_DIR, "index.html")
LOC_FILE = os.path.join(BASE_DIR, "south_florida_locations.txt")
DIR_PATH = os.path.join(BASE_DIR, "areas-we-serve")

def build_directory():
    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
        
    # Read the 1000 cities
    with open(LOC_FILE, 'r', encoding='utf-8') as f:
        cities = f.read().splitlines()
        
    # Build Alphabetical Groups
    alpha_groups = {}
    for city in sorted(cities):
        if not city.strip(): continue
        
        first_letter = city[0].upper()
        if first_letter not in alpha_groups:
            alpha_groups[first_letter] = []
        alpha_groups[first_letter].append(city)
        
    # Generate the Directory HTML Block
    dir_html = ""
    for letter in sorted(alpha_groups.keys()):
        dir_html += f"""
        <div className="mb-12">
            <h3 className="text-4xl font-black text-brand-dark mb-6 border-b-2 border-brand-orange/20 pb-2 inline-block pr-8">{letter}</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 gap-y-6">"""
            
        for city in alpha_groups[letter]:
            slug = city.lower().replace(" ", "-") + "-painting"
            dir_html += f"""
                <a href="/{slug}/" className="text-brand-dark/80 hover:text-brand-orange hover:translate-x-2 font-bold text-sm transition-all duration-300 flex items-center gap-2 group">
                    <div className="w-1.5 h-1.5 rounded-full bg-brand-orange/40 group-hover:bg-brand-orange transition-colors"></div>
                    {city}
                </a>"""
                
        dir_html += """
            </div>
        </div>"""

    # We will inject this directly into a cloned index page, wiping out the hero and services.
    target_file = os.path.join(DIR_PATH, "index.html")
    shutil.copy2(SOURCE_FILE, target_file)
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex out the <main> block and replace it with our custom directory
    import re
    main_pattern = re.compile(r'<main>.*?</main>', re.DOTALL)
    
    NEW_MAIN = f"""<main className="pt-32 pb-24 bg-brand-light min-h-screen">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
            <div className="text-center mb-16">
                <span className="text-brand-orange font-black tracking-[0.3em] text-xs sm:text-sm uppercase mb-4 block">FLORIDA LOCATIONS</span>
                <h1 className="text-5xl sm:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85] mb-8 text-brand-dark">
                    AREAS WE <span className="text-brand-orange">SERVE</span>
                </h1>
                <p className="max-w-2xl mx-auto text-brand-dark/70 text-lg">
                    Painting Florida Pros aggressively services over 1,000 distinct neighborhoods, zip codes, and municipalities across Miami-Dade, Broward, and Palm Beach counties. Select your local area below.
                </p>
            </div>
            
            <div className="bg-white rounded-3xl shadow-xl border border-brand-dark/5 p-8 sm:p-12 lg:p-16">
                {dir_html}
            </div>
        </div>
    </main>"""
    
    content = re.sub(main_pattern, NEW_MAIN, content)
    
    # Update Metadata
    content = content.replace("<title>Painting Florida Pros | Miami's Premier Painting Contractors</title>", 
                              "<title>Painters Near Me | 1,000+ South Florida Service Areas</title>")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Master Area Directory generated at: /areas-we-serve/index.html")


if __name__ == '__main__':
    build_directory()
