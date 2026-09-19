from pathlib import Path

SIG = {
    b'\x89PNG\r\n\x1a\n':  '.png',
    b'%PDF-':              '.pdf',
    b'OTTO':               '.otf',
    b'\xff\xd8\xff':       '.jpg',
    b'Rar!\x1a\x07':       '.rar',
    b'7z\xbc\xaf\x27\x1c': '.7z',
    b'PK':                 '.zip',
    b'\xff\xfe':           '.utf16le.txt',
    b'\xfe\xff':           '.utf16be.txt',
}

for f in Path('.').iterdir():
    if not f.is_file() or f.suffix or f.name == Path(__file__).name:
        continue
    head = f.read_bytes()[:8]
    for sig, ext in SIG.items():
        if head.startswith(sig):
            new = f.with_name(f.name + ext)
            f.rename(new)
            print(f'{f.name} -> {new.name}')
            break
    else:
        print(f'{f.name}: тип не определён')
