# START from https://stackoverflow.com/a/21153007/1098332
import math, struct

mult4 = lambda n: int(math.ceil(n/4))*4
mult8 = lambda n: int(math.ceil(n/8))*8
lh = lambda n: struct.pack("<h", n)
li = lambda n: struct.pack("<i", n)

def bmp(rows, w):
    h, wB = len(rows), int(mult8(w)/8)
    s, pad = li(mult4(wB)*h+0x20), [0]*(mult4(wB)-wB)
    s = li(mult4(w)*h+0x20)
    return (b"BM" + s + b"\x00\x00\x00\x00\x20\x00\x00\x00\x0C\x00\x00\x00" +
            lh(w) + lh(h) + b"\x01\x00\x01\x00\xff\xff\xff\x00\x00\x00" +
            b"".join([bytes(row+pad) for row in reversed(rows)]))
# END from https://stackoverflow.com/a/21153007/1098332

def convert_raw_to_bitmap(rawdata):
    blen = len(rawdata)
    Blen = blen * 8 
    bw = int(math.sqrt(Blen))
    bw -= bw % 8
    truncate_to = (bw**2)//8

    print(f"Ignoring last {len(rawdata) - truncate_to} bytes")
    print(f"Making a {bw}x{bw} monochrome bitmap image")
    Bw=bw//8
    rows=[list(rawdata[i*Bw:(i+1)*Bw]) for i in range(0, bw)]

    return bmp(rows, bw)



def Main(input, output):
    print(f"Reading file: {input}")
    random = open(input, "rb").read()

    print("Converting contents...")
    bitmap = convert_raw_to_bitmap(random)

    print(f"Writing file: {output}")
    open(output, "wb").write(bitmap)

if __name__ == "__main__":
    import sys
    Main(sys.argv[1], sys.argv[2])
