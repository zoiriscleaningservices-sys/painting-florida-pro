import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"
OUTPUT_FILE = os.path.join(BASE_DIR, "areas-we-serve", "index.html")

def build_master_directory():
    # 1. Dynamically read all physical hubs on disk
    locations = []
    
    for item in os.listdir(BASE_DIR):
        if item.endswith("-painting"):
            folder_path = os.path.join(BASE_DIR, item)
            if os.path.isdir(folder_path):
                # Ensure the index.html actually exists inside
                if os.path.exists(os.path.join(folder_path, "index.html")):
                    # Convert folder name 'coral-gables-painting' -> 'Coral Gables'
                    raw_name = item.replace("-painting", "")
                    city_name = " ".join(word.capitalize() for word in raw_name.split("-"))
                    locations.append((city_name, item))
                    
    locations.sort(key=lambda x: x[0])  # Alphabetize
    
    print(f"Discovered {len(locations)} physical location hubs on disk.")
    
    # 2. Build the HTML Grid payload
    grid_html = ""
    for loc_name, folder_name in locations:
        url_path = f"/{folder_name}/"
        grid_html += f"""
        <a href="{url_path}" class="block group">
            <div class="bg-brand-paper rounded-xl p-4 shadow-sm border border-gray-100 hover:border-brand-orange hover:shadow-md transition-all duration-300 flex items-center justify-between">
                <span class="font-medium text-brand-dark group-hover:text-brand-orange transition-colors">{loc_name}</span>
                <svg class="w-5 h-5 text-gray-400 group-hover:text-brand-orange transform group-hover:translate-x-1 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
            </div>
        </a>
        """

    # 3. Inject into the HTML Template
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Areas We Serve | Painting Florida Pros</title>
    <meta name="description" content="View the complete directory of cities, neighborhoods, and regions served by Painting Florida Pros across South Florida.">
    <link rel="icon" type="image/png" href="https://i.ibb.co/LdJySH38/956a318f-590e-48f6-a6ea-098fea818a4f-Picsart-Background-Remover.png">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=Outfit:wght@400;700;900&display=swap" rel="stylesheet">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            orange: '#F27D26',
                            yellow: '#FFD700',
                            blue: '#0056b3',
                            green: '#32CD32',
                            dark: '#000000',
                            light: '#F9F8F6',
                            paper: '#FFFFFF',
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-brand-light text-brand-dark font-sans antialiased overflow-x-hidden pt-24">

    <!-- Simple Header Navigation -->
    <header class="fixed top-0 w-full z-50 bg-brand-paper/90 backdrop-blur-md border-b border-gray-100 shadow-sm transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex-shrink-0 flex items-center space-x-2">
                    <img src="https://i.ibb.co/LdJySH38/956a318f-590e-48f6-a6ea-098fea818a4f-Picsart-Background-Remover.png" alt="Painting Florida Pros Logo" class="h-12 w-auto" />
                    <span class="font-heading font-black text-2xl tracking-tight text-brand-dark">PAINTING <span class="text-brand-orange">FLORIDA</span> PROS</span>
                </a>
                <a href="/" class="text-sm font-semibold text-brand-dark hover:text-brand-orange transition-colors">← Back to Home</a>
            </div>
        </div>
    </header>

    <!-- Header Section -->
    <section class="pt-16 pb-12 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="font-heading font-black text-5xl md:text-6xl text-brand-dark mb-6 tracking-tight">
                Areas We <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-orange to-brand-yellow">Serve</span>
            </h1>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
                We provide elite residential and commercial painting services across South Florida. Select your local area below to view dedicated services.
            </p>
        </div>
    </section>

    <!-- Master Grid -->
    <section class="py-16 bg-brand-light">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {grid_html}
            </div>
        </div>
    </section>

</body>
</html>
"""

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(template)
        
    print(f"Successfully generated Master Directory isolating {len(locations)} verified local hubs.")

if __name__ == '__main__':
    build_master_directory()
