import os

files_to_check = [
    "main.py",
    "config.py",
    "requirements.txt",
    "Procfile",
    "handlers/__init__.py",
    "handlers/commands.py",
    "keyboards/__init__.py",
    "keyboards/inline.py",
    "utils/__init__.py",
    "utils/helpers.py",
]

print("Checking files...")
for file in files_to_check:
    if os.path.exists(file):
        print(f"✅ {file} exists")
    else:
        print(f"❌ {file} MISSING")
