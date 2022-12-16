# openai_nc

## 使用方法

### 启动服务

```bash
# 设置 python3 环境
pipenv shell
pipenv lock
pipenv sync
# 启动监听 127.0.0.1:8888
python ./nc_service.py
```

### 连接

```bash
nc 127.0.0.1 8888
```
