import io
import json


def parse(s: str) -> dict:
    """
    接受爬虫返回的数据
    返回视频数据
    """
    # to be done: error handling
    data: dict = json.loads(s).get('data')
    count: int = data.get('page').get('count')
    archives: dict = data.get('archives')
    videos = [{'title': video.get('title'), 'link': video.get(
        'short_link'), 'desc': video.get('desc')} for video in archives]
    return {"count": count, "videos": videos}


f = io.open('./backend/utils/test.json')
content = f.read()
f.close()
res = parse(content)
