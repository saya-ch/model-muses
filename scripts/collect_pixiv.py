# -*- coding: utf-8 -*-
"""采集 pixiv 画师的 AI 拟人作品元数据。

只采元数据（标题、作者、页数、标签、尺寸），**不下载图片**。
输出 data/pixiv_artists.json，供 docs/美术素材索引.md 引用与复核。

用法：
  python scripts/collect_pixiv.py

三个坑：
  1. 批量接口 /ajax/illust?illust_id=a&illust_id=b 会 412，只能逐个查
  2. 缩略图路径 /c/1200x2400/img-master/... 一律 403，要原图只能走 urls.original
  3. 间隔要 1.5 秒，太快会被限流

改画师：编辑下面的 ARTISTS。
"""
import json
import os
import time
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      'Chrome/120.0 Safari/537.36')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data')
os.makedirs(OUT, exist_ok=True)


def one(aid):
    """查单个作品详情。"""
    u = f'https://www.pixiv.net/ajax/illust/{aid}?lang=zh'
    req = urllib.request.Request(
        u, headers={'User-Agent': UA,
                    'Referer': f'https://www.pixiv.net/artworks/{aid}'})
    d = json.loads(urllib.request.urlopen(req, timeout=25).read())
    if d.get('error'):
        return None
    b = d.get('body') or {}
    return {
        'id': aid, 'title': b.get('title'), 'user': b.get('userName'),
        'uid': b.get('userId'), 'pages': b.get('pageCount'),
        'tags': [t['tag'] for t in (b.get('tags') or {}).get('tags', [])],
        'w': b.get('width'), 'h': b.get('height'),
        'date': (b.get('createDate') or '')[:10],
        'desc': (b.get('description') or '')[:200],
    }


def user_all(uid):
    """只拿作品 id 列表，不查详情。"""
    u = f'https://www.pixiv.net/ajax/user/{uid}/profile/all?lang=zh'
    req = urllib.request.Request(
        u, headers={'User-Agent': UA, 'Referer': f'https://www.pixiv.net/users/{uid}'})
    b = (json.loads(urllib.request.urlopen(req, timeout=25).read()).get('body') or {})
    return list((b.get('illusts') or {}).keys())


# 萌娘百科等明确点名的 AI 娘作品
KNOWN = ['126903927', '147481146']

ARTISTS = [
    ('上善无形', '62155430', '原始 OC「溟月」的作者，CC BY-NC-SA 4.0'),
    ('ZipZipPipe', '18604994', '主表 31 张的作者'),
    ('hcz', '6799975', '「小鲸鱼饮料瓶」作者，101 件 AI 作品'),
    ('康壳火火火', '56521010', '萌百收录的 DeepSeek娘 早期形象作者'),
]

AI_KEYWORDS = ['deepseek', 'chatgpt', 'claude', 'gemini', 'grok', 'glm', 'qwen',
               'kimi', 'ai娘', '拟人', '娘化', 'meme', 'ミーム', '豆包', 'zcode',
               'aigirl', 'aivtuber']


def is_ai(work):
    tags = ' '.join(work['tags']).lower()
    return any(k in tags for k in AI_KEYWORDS)


if __name__ == '__main__':
    data = {'说明': '画师作品索引（仅元数据，不含图片）', 'known': [], 'artists': []}

    print('=== 已知作品 ===', flush=True)
    for aid in KNOWN:
        r = one(aid)
        if r:
            data['known'].append(r)
            print(f"  {aid} {r['user']} {r['pages']}p {r['w']}x{r['h']} "
                  f"{str(r['title'])[:28]}", flush=True)
        time.sleep(1.5)

    for name, uid, note in ARTISTS:
        print(f'=== {name} ({uid}) ===', flush=True)
        try:
            ids = user_all(uid)
        except Exception as e:
            print('  ERR', type(e).__name__, flush=True)
            continue
        print(f'  主页共 {len(ids)} 件', flush=True)
        works = []
        for aid in ids:
            try:
                r = one(aid)
                if r and is_ai(r):
                    works.append(r)
                    print(f"    {aid} {r['pages']}p {r['w']}x{r['h']} "
                          f"{str(r['title'])[:26]:28} {','.join(r['tags'][:3])}", flush=True)
            except Exception:
                pass
            time.sleep(1.5)
        data['artists'].append({'name': name, 'uid': uid, 'note': note,
                                'total': len(ids), 'ai_works': len(works),
                                'works': works})

    path = os.path.join(OUT, 'pixiv_artists.json')
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'写入 {path}')
