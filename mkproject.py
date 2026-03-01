#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def get_target_path(location):
    # Kamus sakti: Kumpulan typo dan shortcut yang dipetakan ke path asli
    shortcuts = {
        # Desktop & Typos
        'desktop': '~/Desktop', 'dekstop': '~/Desktop', 'destop': '~/Desktop',
        'desktp': '~/Desktop', 'sektop': '~/Desktop', 'dsktop': '~/Desktop',
        'dks': '~/Desktop', 'deks': '~/Desktop',
        
        # Downloads & Typos
        'downloads': '~/Downloads', 'download': '~/Downloads', 'donlod': '~/Downloads',
        'downlod': '~/Downloads', 'dwonlod': '~/Downloads', 'dwnld': '~/Downloads',
        'dl': '~/Downloads',
        
        # Documents & Typos
        'documents': '~/Documents', 'document': '~/Documents', 'dokumen': '~/Documents',
        'doc': '~/Documents', 'docs': '~/Documents', 'dok': '~/Documents',
        
        # Home
        'home': '~', 'hom': '~'
    }
    
    loc_lower = location.strip().lower()
    # Kalau input ada di kamus, ambil path aslinya. Kalau nggak ada, pakai input aslinya.
    path_str = shortcuts.get(loc_lower, location)
    return Path(path_str).expanduser().resolve()


def build_structure(blueprint, base_path):
    lines = blueprint.strip().split('\n')
    stack = [(-1, base_path)] 

    for line in lines:
        if not line.strip(): 
            continue

        if '#' in line:
            line = line.split('#')[0]
        line = line.rstrip()

        match = re.search(r'[^\s│├─└]', line)
        if not match: 
            continue
            
        indent = match.start()
        name_raw = line[indent:].strip()

        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()

        parent_path = stack[-1][1]
        
        is_dir = name_raw.startswith('/') or name_raw.endswith('/')
        clean_name = name_raw.strip('/')
        
        if not clean_name:
            continue

        current_path = parent_path / clean_name

        if is_dir:
            current_path.mkdir(parents=True, exist_ok=True)
            stack.append((indent, current_path))
            print(f"  [+] Dir  : {current_path.relative_to(base_path.parent)}")
        else:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            current_path.touch(exist_ok=True)
            print(f"  [-] File : {current_path.relative_to(base_path.parent)}")


if __name__ == "__main__":
    print("=== mkproject bot ===")
    
    # --- 1. LOOP KONFIRMASI LOKASI ---
    while True:
        loc_input = input("\n📁 Lokasi target (desktop/downloads/dll): ").strip()
        if not loc_input:
            loc_input = "."
            
        target_dir = get_target_path(loc_input)
        
        # Tanya konfirmasi (Default Y kalau cuma di-Enter)
        confirm_loc = input(f"    Maksudnya di '{target_dir}'? [Y/n]: ").strip().lower()
        if confirm_loc in ['', 'y', 'yes']:
            break # Lanjut ke tahap berikutnya kalau Yes
        else:
            print("    [!] Oke, mari kita ulang input lokasinya.")

    # --- 2. LOOP KONFIRMASI NAMA PROJECT ---
    while True:
        project_name = input("\n📦 Nama project: ").strip()
        if not project_name:
            print("    [!] Nama project tidak boleh kosong.")
            continue
            
        project_path = target_dir / project_name
        
        # Tanya konfirmasi
        confirm_proj = input(f"    Buat project '{project_name}' di dalam '{target_dir}'? [Y/n]: ").strip().lower()
        if confirm_proj in ['', 'y', 'yes']:
            break # Lanjut ke tahap berikutnya kalau Yes
        else:
            print("    [!] Oke, silakan ketik ulang nama project-nya.")

    # Buat folder utama project-nya sekarang
    project_path.mkdir(parents=True, exist_ok=True)

    # --- 3. INPUT BLUEPRINT ---
    print("\n📝 Masukkan blueprint:")
    print("   (Tekan Enter, lalu tekan Ctrl+D untuk eksekusi)")
    blueprint_content = sys.stdin.read()
    
    if not blueprint_content.strip():
        print("\n❌ Error: Blueprint kosong. Membatalkan proses.")
        sys.exit(1)

    # --- 4. EKSEKUSI ---
    print("\n🚀 [mkproject] Membangun struktur...")
    build_structure(blueprint_content, project_path)
    print(f"\n✅ [mkproject] Selesai! Project siap di: {project_path}")