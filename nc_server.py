#!python
import openai_api
import asyncio


class NCServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(self.peername))
        self.transport.write(b'\n> ')

    def data_received(self, data):
        message = data.decode().strip()
        # print('Data received: {!r}'.format(message))
        if message:
            if message == 'exit':
                self.transport.close()
                return
            response = openai_api.my_diy(message) + '\n'
        else:
            response = 'None\n'
        self.transport.write(response.encode())
        self.transport.write(b'\n> ')

    def connection_lost(self, exc):
        print('Connection from {} closed'.format(self.peername))


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
coro = loop.create_server(NCServer, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
