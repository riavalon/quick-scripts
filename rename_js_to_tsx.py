import os
import shutil
import argparse

def get_all_files(flist, cwd, with_ext):
    os.chdir(cwd)
    new_list = []
    for f in flist:
        fabspath = os.path.abspath(f)
        if os.path.isdir(fabspath):
            new_list.extend(get_all_files(os.listdir(fabspath), fabspath, with_ext))
            os.chdir(cwd)
        else:
            new_list.append(fabspath)
    return [x for x in new_list if x.endswith(with_ext)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--src", type=str, default="./")
    parser.add_argument("-f", "--from-extension", type=str, default=".js")
    parser.add_argument("-t", "--to-extension", type=str, default=".tsx")
    
    parser.description = """
    Recursively finds all files in a directory and changes their extension.
    Defaults to finding `.js` files and converting them to `.tsx` files.
    Will look in the current working directory for files unless otherwise
    specified with the `-s` / `--src` flag.
    """

    args = parser.parse_args()

    filtered_files = get_all_files(os.listdir("./src"), os.path.abspath(args.src), args.from_extension)
    for fname in filtered_files:
        ext_idx = fname.index(args.from_extension)
        without_ext = fname[:ext_idx]
        renamed_file = without_ext + args.to_extension
        shutil.move(fname, renamed_file)