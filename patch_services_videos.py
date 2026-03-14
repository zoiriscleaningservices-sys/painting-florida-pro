import os
import re
import sys

def process_directory(directory):
    processed = 0
    errors = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith('.html'):
                continue
                
            filepath = os.path.join(root, file)
            
            # Calculate depth to determine correct relative path to videos/
            rel_path = os.path.relpath(directory, root)
            depth = 0 if rel_path == '.' else len(rel_path.split(os.sep))
            
            # The root directory has depth 0 (e.g., index.html)
            # A city directory has depth 1 (e.g., mobile-al/index.html) -> ../videos/
            # A city/service directory has depth 2 (e.g., mobile-al/residential-painting/index.html) -> ../../videos/
            if depth == 0:
                vid_prefix = 'videos/'
            else:
                vid_prefix = '../' * depth + 'videos/'

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = content
                
                # Replace Residential Painting image
                res_match = re.search(r'title:\s*"Residential Painting",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if res_match:
                    old_res_img = res_match.group(1)
                    new_content = new_content.replace(old_res_img, f'{vid_prefix}Ultra_Realistic_Video_Generation_Complete.mp4')
                    
                # Replace Commercial Property image
                com_match = re.search(r'title:\s*"Commercial Property",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if com_match:
                    old_com_img = com_match.group(1)
                    new_content = new_content.replace(old_com_img, f'{vid_prefix}67d8fc8a03d9428ec0b29c6f_67eb0de84444fe3be438db38_Commercial-Painting-transcode.mp4')
                    
                # Replace Interior Painting image
                int_match = re.search(r'title:\s*"Interior Painting",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if int_match:
                    old_int_img = int_match.group(1)
                    new_content = new_content.replace(old_int_img, f'{vid_prefix}Image_To_Live_Second_Video.mp4')
                    
                # Replace Epoxy Flooring image
                epx_match = re.search(r'title:\s*"Epoxy Flooring",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if epx_match:
                    old_epx_img = epx_match.group(1)
                    new_content = new_content.replace(old_epx_img, f'{vid_prefix}67d8fc8a03d9428ec0b29c6f_67eb0e0246c623902c3abd89_Concrete-Restoration-transcode.mp4')
                    
                # Replace Pressure Washing image
                pw_match = re.search(r'title:\s*"Pressure Washing",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if pw_match:
                    old_pw_img = pw_match.group(1)
                    new_content = new_content.replace(old_pw_img, f'{vid_prefix}67d8fc8a03d9428ec0b29c6f_67eb0e0c4444fe3be4391897_Pressure-Washing-transcode.mp4')
                    
                # Replace Drywall Repair image
                dw_match = re.search(r'title:\s*"Drywall Repair",.*?image:\s*"([^"]+)"', new_content, re.DOTALL)
                if dw_match:
                    old_dw_img = dw_match.group(1)
                    new_content = new_content.replace(old_dw_img, f'{vid_prefix}Last_Ultra_Realistic_Video_Generated.mp4')

                # Write changes if modified
                if content != new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    processed += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                errors += 1
                
    return processed, errors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = os.path.dirname(os.path.abspath(__file__))
        
    print(f"Starting replacement in {target_dir}")
    p, e = process_directory(target_dir)
    print(f"Operation complete. Updated {p} files. Errors: {e}")
