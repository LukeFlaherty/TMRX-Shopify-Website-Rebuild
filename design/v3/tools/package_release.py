#!/usr/bin/env python3
"""Validate and package V3; writes ZIP/checksum beside the package folder.

Only the standard library is required. No API, deployment or cloud upload.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT/'package-metadata.json').read_text())['version']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    subprocess.run([sys.executable, str(ROOT/'tools/validate_package.py')], check=True)
    inventory_path = ROOT/'qa/file-inventory.json'
    rows = [{'file': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
             'sha256': digest(p.read_bytes())}
            for p in sorted(ROOT.rglob('*'))
            if p.is_file() and p != inventory_path and '__pycache__' not in p.parts]
    inventory_path.write_text(json.dumps({'version': VERSION,
        'scope': 'Every package file except this inventory itself.', 'files': rows}, indent=2)+'\n')
    output = ROOT.parent/f'true-matrx-v3-redesign-{VERSION}.zip'
    prefix = f'true-matrx-v3-redesign-{VERSION}'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(ROOT.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                archive.write(path, prefix+'/'+path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError('Archive CRC failed: '+bad)
        for row in rows:
            archived = archive.read(prefix+'/'+row['file'])
            if digest(archived) != row['sha256']:
                raise RuntimeError('Archived hash mismatch: '+row['file'])
    checksum = digest(output.read_bytes())
    output.with_suffix('.zip.sha256').write_text(checksum+'  '+output.name+'\n')
    print(json.dumps({'archive': str(output), 'bytes': output.stat().st_size,
                      'package_files': len(rows)+1, 'sha256': checksum,
                      'archive_crc_and_content_hashes_verified': True}, indent=2))


if __name__ == '__main__':
    main()
