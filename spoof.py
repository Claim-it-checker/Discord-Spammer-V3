import os

def get_separator():
    """Reads the separator symbol from simble.txt"""
    try:
        with open("simble.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ Error: simble.txt not found! Create simble.txt and put a single separator symbol inside.")
        exit()

def rename_file():
    """Renames an existing file in the current directory to spoof its extension"""
    file_name = input("Enter the file you want to rename (must be in this directory): ").strip()

    if not os.path.exists(file_name):
        print(f"❌ Error: File '{file_name}' not found in the current directory!")
        return

    fake_ext = input("Fake file extension (e.g., txt): ").strip()

    separator = get_separator()
    name, ext = os.path.splitext(file_name)
    
    new_name = f"{name}{separator}{fake_ext}{ext}"
    
    os.rename(file_name, new_name)
    
    print(f"✅ File renamed to: {new_name}")

if __name__ == "__main__":
    rename_file()
