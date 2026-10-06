"""Generate Markdown navigation and validate the wiki: update | check."""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
CATEGORIES = {
    'computer-science': '컴퓨터 과학', 'operating-systems': '운영체제',
    'networking': '네트워크', 'databases': '데이터베이스', 'cloud': '클라우드',
    'containers': '컨테이너 · Kubernetes', 'devops': 'DevOps · 운영',
    'security': '보안', 'storage': '스토리지', 'architecture': '시스템 설계',
    'languages': '프로그래밍 언어', 'career': '면접 · 협업 · 경험',
}
CONFIG = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))
PUBLIC = CONFIG.get('extra', {}).get('publication_scope') == 'public'
STATUS = {'note': '노트', 'draft': '초안', 'review': '검토 필요'}
FOOTER_START, FOOTER_END = '<!-- BEGIN WIKI NAV -->', '<!-- END WIKI NAV -->'
NAV_START, NAV_END = '# BEGIN GENERATED NAV', '# END GENERATED NAV'

def read_page(file):
    text = file.read_text(encoding='utf-8-sig')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError(f'{file.relative_to(ROOT)}: front matter가 없습니다')
    meta = yaml.safe_load(match[1])
    if not isinstance(meta, dict):
        raise ValueError(f'{file.relative_to(ROOT)}: 잘못된 front matter')
    return meta, text[match.end():].lstrip('\n')

def frontmatter(title, category='wiki', tags=None):
    return '---\n' + yaml.safe_dump(
        dict(title=title, category=category, tags=tags or ['wiki'], status='note', **({'visibility': 'public'} if PUBLIC else {})),
        allow_unicode=True, sort_keys=False,
    ) + '---\n\n'

def relative(source, target):
    return os.path.relpath(target, source.parent).replace(os.sep, '/')

def link(page, source):
    return f"[{page['title']}]({relative(source, page['file'])})"

def topic_pages():
    pages = []
    for category in CATEGORIES:
        for file in sorted((DOCS / category).rglob('*.md')):
            if file == DOCS / category / 'index.md':
                continue
            meta, body = read_page(file)
            if meta.get('category') != category:
                raise ValueError(f'{file.relative_to(ROOT)}: category와 디렉터리가 다릅니다')
            pages.append({**meta, 'file': file, 'body': body})
    return pages

def outputs(pages):
    result, by_category, by_tag = {}, defaultdict(list), defaultdict(list)
    for page in pages:
        by_category[page['category']].append(page)
        for tag in page['tags']:
            by_tag[tag].append(page)
    active = {key: title for key, title in CATEGORIES.items() if by_category[key]}
    for group in [*by_category.values(), *by_tag.values()]:
        group.sort(key=lambda p: (p['status'] == 'draft', p['title'], str(p['file'])))
    home, counts = DOCS / 'index.md', Counter(p['status'] for p in pages)
    name = CONFIG.get('site_name', 'Knowledge wiki')
    intro = CONFIG.get('site_description', '기술 지식 위키')
    text = frontmatter(name) + f'# {name}\n\n{intro}\n\n'
    text += '[태그로 찾기](tags.md) · [웹 태그 목록](tags/index.md) · [위키 사용법](guides/wiki.md) · [문서 작성 규칙](guides/contributing.md)\n\n'
    text += f"주제 문서는 **{len(pages)}개**, 태그는 **{len(by_tag)}개**입니다. 초안 {counts['draft']}개와 검토 필요 {counts['review']}개를 상태로 구분합니다.\n\n"
    text += '## 주제별 탐색\n\n| 주제 | 문서 | 초안 |\n| --- | ---: | ---: |\n'
    for category, title in active.items():
        group = by_category[category]
        text += f"| [{title}]({category}/index.md) | {len(group)} | {sum(p['status'] == 'draft' for p in group)} |\n"
    text += '\n## 시작하기\n\n'
    for category in active:
        page = by_category[category][0]
        text += f"- {active[category]}: {link(page, home)}\n"
    text += '\n'
    text += '## 문서 상태\n\n- **노트**: 기존 학습·운영 기록입니다. 전체 사실 검증을 완료했다는 뜻은 아닙니다.\n- **초안**: 작성 예정이거나 제목·질문 중심인 문서입니다.\n- **검토 필요**: 앞선 점검에서 기술 설명을 보완할 부분이 발견된 문서입니다.\n\n'
    text += '문서 추가 또는 태그 변경 후 `python scripts/wiki.py update`로 목차를 갱신하세요.\n'
    result[home] = text
    for category, title in active.items():
        file = DOCS / category / 'index.md'
        text = frontmatter(title, category, [category]) + f'# {title}\n\n[위키 홈](../index.md) · [태그 목록](../tags.md)\n\n| 문서 | 상태 | 태그 |\n| --- | --- | --- |\n'
        for page in by_category[category]:
            tags = ' · '.join(f'[#{t}](../tags.md#{t})' for t in page['tags'])
            text += f"| {link(page, file)} | {STATUS[page['status']]} | {tags} |\n"
        result[file] = text
    file = DOCS / 'tags.md'
    text = frontmatter('태그별 문서 목록') + '# 태그별 문서 목록\n\nGitHub와 웹 위키에서 공통으로 탐색할 수 있는 목록입니다. [위키 홈](index.md) · [웹 태그 목록](tags/index.md)\n\n'
    text += ' · '.join(f'[#{t}](#{t})' for t in sorted(by_tag)) + '\n\n'
    for tag, group in sorted(by_tag.items()):
        text += f'## {tag}\n\n'
        for page in group:
            text += f"- {link(page, file)} — {STATUS[page['status']]}\n"
        text += '\n'
    result[file] = text
    for page in pages:
        file = page['file']
        original = file.read_text(encoding='utf-8-sig')
        original = re.sub(r'\n*' + re.escape(FOOTER_START) + r'.*?' + re.escape(FOOTER_END) + r'\n*\Z', '', original, flags=re.S).rstrip()
        tags = ' · '.join(f"[#{t}]({relative(file, DOCS / 'tags.md')}#{t})" for t in page['tags'])
        footer = f"\n\n{FOOTER_START}\n\n---\n\n상태: **{STATUS[page['status']]}** · 태그: {tags}\n\n"
        footer += f"[주제 목차]({relative(file, DOCS / page['category'] / 'index.md')}) · [위키 홈]({relative(file, home)})\n\n{FOOTER_END}\n"
        result[file] = original + footer
    nav = [{'홈': 'index.md'}, {'태그': 'tags/index.md'}, {'태그 목록 (Markdown)': 'tags.md'}]
    for category, title in active.items():
        entries = [{'주제 목차': f'{category}/index.md'}]
        entries += [{page['title']: page['file'].relative_to(DOCS).as_posix()} for page in by_category[category]]
        nav.append({title: entries})
    nav.append({'위키 안내': [{'위키 사용법': 'guides/wiki.md'}, {'문서 작성 규칙': 'guides/contributing.md'}, {'GitHub Pages 배포': 'guides/github-pages.md'}]})
    config = ROOT / 'mkdocs.yml'
    generated = NAV_START + '\n' + yaml.safe_dump({'nav': nav}, allow_unicode=True, sort_keys=False, width=120).rstrip() + '\n' + NAV_END
    result[config] = re.sub(re.escape(NAV_START) + r'.*?' + re.escape(NAV_END), lambda _: generated, config.read_text(encoding='utf-8'), flags=re.S)
    return {file: text.rstrip() + '\n' for file, text in result.items()}

def validate():
    errors = []
    for file in sorted(DOCS.rglob('*.md')):
        try:
            meta, body = read_page(file)
        except ValueError as error:
            errors.append(str(error)); continue
        if not isinstance(meta.get('title'), str) or not meta['title'].strip():
            errors.append(f'{file.relative_to(ROOT)}: title이 필요합니다')
        tags = meta.get('tags')
        if not isinstance(tags, list) or not tags or any(not isinstance(t, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in tags):
            errors.append(f'{file.relative_to(ROOT)}: tags는 소문자 kebab-case 목록이어야 합니다')
        elif len(tags) != len(set(tags)):
            errors.append(f'{file.relative_to(ROOT)}: 중복 태그')
        if PUBLIC and meta.get('visibility') != 'public':
            errors.append(f'{file.relative_to(ROOT)}: 공개 문서는 visibility: public이 필요합니다')
        if meta.get('status') not in STATUS:
            errors.append(f'{file.relative_to(ROOT)}: status는 note/draft/review 중 하나여야 합니다')
        fence = None
        for number, line in enumerate(body.splitlines(), 1):
            marker = re.match(r'\s*(`{3,}|~{3,})', line)
            if marker:
                fence = None if fence == marker[1][0] else marker[1][0]; continue
            if fence: continue
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', line):
                url = urlsplit(target.strip('<>'))
                if url.scheme or url.netloc or not url.path: continue
                destination = (file.parent / unquote(url.path)).resolve()
                if not destination.is_relative_to(DOCS):
                    errors.append(f'{file.relative_to(ROOT)}:{number}: docs 밖의 링크 {target}')
                elif not destination.exists():
                    errors.append(f'{file.relative_to(ROOT)}:{number}: 없는 링크 {target}')
    for file in DOCS.rglob('*'):
        if file.is_file() and (re.search(r'[\x00-\x1f<>:"|?*]', file.name) or file.name.endswith(('.', ' '))):
            errors.append(f'Windows 비호환 파일명: {file.relative_to(ROOT)}')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['update', 'check'])
    args = parser.parse_args()
    try:
        pages = topic_pages(); generated = outputs(pages)
    except (ValueError, KeyError, TypeError) as error:
        print(error, file=sys.stderr); return 1
    if args.command == 'update':
        for file, text in generated.items():
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(text, encoding='utf-8', newline='\n')
    errors = validate()
    if args.command == 'check':
        for file, expected in generated.items():
            if not file.exists() or file.read_text(encoding='utf-8') != expected:
                errors.append(f'{file.relative_to(ROOT)}: 자동 목록이 오래되었습니다 (wiki.py update 실행)')
    if errors:
        print('\n'.join(errors), file=sys.stderr); return 1
    print(f"Wiki {args.command}: {len(pages)} topic documents, {len(set(p['category'] for p in pages))} categories, {len(set(t for p in pages for t in p['tags']))} tags; links and metadata OK")
    return 0

if __name__ == '__main__':
    sys.exit(main())
