import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

PAGE_DATA = {
    "index.html": {
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                TOP RATED <br />
                                <span className="text-gradient">
                                    PAINTING CONTRACTORS
                                </span> <br />
                                IN MIAMI FLORIDA.
                            </h1>""",
        "pattern": r'<h1.*?WE BRING.*?MIAMI VIBES.*?TO YOUR SPACE.*?</h1>'
    },
    "residential-painting.html": {
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                PREMIER <br />
                                <span className="text-gradient">
                                    RESIDENTIAL PAINTING
                                </span> <br />
                                CONTRACTORS IN MIAMI.
                            </h1>""",
        "pattern": r'<h1.*?WE TRANSFORM.*?MIAMI HOMES.*?INSIDE & OUT.*?</h1>'
    },
    "commercial-painting.html": {
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                EXPERT <br />
                                <span className="text-gradient">
                                    COMMERCIAL PAINTING
                                </span> <br />
                                SERVICES MIAMI FL.
                            </h1>""",
        "pattern": r'<h1.*?WE ELEVATE.*?MIAMI BUSINESSES.*?THROUGH COLOR.*?</h1>'
    },
    "exterior-painting.html": {
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                #1 RATED <br />
                                <span className="text-gradient">
                                    EXTERIOR PAINTERS
                                </span> <br />
                                MIAMI FLORIDA.
                            </h1>""",
        "pattern": r'<h1.*?WE SHIELD.*?YOUR PROPERTY.*?FROM THE ELEMENTS.*?</h1>'
    },
    "cabinet-refinishing.html": {
        "h1": """<h1 className="text-4xl sm:text-6xl lg:text-7xl font-black text-brand-dark tracking-tighter leading-[1] sm:leading-[0.9] mb-6 sm:mb-8 drop-shadow-sm">
                                PROFESSIONAL <br />
                                <span className="text-gradient">
                                    CABINET REFINISHING
                                </span> <br />
                                EXPERTS MIAMI.
                            </h1>""",
        "pattern": r'<h1.*?WE UPGRADE.*?MIAMI KITCHENS.*?FOR LESS.*?</h1>'
    }
}

def process_files():
    for filename, data in PAGE_DATA.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(data["pattern"], data["h1"], content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated H1 for: {filename}")
        else:
            print(f"Pattern not found in: {filename}")

if __name__ == "__main__":
    process_files()
