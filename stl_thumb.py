#!/usr/bin/env python3

import subprocess
import sys
import tempfile


def main():
    if len(sys.argv) != 4:
        print(f"{sys.argv[0]}: usage: {sys.argv[0]} <input path> <output path> <size>", file=sys.stderr)
        return 1

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    size = sys.argv[3]

    with tempfile.NamedTemporaryFile() as f:
        f.write(f'import("{input_path}");\n'.encode('utf-8'))
        f.flush()
        subprocess.call(["openscad", "-o", output_path, "--export-format=png", f"--imgsize={size},{size}", f.name])

    return 0


if __name__ == '__main__':
    sys.exit(main())
