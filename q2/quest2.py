import os
from pathlib import Path

desktop = Path.home() / 'Desktop'
path = desktop / 'Кафедра_ИБСТ_ПГУ.desktop'

content = """[Desktop Entry]
Name=Кафедра ИБСТ ПГУ
GenericName=ИБСТ
Comment=Моя любимая кафедра
URL=https://dep_ibst.pnzgu.ru/ctf
Type=Link
Icon=text-html
Terminal=false
"""

path.write_text(content, encoding='utf-8')
os.chmod(path, 0o755)
print(path)
