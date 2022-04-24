# Cook

> 好的，今天我们来做菜 🥬

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
