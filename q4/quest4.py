from pathlib import Path

for f in Path('.').iterdir():
    if not f.is_file() or f.name == Path(__file__).name:
        continue
    raw = f.read_bytes()[:64]
    for enc in ('utf-8', 'utf-16', 'cp1251', 'cp866'):
        try:
            text = raw.decode(enc)
        except UnicodeDecodeError:
            continue
        if text.startswith('Привет'):
            print(f'=== {f.name} [{enc}] ===')
            print(f.read_text(encoding=enc))
            break
    else:
        print(f'{f.name}: кодировка не определена')
