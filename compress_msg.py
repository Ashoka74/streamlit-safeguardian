import msgpack
import gzip
import json

with open('configs/victim_json_template_flat_abbr.json', 'r') as f:
    victim_info = json.load(f)

def compress_json_msgpack(input_data, output_file):
    """
    Serializes data using MessagePack and compresses it with gzip.
    """
    # Serialize the data using MessagePack
    packed_data = msgpack.packb(input_data)
    # Compress the packed data
    with gzip.open(output_file, 'wb') as f:
        f.write(packed_data)

# Example usage
compress_json_msgpack(victim_info, 'victim_info_abbr.msgpack.gz')

# decode
with gzip.open('victim_info_abbr.msgpack.gz', 'rb') as f:
    # Read directly from the gzip file - no need for gzip.decompress()
    unpacked_data = msgpack.unpackb(f.read())
    print(unpacked_data)
