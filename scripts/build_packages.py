"""Build portable skill uploads and a complete Gem knowledge file; no network calls."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
NAME = 'family-trip-guide'


def flatten_links(text, parent):
    def replace(match):
        label, target = match.groups()
        if '://' in target or target.startswith('#'):
            return match.group(0)
        path = (parent / target.split('#')[0]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError(f'Invalid reference: {target}')
        return f'{label}（見「來源：{path.relative_to(ROOT).as_posix()}」章節）'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, text)


def build(output):
    version = (ROOT / 'VERSION').read_text().strip()
    skill = ROOT / 'SKILL.md'
    header = skill.read_text().split('---', 2)[1]
    if not re.search(r'^name: family-trip-guide$', header, re.M):
        raise ValueError('Skill name must match the package folder')
    documents = [skill, *sorted((ROOT / 'references').glob('*.md'))]
    payload = {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in documents}
    payload['LICENSE.txt'] = (ROOT / 'LICENSE').read_bytes()
    output.mkdir(parents=True, exist_ok=True)
    artifacts = []
    for platform, prefix in [('claude', f'{NAME}/'), ('gemini', '')]:
        path = output / f'{NAME}-{platform}.zip'
        with ZipFile(path, 'w', compression=ZIP_DEFLATED) as archive:
            for name, data in sorted(payload.items()):
                item = ZipInfo(prefix + name, date_time=(2026, 1, 1, 0, 0, 0))
                item.compress_type = ZIP_DEFLATED
                item.external_attr = 0o100644 << 16
                archive.writestr(item, data)
        with ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise ValueError('Corrupt archive')
            for name in archive.namelist():
                if '..' in PurePosixPath(name).parts or name.startswith('/'):
                    raise ValueError('Unsafe archive path')
        artifacts.append(path)
    knowledge = [f'Family Trip Guide 完整知識｜v{version}',
                 '依【來源：原始檔名】尋找章節；相對文件連結已改成同檔章節索引。',
                 '這是通用skill知識，不包含任何實際旅行訂單、票券或旅伴個資。']
    for path in documents:
        label = path.relative_to(ROOT).as_posix()
        knowledge.extend(['', f'【來源：{label}】',
                          flatten_links(path.read_text(), path.parent)])
    knowledge_path = output / f'{NAME}-knowledge.txt'
    knowledge_path.write_text('\n'.join(knowledge) + '\n', encoding='utf-8')
    artifacts.append(knowledge_path)
    instructions_path = output / 'gemini-gem-instructions.txt'
    instructions_path.write_bytes((ROOT / 'platforms/gemini-gem-instructions.txt').read_bytes())
    artifacts.append(instructions_path)
    manifest = {'version': version, 'name': NAME, 'knowledge_sections': len(documents),
                'files': [{'name': p.name, 'bytes': p.stat().st_size,
                           'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                          for p in artifacts]}
    (output / 'checksums.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    print(json.dumps(build(args.output_dir.resolve()), ensure_ascii=False, indent=2))
