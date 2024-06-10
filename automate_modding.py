import os
import shutil
import gzip
import json

# Define paths and constants
user_name = 'your_windows_username'  # Replace with your Windows username
source_dir = rf'C:\Users\{user_name}\AppData\LocalLow\Mediatonic\FallGuys_client'
source_file = os.path.join(source_dir, 'content_v2.gdata')
working_dir = rf'C:\Users\{user_name}\downloads'
decoded_file = os.path.join(working_dir, 'contentmodding.gz')
json_file = os.path.join(working_dir, 'contentmodding.json')
xor_key = [0x61, 0x23, 0x21, 0x73, 0x43, 0x30, 0x2c, 0x2e]

def decode_file(input_file, output_file, key):
    content = bytearray()
    content_idx = 0

    try:
        with open(input_file, 'rb') as input_f:
            while (byte := input_f.read(1)):
                content += bytes([ord(byte) ^ key[content_idx % len(key)]])
                content_idx += 1
    except (IOError, OSError) as e:
        print('Error: could not read input file:', e)
        return False

    try:
        with open(output_file, 'wb') as output_f:
            output_f.write(content)
    except (IOError, OSError) as e:
        print('Error: could not create output file:', e)
        return False

    return True

def encode_file(input_file, output_file, key):
    return decode_file(input_file, output_file, key)

if not os.path.exists(json_file):
    # Step 1: Copy the content_v2 file to the working directory
    shutil.copy(source_file, working_dir)

    # Step 2: Decode the content_v2.gdata file
    if not decode_file(os.path.join(working_dir, 'content_v2.gdata'), decoded_file, xor_key):
        exit()

    # Step 3: Extract contentmodding.gz
    with gzip.open(decoded_file, 'rb') as f_in:
        with open(json_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Step 4: Format the extracted JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    formatted_json = json.dumps(json_data, indent=4)

    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(formatted_json)

    print(f"JSON file created: {json_file}")
else:
    # Step 5: Compress the modified JSON back into a .gz file
    with open(json_file, 'rb') as f_in:
        with gzip.open(decoded_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Step 6: Encode the modified contentmodding.gz back to content_v2.gdata
    if not encode_file(decoded_file, os.path.join(working_dir, 'content_v2.gdata'), xor_key):
        exit()

    # Step 7: Copy the modified content_v2.gdata back to the source directory
    shutil.copy(os.path.join(working_dir, 'content_v2.gdata'), source_dir)

    print("Process completed successfully!")
