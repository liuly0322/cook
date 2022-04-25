# Cook

> 好的，今天我们来做菜 🥬

## 说明

计划通过定时获取请求 B 站美食制作区新发布视频，在分词处理后获取菜谱名和菜谱食材，并交由前端界面展示

进度：正在开发

### 参考项目

- [cook](https://github.com/YunYouJun/cook)
- [jieba 分词](https://github.com/fxsjy/jieba)
- [中文菜单词库](https://github.com/wainshine/Food-Names-Corpus)

## Usage

### Development

前端：

```bash
cd frontend
# install dependencies
pnpm install

# convert csv to json
# automatically executed when postinstall
pnpm convert

# start
pnpm dev
# http://localhost:3333
```

后端：

```bash
cd backend
# to be done: requirements.txt
uvicorn main:app --reload
```

### Production

前端：

```bash
cd frontend
pnpm build
```

后端：

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 80
```
