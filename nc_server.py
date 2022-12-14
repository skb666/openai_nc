#!python
import openai_api
import asyncio  # 导入asyncio库


# 定义一个异步处理网络请求的函数
async def nc_handler(reader, writer):
    content = ''
    while True:
        # 打印提示符
        writer.write(b'\n> ')
        await writer.drain()
        # 从网络连接中读取数据
        data = await reader.read(1024)
        # 获取远程连接的地址信息
        addr = writer.get_extra_info('peername')
        print(f"Received from {addr}")
        # 解码数据
        if data:
            txt = data.decode().strip()
        else:
            txt = ''
        if txt:
            if txt == 'exit':
                break
            content += txt + '\n'
            response = openai_api.my_diy(content) + '\n'
        else:
            response = 'None\n'
        # 向客户端发送响应的数据
        writer.write(response.encode())
    # 关闭连接
    writer.close()


# 获取一个事件循环对象loop
loop = asyncio.get_event_loop()
# 绑定nc服务器的地址和端口
coro = asyncio.start_server(nc_handler, '0.0.0.0', 8888, loop=loop)
# 启动一个服务
server = loop.run_until_complete(coro)

# 打印出服务器相关信息
print('Serving on {}'.format(server.sockets[0].getsockname()))
# 使用无限循环来保持程序不退出
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# 关闭服务
server.close()
# 关闭事件循环
loop.run_until_complete(server.wait_closed())
loop.close()
