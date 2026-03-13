import os
import re

# Define the base directory
BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Data structures for the 4 pages
PAGE_DATA = {
    "residential-painting.html": {
        "cta_text": "READY FOR A NEW INTERIOR?"
    },
    "commercial-painting.html": {
        "cta_text": "READY TO UPGRADE YOUR BUSINESS?"
    },
    "exterior-painting.html": {
        "cta_text": "READY TO PROTECT YOUR EXTERIOR?"
    },
    "cabinet-refinishing.html": {
        "cta_text": "READY FOR A NEW KITCHEN?"
    }
}

def process_files():
    for filename, data in PAGE_DATA.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Desktop Grid Button replacement using Regex
        desktop_pattern = r'<button className="inline-flex items-center gap-3 text-brand-orange font-black text-xs uppercase tracking-widest group/btn">.*?LEARN MORE.*?<div className="w-8 h-8 rounded-full border border-brand-orange/30 flex items-center justify-center group-hover/btn:bg-brand-orange group-hover/btn:text-brand-paper group-hover/btn:scale-125 transition-all">.*?<Icon name="ArrowRight" className="w-4 h-4" />.*?</div>.*?</button>'
        
        desktop_replacement = """<a href="#contact" className="inline-flex items-center gap-3 text-brand-orange font-black text-xs uppercase tracking-widest group/btn">
                                            LEARN MORE 
                                            <div className="w-8 h-8 rounded-full border border-brand-orange/30 flex items-center justify-center group-hover/btn:bg-brand-orange group-hover/btn:text-brand-paper group-hover/btn:scale-125 transition-all">
                                                <Icon name="ArrowRight" className="w-4 h-4" />
                                            </div>
                                        </a>"""
        
        content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
        
        # Mobile Slider Button replacement using Regex
        mobile_pattern = r'<motion\.button\s+whileHover=\{\{\s*scale:\s*1\.05\s*\}\}\s+whileTap=\{\{\s*scale:\s*0\.95\s*\}\}\s+className="bg-brand-orange text-brand-dark font-black px-8 py-4 rounded-2xl text-sm uppercase tracking-widest flex items-center gap-3 shadow-xl shadow-brand-orange/20"\s*>.*?LEARN MORE.*?<motion\.div animate=\{\{\s*x:\s*\[0,\s*5,\s*0\]\s*\}\}\s*transition=\{\{\s*repeat:\s*Infinity,\s*duration:\s*1\.5\s*\}\}>\s*<Icon name="ArrowRight" className="w-4 h-4" />\s*</motion\.div>\s*</motion\.button>'
        
        mobile_replacement = """<motion.a 
                                                        href="#contact"
                                                        whileHover={{ scale: 1.05 }}
                                                        whileTap={{ scale: 0.95 }}
                                                        className="bg-brand-orange text-brand-dark font-black px-8 py-4 rounded-2xl text-sm uppercase tracking-widest flex items-center gap-3 shadow-xl shadow-brand-orange/20 inline-flex"
                                                    >
                                                        LEARN MORE
                                                        <motion.div animate={{ x: [0, 5, 0] }} transition={{ repeat: Infinity, duration: 1.5 }}>
                                                            <Icon name="ArrowRight" className="w-4 h-4" />
                                                        </motion.div>
                                                    </motion.a>"""

        content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully fixed links: {filename}")

if __name__ == "__main__":
    process_files()
