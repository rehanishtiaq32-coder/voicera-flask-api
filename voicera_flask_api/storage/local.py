import os, shutil

def save_upload(src_path: str, dest_dir: str) -> str:
    os.makedirs(dest_dir, exist_ok=True)
    filename = os.path.basename(src_path)
    dest = os.path.join(dest_dir, filename)
    if os.path.abspath(src_path) != os.path.abspath(dest):
        shutil.copyfile(src_path, dest)
    return dest
