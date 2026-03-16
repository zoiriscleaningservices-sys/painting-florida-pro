import os
import re

BASE_DIR = r"c:\Users\lucia\OneDrive\Desktop\painting-florida-pro"

videos = [
    "Ultra_Realistic_Video_Generation_Complete.mp4",
    "67d8fc8a03d9428ec0b29c6f_67eb0de84444fe3be438db38_Commercial-Painting-transcode.mp4",
    "Image_To_Live_Second_Video.mp4",
    "67d8fc8a03d9428ec0b29c6f_67eb0e0246c623902c3abd89_Concrete-Restoration-transcode.mp4",
    "67d8fc8a03d9428ec0b29c6f_67eb0e0c4444fe3be4391897_Pressure-Washing-transcode.mp4",
    "Last_Ultra_Realistic_Video_Generated.mp4"
]

def map_images_to_videos():
    updated = 0
    # regex to find image: "https://images.unsplash.com/..."
    pattern = re.compile(r'image:\s*"https://images\.unsplash\.com/[^"]+"')

    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
        
        rel_path = os.path.relpath(root, BASE_DIR)
        
        # Calculate depth for video path resolution
        if rel_path == '.':
            depth = 0
            video_prefix = "videos/"
        else:
            length = len(rel_path.split(os.sep))
            depth = length
            video_prefix = "../" * depth + "videos/"
            
        for name in files:
            if name.endswith('.html'):
                filepath = os.path.join(root, name)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    if 'image: "https://images.unsplash.com/' not in content:
                        continue
                        
                    # Find all matches
                    matches = pattern.findall(content)
                    if not matches:
                        continue
                        
                    new_content = content
                    # We only replace the exact matches as we encounter them to map 1 to 1 sequentially
                    for i, match in enumerate(matches):
                        video_file = videos[i % len(videos)]
                        replacement = f'image: "{video_prefix}{video_file}"'
                        new_content = new_content.replace(match, replacement, 1) # replace one by one top down
                        
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated += 1
                        
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    
                if updated > 0 and updated % 1000 == 0:
                    print(f"Status: Updated {updated} files...")

    print(f"Complete. Updated {updated} files to use videos instead of images.")

if __name__ == '__main__':
    map_images_to_videos()
