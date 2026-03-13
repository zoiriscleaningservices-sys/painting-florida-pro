import os

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

# Shared Constants (Top part)
CHUNK_1 = """                    <h1 style="color: #F27D26;">Oops! Something went wrong.</h1>
                    <p>${message}</p>
                    <button onclick="location.reload()" style="background: #F27D26; color: black; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Reload Page</button>
                </div>`;
            }
        };

        const { useState, useEffect, useRef } = React;
        
        // Framer Motion UMD export is often 'Motion' or 'framerMotion'
        const motion = window.Motion?.motion || window.framerMotion?.motion || (({ children, ...props }) => <div {...props}>{children}</div>);
        const AnimatePresence = window.Motion?.AnimatePresence || window.framerMotion?.AnimatePresence || (({ children }) => <>{children}</>);

        // --- Constants ---
        const LOGO_URL = "https://i.ibb.co/LdJySH38/956a318f-590e-48f6-a6ea-098fea818a4f-Picsart-Background-Remover.png";

        const NAV_ITEMS = [
            { label: 'Home', href: 'index.html' },
            { label: 'Services', href: '#services' },
            { label: 'Contact', href: '#contact' },
        ];
"""

# Services for each page
SERVICES_DATA = {
    "index.html": """        const SERVICES = [
            {
                title: "Residential Painting",
                description: "Transform your home with vibrant colors and flawless finishes that last for years.",
                icon: "Paintbrush",
                image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Commercial Property",
                description: "Professional painting solutions for Miami businesses, offices, retail spaces, and heavy industrial complexes.",
                icon: "Building2",
                image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4"
            },
            {
                title: "Interior Design",
                description: "Expert color consultation and precision interior painting for every room.",
                icon: "Palette",
                image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Exterior Protection",
                description: "Weather-resistant coatings designed specifically to withstand harsh Miami sun, salt air, and heavy humidity.",
                icon: "Shield",
                image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Cabinet Refinishing",
                description: "Give your kitchen a factory-new look with our specialized cabinet painting process.",
                icon: "Layers",
                image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800"
            },
            {
                title: "Industrial Coatings",
                description: "High-performance epoxy and protective coatings for heavy-duty environments.",
                icon: "Zap",
                image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800"
            }
        ];
""",
    "residential-painting.html": """        const SERVICES = [
            { title: "Interior House Painting", description: "Flawless luxury finishes for living rooms, bedrooms, and entire home interiors.", icon: "Paintbrush", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Exterior Protection", description: "Weather-resistant coatings designed specifically to withstand harsh Miami sun and humidity.", icon: "Shield", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Kitchen Cabinets", description: "Give your kitchen a factory-new look with our specialized cabinet painting process.", icon: "Layers", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Drywall Repair", description: "Seamless patching and blending for water damage, cracks, and everyday wear and tear.", icon: "Wrench", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Wood Staining", description: "Enhance and protect exterior decks, fences, and pergolas from absolute sun decay.", icon: "Sun", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Color Consultation", description: "Expert design advice to pick the perfect palette for your Miami home's natural lighting.", icon: "Palette", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];
""",
    "commercial-painting.html": """        const SERVICES = [
            { title: "Office & Retail", description: "Low-odor, rapid-dry painting to keep your Miami storefront or office running smoothly.", icon: "Building", image: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=800" },
            { title: "High-Rise Exteriors", description: "Fully insured and equipped for complex, multi-story condominium and hotel painting.", icon: "Building2", image: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=800" },
            { title: "Industrial Epoxies", description: "Heavy-duty floor coatings for warehouses, showrooms, and manufacturing facilities.", icon: "Layers", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Anti-Graffiti", description: "Protective clear coats that allow you to easily wash away vandalism and tagging.", icon: "ShieldAlert", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "HOA Communities", description: "Large-scale cohesive painting plans for Miami-Dade townhomes and community associations.", icon: "Home", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Warehouse Coatings", description: "Direct-to-metal (DTM) paints and rust-inhibitive primers for structural steel.", icon: "Zap", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];
""",
    "exterior-painting.html": """        const SERVICES = [
            { title: "Elastomeric Coating", description: "Thick, flexible waterproofing bridge that seals hairline stucco cracks from driving rain.", icon: "ShieldCheck", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Stucco Repair", description: "Expert patching and texturing to match your home's existing block or frame construction.", icon: "Wrench", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Coastal Proofing", description: "100% acrylic UV-resistant paints specifically formulated to combat fading and salt air.", icon: "Sun", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Power Washing", description: "High-PSI removal of chalking, mold, mildew, and salt residue prior to painting.", icon: "Droplets", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Trim & Fascia", description: "Detail-oriented painting of soffits, gutters, and trim for sharp architectural contrast.", icon: "Mails", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Deck Staining", description: "Deep penetrating oils to protect your pool deck and wooden patios from water rot.", icon: "Layers", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];
""",
    "cabinet-refinishing.html": """        const SERVICES = [
            { title: "Solid Color Conversion", description: "Transform outdated dark oak or cherry wood into modern, bright white or custom colors.", icon: "Palette", image: "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&q=80&w=800" },
            { title: "Factory Finish", description: "Sprayed industrial-grade urethane enamels for a hard, smooth, chip-resistant shell.", icon: "Shield", image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80&w=800" },
            { title: "Custom Built-ins", description: "Refinishing for library shelves, entertainment centers, and custom closet millwork.", icon: "LayoutTemplate", image: "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&q=80&w=800" },
            { title: "Vanity Refinishing", description: "Moisture-resistant bathroom vanity upgrades that withstand high Florida humidity.", icon: "Thermometer", image: "https://images.unsplash.com/photo-1595844730298-b960ff98fee0?auto=format&fit=crop&q=80&w=800" },
            { title: "Hardware Upgrades", description: "Drilling and filling for brand new handle and pull placements to complete the modern look.", icon: "Wrench", image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=800" },
            { title: "Stain Blocking", description: "Heavy-duty shellac and oil primers to guarantee dark wood tannins never bleed through.", icon: "XCircle", image: "https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" }
        ];
"""
}

# The Navbar and start of Hero (before the H1 tag)
CHUNK_3 = """
        // --- Helper Components ---
        const Icon = ({ name, className }) => {
            useEffect(() => {
                if (window.lucide) {
                    window.lucide.createIcons();
                }
            }, [name]);
            return <i data-lucide={name.toLowerCase()} className={className}></i>;
        };

        const Navbar = () => {
            const [isOpen, setIsOpen] = useState(false);
            const [scrolled, setScrolled] = useState(false);

            useEffect(() => {
                const handleScroll = () => setScrolled(window.scrollY > 50);
                window.addEventListener('scroll', handleScroll);
                return () => window.removeEventListener('scroll', handleScroll);
            }, []);

            useEffect(() => {
                if (isOpen) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = 'unset';
                }
            }, [isOpen]);

            const scrollToContact = (e) => {
                e.preventDefault();
                const contactSection = document.getElementById('contact');
                if (contactSection) {
                    contactSection.scrollIntoView({ behavior: 'smooth' });
                    setIsOpen(false);
                }
            };

            const menuVariants = {
                closed: {
                    y: "-100%",
                    transition: {
                        type: "spring",
                        stiffness: 300,
                        damping: 30,
                        staggerChildren: 0.05,
                        staggerDirection: -1
                    }
                },
                open: {
                    y: 0,
                    transition: {
                        type: "spring",
                        stiffness: 300,
                        damping: 30,
                        staggerChildren: 0.1,
                        delayChildren: 0.2
                    }
                }
            };

            const itemVariants = {
                closed: { opacity: 0, y: 20 },
                open: { opacity: 1, y: 0 }
            };

            return (
                <>
                    <nav className={`fixed top-0 left-0 w-full transition-all duration-500 ${isOpen ? 'z-[110] bg-transparent' : 'z-50 ' + (scrolled ? 'bg-brand-paper/95 backdrop-blur-xl py-3 sm:py-4 border-b border-brand-dark/10' : 'bg-transparent py-6 sm:py-8')}`}>
                    <div className="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between">
                        <a href="index.html" className="flex items-center gap-3">
                            <img src={LOGO_URL} alt="Logo" className="h-10 sm:h-16 w-auto object-contain" />
                        </a>

                        <div className="hidden lg:flex items-center gap-8">
                            {NAV_ITEMS.map((item, idx) => (
                                <motion.a 
                                    key={item.label} 
                                    href={item.href}
                                    initial={{ opacity: 0, y: -20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: idx * 0.1, type: "spring", stiffness: 300 }}
                                    whileHover={{ scale: 1.1, y: -2, color: '#F27D26' }}
                                    whileTap={{ scale: 0.95 }}
                                    className="text-sm font-medium text-brand-dark hover:text-brand-orange transition-colors"
                                >
                                    {item.label}
                                </motion.a>
                            ))}
                        </div>

                        <div className="hidden lg:block">
                            <motion.button 
                                initial={{ opacity: 0, scale: 0.8 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: 0.4, type: "spring", bounce: 0.5 }}
                                whileHover={{ scale: 1.05, boxShadow: "0px 10px 20px rgba(242, 125, 38, 0.4)", rotate: [0, -2, 2, -2, 0] }}
                                whileTap={{ scale: 0.95 }}
                                onClick={scrollToContact}
                                className="bg-brand-orange hover:bg-brand-yellow text-brand-dark font-bold px-8 py-3 rounded-full transition-all shadow-lg shadow-brand-orange/20"
                            >
                                GET A QUOTE
                            </motion.button>
                        </div>

                        <button className="lg:hidden text-brand-dark p-2 z-[120] relative" onClick={() => setIsOpen(!isOpen)}>
                            {isOpen ? <Icon name="X" className="w-8 h-8" /> : <Icon name="Menu" className="w-8 h-8" />}
                        </button>
                    </div>
                </nav>

                <AnimatePresence>
                    {isOpen && (
                        <motion.div 
                            variants={menuVariants}
                            initial="closed"
                            animate="open"
                            exit="closed"
                            className="fixed inset-0 bg-brand-light z-[100] lg:hidden flex flex-col pt-32 pb-12 px-8 sm:px-12"
                            style={{ backgroundColor: '#F9F8F6', opacity: 1 }}
                        >
                                <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none opacity-40">
                                    <div className="absolute top-[-10%] right-[-10%] w-[80%] h-[80%] bg-brand-orange/20 blur-[150px] rounded-full" />
                                    <div className="absolute bottom-[-10%] left-[-10%] w-[70%] h-[70%] bg-brand-blue/20 blur-[150px] rounded-full" />
                                </div>

                                <div className="flex flex-col gap-6 relative z-10">
                                    {NAV_ITEMS.map((item, idx) => (
                                        <motion.a 
                                            key={item.label} 
                                            variants={itemVariants}
                                            href={item.href} 
                                            onClick={() => setIsOpen(false)} 
                                            className="text-5xl sm:text-7xl font-black text-brand-dark hover:text-brand-orange transition-colors tracking-tighter leading-none"
                                        >
                                            <span className="text-brand-orange/60 mr-4 text-2xl sm:text-3xl font-mono">0{idx + 1}</span>
                                            {item.label}
                                        </motion.a>
                                    ))}
                                </div>

                                <motion.div variants={itemVariants} className="mt-12 relative z-10">
                                    <button 
                                        onClick={scrollToContact}
                                        className="w-full bg-brand-orange text-brand-dark font-bold py-6 rounded-3xl text-2xl shadow-2xl shadow-brand-orange/30 active:scale-95 transition-transform"
                                    >
                                        GET A QUOTE
                                    </button>
                                </motion.div>

                                <motion.div variants={itemVariants} className="mt-auto flex flex-col gap-8 relative z-10">
                                    <div className="h-px w-full bg-brand-dark/10" />
                                    <div className="flex justify-between items-end">
                                        <div className="space-y-2">
                                            <p className="text-xs font-bold text-brand-dark/60 uppercase tracking-widest">Connect with us</p>
                                            <div className="flex gap-6">
                                                <a href="https://www.instagram.com/paintingfloridapros/" target="_blank" rel="noopener noreferrer" className="text-brand-dark hover:text-brand-orange transition-colors">
                                                    <Icon name="Instagram" className="w-8 h-8" />
                                                </a>
                                                <a href="https://x.com/paintingflpros" target="_blank" rel="noopener noreferrer" className="text-brand-dark hover:text-brand-orange transition-colors">
                                                    <svg viewBox="0 0 24 24" className="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
                                                </a>
                                                <a href="https://www.pinterest.com/paintingflorida/_profile/" target="_blank" rel="noopener noreferrer" className="text-brand-dark hover:text-brand-orange transition-colors">
                                                    <svg viewBox="0 0 24 24" className="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg"><path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.162-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.966 1.406-5.966s-.359-.72-.359-1.781c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.261 7.929-7.261 4.162 0 7.398 2.967 7.398 6.93 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146 1.124.347 2.317.535 3.554.535 6.607 0 11.985-5.365 11.985-11.987C23.97 5.39 18.592 0 12.017 0z"/></svg>
                                                </a>
                                            </div>
                                        </div>
                                        <img src={LOGO_URL} alt="Logo" className="h-20 w-auto opacity-100" />
                                    </div>
                                </motion.div>
                            </motion.div>
                        )}
                </AnimatePresence>
                </>
            );
        };

        const Hero = () => {
            const scrollToContact = () => {
                const contactSection = document.getElementById('contact');
                if (contactSection) {
                    contactSection.scrollIntoView({ behavior: 'smooth' });
                }
            };

            return (
                <section className="relative min-h-screen flex items-center pt-24 pb-12 sm:pt-20 overflow-hidden bg-brand-light">
                    {/* Background Video with Overlay */}
                    <div className="absolute inset-0 z-0">
                        <video 
                            autoPlay 
                            loop 
                            muted 
                            playsInline
                            className="w-full h-full object-cover opacity-80"
                        >
                            <source src="https://cdn.prod.website-files.com/67d8fc8a03d9428ec0b29c6f%2F67eb0fa936122199232474d0_Coastal-Painting-Header-Small-transcode.mp4" type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                        <div className="absolute inset-0 bg-gradient-to-b from-brand-light/10 via-brand-light/30 to-brand-light/90" />
                    </div>

                    <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col items-center text-center relative z-10">
                        <motion.div 
                            initial={{ opacity: 0, y: 30 }} 
                            animate={{ opacity: 1, y: 0 }} 
                            transition={{ duration: 0.8 }}
                            className="max-w-4xl"
                        >
                            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-brand-orange/10 border border-brand-orange/20 text-brand-orange text-xs sm:text-sm font-bold mb-6 sm:mb-8">
                                <Icon name="Star" className="w-4 h-4 text-brand-orange fill-brand-orange" />
"""

TAG_DATA = {
    "index.html": "MIAMI'S #1 RATED PAINTING CONTRACTORS",
    "residential-painting.html": "MIAMI'S ELITE RESIDENTIAL PAINTERS",
    "commercial-painting.html": "MIAMI'S PREMIER COMMERCIAL CONTRACTORS",
    "exterior-painting.html": "MIAMI'S TOP EXTERIOR COATING EXPERTS",
    "cabinet-refinishing.html": "MIAMI'S LEADING KITCHEN REFINISHERS"
}

def fix_files():
    for f in SERVICES_DATA.keys():
        filepath = os.path.join(BASE_DIR, f)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # The target signature where the file is currently torn.
        # `<div style="color: white; padding: 20px; text-align: center;">`
        
        target = '<div style="color: white; padding: 20px; text-align: center;">'
        if target in content:
            idx = content.find(target)
            
            # Keep up to the target string INCLUDING the target string itself.
            top_half = content[:idx] + target + "\n"
            
            # The bottom half exists right after the target.
            bottom_half = content[idx + len(target):]
            
            # The missing block
            missing_block = CHUNK_1 + SERVICES_DATA[f] + CHUNK_3 + f"                                {TAG_DATA[f]}\n                            </div>\n"
            
            # Stitch them together
            fixed_content = top_half + missing_block + bottom_half
            
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(fixed_content)
                
            print(f"Fixed {f}")
        else:
            print(f"Target not found in {f}")

if __name__ == "__main__":
    fix_files()
