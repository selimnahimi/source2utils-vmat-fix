import os, sys, re

def list_files(dir):
    found = []

    for path, _, files in os.walk(dir):
        for name in files:
            if (name.endswith(".vmat")):
                full_path = os.path.join(path, name)
                found.append(full_path)
    
    return found

def get_texturecolor(lines):
    for line in lines:
        if "TextureColor" in line:
            x = re.search("TextureColor \"(.+)\"", line)
            return x.group(1)
    
    return False

def check_detailtexture(content):
    if "TextureDetail" not in content:
        return False
    
    return True

def replace_detailtexture(lines, texturecolor):
    
    newlines = []
    
    for line in lines:
        if "TextureDetail" not in line:
            newlines.append(line)
        else:
            newlines.append("\tTextureDetail \"{0}\"".format(texturecolor))

    return newlines

def read_file(path):
    file = open(path)
    content = file.read()
    file.close()

    return content

def write_file(lines, path):
    file = open(path, "w")

    for line in lines:
        file.write(line + "\n")
    
    file.close()

vmat_files = []

file_paths = sys.argv[1:]  # the first argument is the script itself
for p in file_paths:
    print("Reading path: {0}".format(p))
    vmat_files += list_files(p)

for file in vmat_files:
    print("Processing {0}".format(file.split("/")[-1].split("\\")[-1]))

    content = read_file(file)
    if not check_detailtexture(content): continue

    lines = content.splitlines()
    
    texturecolor = get_texturecolor(lines)
    if texturecolor == False: continue

    newlines = replace_detailtexture(lines, texturecolor)

    write_file(newlines, file)

print("Done.")
