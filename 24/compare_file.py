import sys
import hashlib

def calc_file_hash(file_path):
    obj = hashlib.new("sha256")
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            obj.update(chunk)
    return obj.hexdigest()

def compare_files(file1, file2):
    hash1 = calc_file_hash(file1)
    hash2 = calc_file_hash(file2)
    return hash1 == hash2

def main():
    if len(sys.argv) < 2:
        print("Error")
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    print(compare_files(file1, file2))

if __name__ == "__main__":
    main()