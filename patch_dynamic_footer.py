import os
import re
import random

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Regex pattern to capture the ENTIRE existing Footer component
FOOTER_REGEX = re.compile(
    r'const Footer = \(\) => \{.+?return \(.+?<footer.+?</footer>.+?\);.+?};',
    re.DOTALL
)

def get_all_hubs():
    """Scans the master directory for all active local Hub folders."""
    hubs = []
    
    # Exclude non-hub folders
    excludes = ['areas-we-serve', '.git', '.gemini']
    
    for item in os.listdir(BASE_DIR):
        if item in excludes: continue
        item_path = os.path.join(BASE_DIR, item)
        # Identify a valid hub by the presence of an active index.html and a structure like *-painting
        if os.path.isdir(item_path) and item.endswith("-painting"):
            if os.path.exists(os.path.join(item_path, 'index.html')):
                # Format name beautifully for display: 'kendall-painting' -> 'Kendall'
                display_name = item.replace("-painting", "").replace("-", " ").title()
                hubs.append({
                    "slug": item,
                    "name": display_name
                })
    return hubs

def build_mega_footer(hubs_list):
    """
    Constructs the React component string for the new 4-Column Mega Footer.
    It takes action to pull 5 random items from hubs_list to inject.
    """
    
    # Select 5 random active hubs for the dynamic cross-linking column
    dynamic_links = random.sample(hubs_list, min(5, len(hubs_list)))
    
    # Build the HTML output for those 5 links
    dynamic_column_html = ""
    for hub in dynamic_links:
        dynamic_column_html += f"""
                                    <li>
                                        <a href="/{hub['slug']}/" className="text-brand-dark/70 hover:text-brand-orange hover:translate-x-1 transition-all inline-block flex items-center gap-2 text-sm">
                                            <Icon name="MapPin" className="w-3 h-3 text-brand-orange" />
                                            {hub['name']} Painters
                                        </a>
                                    </li>"""

    # The colossal new 4-Column Footer Component Replacement String
    mega_footer = f"""const Footer = () => {{
            return (
                <footer className="py-16 sm:py-24 border-t border-brand-dark/10 bg-brand-light relative overflow-hidden">
                    <div className="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8 mb-16 sm:mb-24">
                            
                            {{/* Column 1: Brand & Bio */}}
                            <motion.div 
                                initial={{{{ opacity: 0, y: 30 }}}}
                                whileInView={{{{ opacity: 1, y: 0 }}}}
                                viewport={{{{ once: true }}}}
                                transition={{{{ duration: 0.8 }}}}
                            >
                                <motion.img whileHover={{{{ scale: 1.05, rotate: -2 }}}} src={{LOGO_URL}} alt="Logo" className="h-16 sm:h-20 w-auto object-contain mb-8 mx-auto sm:mx-0 cursor-pointer" />
                                <p className="text-brand-dark/70 mb-8 leading-relaxed text-sm">
                                    Painting Florida Pros is South Florida's elite residential and commercial coating contractor. 
                                    We aggressively defend your exterior against coastal elements and transform your interiors with perfect finishes.
                                </p>
                                <div className="flex gap-4 justify-center sm:justify-start">
                                    <motion.a whileHover={{{{ scale: 1.2, rotate: 15 }}}} whileTap={{{{ scale: 0.9 }}}} href="https://www.instagram.com/paintingfloridapros/" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-full bg-brand-dark/5 flex items-center justify-center text-brand-dark hover:bg-brand-orange hover:text-brand-paper transition-colors">
                                        <Icon name="Instagram" className="w-5 h-5" />
                                    </motion.a>
                                    <motion.a whileHover={{{{ scale: 1.2, rotate: -15 }}}} whileTap={{{{ scale: 0.9 }}}} href="https://x.com/paintingflpros" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-full bg-brand-dark/5 flex items-center justify-center text-brand-dark hover:bg-brand-orange hover:text-brand-paper transition-colors">
                                        <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current" xmlns="http://www.w3.org/2000/svg"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
                                    </motion.a>
                                    <motion.a whileHover={{{{ scale: 1.2, rotate: 15 }}}} whileTap={{{{ scale: 0.9 }}}} href="https://www.pinterest.com/paintingflorida/_profile/" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-full bg-brand-dark/5 flex items-center justify-center text-brand-dark hover:bg-brand-orange hover:text-brand-paper transition-colors">
                                        <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current" xmlns="http://www.w3.org/2000/svg"><path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.162-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.966 1.406-5.966s-.359-.72-.359-1.781c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.261 7.929-7.261 4.162 0 7.398 2.967 7.398 6.93 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146 1.124.347 2.317.535 3.554.535 6.607 0 11.985-5.365 11.985-11.987C23.97 5.39 18.592 0 12.017 0z"/></svg>
                                    </motion.a>
                                </div>
                            </motion.div>

                            {{/* Column 2: Core Services */}}
                            <motion.div 
                                initial={{{{ opacity: 0, y: 30 }}}}
                                whileInView={{{{ opacity: 1, y: 0 }}}}
                                viewport={{{{ once: true }}}}
                                transition={{{{ duration: 0.8, delay: 0.2 }}}}
                            >
                                <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-dark border-b border-brand-orange/20 pb-2 inline-block">Our Services</h4>
                                <ul className="space-y-4">
                                    {{SERVICES.map((s, i) => (
                                        <li key={{i}}>
                                            <a href="#services" className="text-brand-dark/70 hover:text-brand-orange hover:translate-x-1 transition-all inline-block flex items-center gap-2 text-sm">
                                                <Icon name="ChevronRight" className="w-3 h-3 text-brand-orange" />
                                                {{s.title}}
                                            </a>
                                        </li>
                                    ))}}
                                </ul>
                            </motion.div>

                            {{/* Column 3: Dynamic Nearby Locations (Spiderweb SEO) */}}
                            <motion.div 
                                initial={{{{ opacity: 0, y: 30 }}}}
                                whileInView={{{{ opacity: 1, y: 0 }}}}
                                viewport={{{{ once: true }}}}
                                transition={{{{ duration: 0.8, delay: 0.4 }}}}
                            >
                                <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-dark border-b border-brand-orange/20 pb-2 inline-block flex items-center gap-2">
                                    Geographic Range
                                </h4>
                                <ul className="space-y-4">
                                {dynamic_column_html}
                                </ul>
                                <div className="mt-8">
                                    <a href="/areas-we-serve/" className="inline-flex items-center justify-center gap-2 bg-brand-dark/5 text-brand-dark px-4 py-2 rounded-lg font-bold text-[10px] uppercase tracking-widest hover:bg-brand-orange hover:text-brand-paper transition-all duration-300 group">
                                        View All 1,000+ Areas
                                        <Icon name="ArrowRight" className="w-3 h-3 transition-transform group-hover:translate-x-1" />
                                    </a>
                                </div>
                            </motion.div>

                            {{/* Column 4: Contact & Trust Badges */}}
                            <motion.div 
                                initial={{{{ opacity: 0, y: 30 }}}}
                                whileInView={{{{ opacity: 1, y: 0 }}}}
                                viewport={{{{ once: true }}}}
                                transition={{{{ duration: 0.8, delay: 0.6 }}}}
                            >
                                <h4 className="font-bold mb-6 text-sm uppercase tracking-widest text-brand-dark border-b border-brand-orange/20 pb-2 inline-block">Contact & Trust</h4>
                                <div className="space-y-4 text-sm text-brand-dark/70 mb-8">
                                    <p className="flex items-start gap-3">
                                        <Icon name="MapPin" className="w-4 h-4 text-brand-orange shrink-0 mt-0.5" />
                                        Serving Miami-Dade, Broward, &<br/>Palm Beach Counties.
                                    </p>
                                    <p className="flex items-center gap-3">
                                        <Icon name="Phone" className="w-4 h-4 text-brand-orange shrink-0" />
                                        <strong>954-466-4652</strong>
                                    </p>
                                    <p className="flex items-center gap-3">
                                        <Icon name="Mail" className="w-4 h-4 text-brand-orange shrink-0" />
                                        paintingfloridapros@gmail.com
                                    </p>
                                    <p className="flex items-center gap-3">
                                        <Icon name="Clock" className="w-4 h-4 text-brand-orange shrink-0" />
                                        Licensed & Fully Insured
                                    </p>
                                </div>
                                <div className="flex gap-4">
                                    <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-md">
                                        <div className="text-brand-orange font-black text-xs leading-none text-center">5<br/>STAR</div>
                                    </div>
                                    <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-md pt-1">
                                        <Icon name="ShieldCheck" className="w-6 h-6 text-brand-green" />
                                    </div>
                                    <div className="h-12 bg-white rounded-full flex items-center justify-center outline-none shadow-md px-3 border border-brand-dark/5">
                                        <p className="text-[10px] font-bold text-center leading-tight">TOP<br/>RATED</p>
                                    </div>
                                </div>
                            </motion.div>

                        </div>

                        {{/* Bottom Copyright Bar */}}
                        <div className="pt-8 border-t border-brand-dark/10 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-medium text-brand-dark/40">
                            <p>© {{{{new Date().getFullYear()}}}} Painting Florida Pros. All rights reserved.</p>
                            <div className="flex gap-6">
                                <a href="#" className="hover:text-brand-orange transition-colors">Privacy Policy</a>
                                <a href="#" className="hover:text-brand-orange transition-colors">Terms of Service</a>
                            </div>
                        </div>
                    </div>
                </footer>
            );
        }};"""
    return mega_footer


def execute_global_footer_expansion():
    # 1. First, pull the array of all 774 active hubs so we can randomly sample from it later
    print("Indexing Active Geographic Hubs...")
    all_hubs = get_all_hubs()
    print(f"Found {len(all_hubs)} active Hubs (e.g. {all_hubs[0]['name']}).")
    
    updated_files = 0
    scanned_files = 0
    errors = []

    print("\nInitiating Phase 16: Mega Footer Component Swaps...")
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                scanned_files += 1
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Find where the old Footer component is
                    match = FOOTER_REGEX.search(content)
                    if match:
                        # 2. Build a unique mega footer specifically for this individual file (Randomizes the 5 cities)
                        new_mega_footer = build_mega_footer(all_hubs)
                        
                        # 3. Swap the old React Component string for the new Mega Footer string
                        new_content = FOOTER_REGEX.sub(new_mega_footer, content)
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                            
                        updated_files += 1
                except Exception as e:
                    errors.append(f"Failed to process {filepath} : {e}")
                    
    print("\n==============[ MEGA FOOTER DEPLOYMENT COMPLETE ]==============")
    print(f"Total HTML Scripts Scanned: {scanned_files}")
    print(f"Total Footers Dynamically Expanded: {updated_files}")
    if errors:
        print(f"\nErrors reported: {len(errors)}")

if __name__ == '__main__':
    execute_global_footer_expansion()
