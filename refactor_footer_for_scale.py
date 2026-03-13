import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

NEW_FOOTER_BLOCK = """<div className="flex flex-col items-center sm:items-start text-center sm:text-left h-full">
                                    <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-dark">SERVICE DIRECTORY</h4>
                                    <p className="text-brand-dark/70 text-xs mb-6 leading-relaxed max-w-xs">
                                        We aggressively serve all of Miami-Dade, Broward, and Palm Beach counties. We have established dedicated local service hubs in over 1,000 South Florida neighborhoods.
                                    </p>
                                    <a href="/areas-we-serve/" className="inline-flex items-center justify-center gap-3 bg-brand-dark text-brand-paper px-6 py-3 rounded-xl font-bold text-xs uppercase tracking-widest hover:bg-brand-orange hover:shadow-lg hover:shadow-brand-orange/20 transition-all duration-300 group mt-auto">
                                        View All 1,000+ Areas
                                        <div className="w-6 h-6 rounded-full bg-brand-paper/10 flex items-center justify-center group-hover:scale-110 transition-transform">
                                            <i data-lucide="arrow-right" className="w-3 h-3 text-brand-paper"></i>
                                        </div>
                                    </a>
                                </div>"""

def refactor_footers():
    updated = 0
    # The existing block is the 20-city grid: <div className="grid grid-cols-2 gap-x-4 gap-y-3 text-brand-dark/60 text-sm"> ... </div>
    pattern = re.compile(r'<h4 className="font-bold mb-8 text-sm uppercase tracking-widest text-brand-dark">SERVICES</h4>.*?<div className="grid grid-cols-2 gap-x-4 gap-y-3 text-brand-dark/60 text-sm">.*?</div>', re.DOTALL)
    
    # Just in case some have the older UL format still:
    pattern_ul = re.compile(r'<h4 className="font-bold mb-6 text-sm uppercase text-brand-dark">SERVICES</h4>.*?<ul className="space-y-4 text-brand-dark/60 text-sm">.*?</ul>', re.DOTALL)
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                has_changes = False
                
                if re.search(pattern, content):
                    content = re.sub(pattern, NEW_FOOTER_BLOCK, content)
                    has_changes = True
                elif re.search(pattern_ul, content):
                    content = re.sub(pattern_ul, NEW_FOOTER_BLOCK, content)
                    has_changes = True

                if has_changes:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated += 1
                    
    print(f"\nSuccessfully refactored the global footer in {updated} files to securely support the 1000-location Matrix.")

if __name__ == "__main__":
    refactor_footers()
