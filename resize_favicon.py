from PIL import Image
import os

def resize_favicon():
    try:
        # Open the original 640x640 image
        img = Image.open('favicon.png')
        
        # Google requires sizes that are multiples of 48px square.
        # Create 48x48 and 192x192 versions.
        
        # 48x48
        img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
        img_48.save('favicon-48x48.png')
        print("Successfully created favicon-48x48.png")
        
        # 192x192
        img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
        img_192.save('favicon-192x192.png')
        print("Successfully created favicon-192x192.png")
        
    except Exception as e:
        print(f"Error resizing favicon: {e}")

if __name__ == '__main__':
    resize_favicon()
