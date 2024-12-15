def generate_standard_list() -> list:
    characters = [" ", ",", "."]
    characters.extend(map(str, range(10)))
    characters.extend(chr(i) for i in range(ord("a"), ord("z") + 1))  # Add 'a' to 'z'
    return characters


def write_table_to_disk(ft, output_file="frequency.txt") -> None:
    keys = generate_standard_list()
    fh = open(output_file, "w", encoding="utf-8")
    for key in keys:
        if key in ft:
            fh.write(f"{key}:{ft[key]}\n")
        else:
            fh.write(f"{key}:0\n")
    fh.close()
    return None


def write_encoded_text(data, output_file="compressed.bin") -> None:
    binary_data = int(data, 2).to_bytes((len(data) + 7) // 8, byteorder='big')
    with open(output_file, "wb") as fh:
        fh.write(binary_data)


def read_encoded_data():
    return ''

# write_encoded_text("1010101010")
