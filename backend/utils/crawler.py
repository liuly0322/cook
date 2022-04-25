import httpx
# import asyncio


async def get_recent_videos() -> str:
    async with httpx.AsyncClient() as client:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        response = await client.get('https://api.bilibili.com/x/web-interface/newlist?rid=76&type=0&ps=30&pn=1', headers=headers)
        return response.text

# a = asyncio.run(get_recent_videos())
