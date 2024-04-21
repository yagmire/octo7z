import py7zr
import os
import argparse
from sys import exit

LZMA2 = py7zr.FILTER_LZMA2
LZMA = py7zr.FILTER_LZMA
DEFLATE = py7zr.FILTER_DEFLATE
COPY = py7zr.FILTER_COPY
ZSTANDARD = py7zr.FILTER_ZSTD
BROTLI = py7zr.FILTER_BROTLI
PPMD = py7zr.FILTER_PPMD

methods = ["LZMA2", "LZMA", "Bzip2", "Deflate", "Copy", "ZStandard", "Brotli", "PPMd"]

def octo_compress(method="LZMA2", target_dir=".", out_dir=".", name="compressed", header_enc=False):
    with py7zr.SevenZipFile(f'{out_dir}\\{name}.7z', 'w', password=args.password, header_encryption=header_enc) as archive:
        archive.writeall(target_dir)

parser = argparse.ArgumentParser(
    prog='Octo7z',
    epilog="profit??"
)

parser.add_argument('-c', '--compress', action='store_true') 
parser.add_argument('-C', '--decompress', action='store_true') 
parser.add_argument('-t', '--target_dir', action='store')  
parser.add_argument('-o', '--out_dir', action='store')  
parser.add_argument('-m', '--method', action='store')  
parser.add_argument('-n', '--name', action='store')
parser.add_argument('-p', '--password', action='store')  
parser.add_argument('-E', '--header_encrypt', action='store_true')  
parser.add_argument('-y', '--confirm', action='store_true')  
args = parser.parse_args()

if args.method not in methods or args.method == "":
    print("Not a valid method.")
    exit()

#print(args.target_dir)
if args.compress and args.decompress:
    print("Cannot compress and decompress at the same time.")
    exit()
elif args.compress == True:
    action='Compress'
elif args.decompress == True:
    action="Decompress"

print(f"Action: {action}\nTarget Directory: {args.target_dir}\nOutput Directory: {args.out_dir}\nMethod: {args.method}\nArchive Name: {args.name}\nHeader Encryption: {args.header_encrypt}\n")

if args.confirm == False:
    confirm = input("Is this correct? ")
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        if action == "Compress":
            # Do compress
            print("Compressing")
            octo_compress(args.method, args.target_dir, args.out_dir, args.name, args.header_encrypt)
        elif action == "Decompress":
            # Do decompress
            print("Decompressing")
    elif confirm.lower() == 'n' or confirm.lower() == 'no':
        exit()
    elif confirm.lower() != 'y' or confirm.lower() != 'yes' or confirm.lower() != 'n' or confirm.lower() != 'no':
        print("Invalid input. Expecting yes(y) or no(n).")
        exit()
else:
    if action == "Compress":
        # Do compress
        print("Compressing")
        octo_compress(args.method, args.target_dir, args.out_dir, args.name, args.header_encrypt)
    elif action == "Decompress":
        # Do decompress
        print("Decompressing")
