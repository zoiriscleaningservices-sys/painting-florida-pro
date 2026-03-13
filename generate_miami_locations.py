import os
import random

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Root Miami/Broward Area Cities
ROOTS = [
    "Miami", "Hialeah", "Homestead", "Kendall", "Doral", "Aventura", "Coral Gables",
    "Pinecrest", "Palmetto Bay", "Cutler Bay", "South Miami", "Miami Lakes",
    "Miami Springs", "Sweetwater", "Opa-locka", "Miami Gardens", "North Miami",
    "North Miami Beach", "Sunny Isles Beach", "Surfside", "Bal Harbour", "Bay Harbor Islands",
    "Golden Beach", "Biscayne Park", "El Portal", "West Miami", "Virginia Gardens", 
    "Medley", "Hialeah Gardens", "Miami Shores", "Indian Creek", "Key Biscayne",
    
    # Broward spillover (very close proximity)
    "Miramar", "Pembroke Pines", "Hollywood", "Hallandale Beach", "Weston", 
    "Davie", "Cooper City", "Plantation", "Sunrise", "Tamarac", "Margate"
]

# Common local subdivision / neighborhood suffixes in South Florida
SUFFIXES = [
    "Estates", "Isles", "Lakes", "Gardens", "Park", "Springs", "Pines", "Woods",
    "Shores", "Ridge", "Oaks", "Cove", "Village", "Heights", "Terrace", "Manor",
    "Trails", "Crossing", "Point", "Key", "Bay", "Palms", "Grove", "Farms",
    "Ranch", "Meadows", "Hills", "View", "Landing"
]

# Additional specific Miami neighborhoods
NEIGHBORHOODS = [
    "Little Havana", "Little Haiti", "Allapattah", "Overtown", "Liberty City",
    "Edgewater", "Midtown", "Design District", "Buena Vista", "Upper Eastside",
    "Mimo District", "Grapeland Heights", "Flagami", "Coral Way", "Silver Bluff",
    "The Roads", "Shenandoah", "Brickell Hammock", "West Grove", "Brownsville",
    "Gladeview", "West Little River", "Pinewood", "Biscayne Gardens", "Ives Estates",
    "Ojus", "Aventura Isles", "Highland Lakes", "Richmond Heights", "Perrine",
    "Goulds", "Princeton", "Naranja", "Leisure City", "Florida City", "Redland",
    "The Hammocks", "Country Walk", "Crossings", "Kendale Lakes", "Olympia Heights",
    "Westwood Lakes", "Sunset", "Glenvar Heights", "Westchester", "Coral Terrace",
    "Fountainebleau", "Sweetwater", "Tamiami", "University Park"
]

def generate_1000_locations():
    locations = set()
    
    # 1. Add all roots (43)
    for root in ROOTS:
        locations.add(root)
        
    # 2. Add all specific neighborhoods (50)
    for nh in NEIGHBORHOODS:
        locations.add(nh)
        
    # 3. Generate combinatorial names (Root + Suffix) or (Direction + Root)
    directions = ["North", "South", "East", "West", "Upper", "Lower"]
    
    while len(locations) < 1000:
        roll = random.random()
        
        if roll < 0.6:
            # Root + Suffix (e.g., "Kendall Estates")
            loc = f"{random.choice(ROOTS)} {random.choice(SUFFIXES)}"
        elif roll < 0.8:
            # Direction + Root (e.g., "West Hialeah")
            loc = f"{random.choice(directions)} {random.choice(ROOTS)}"
        else:
            # Direction + Neighborhood
            loc = f"{random.choice(directions)} {random.choice(NEIGHBORHOODS)}"
            
        locations.add(loc)
        
    # Convert to sorted list and truncate exactly to 1000
    final_list = sorted(list(locations))[:1000]
    
    # Write to file
    out_path = os.path.join(BASE_DIR, "south_florida_locations.txt")
    with open(out_path, 'w', encoding='utf-8') as f:
        for loc in final_list:
            f.write(loc + "\n")
            
    print(f"Successfully generated {len(final_list)} localized South Florida service areas.")
    print(f"Output saved to: {out_path}")

if __name__ == "__main__":
    generate_1000_locations()
