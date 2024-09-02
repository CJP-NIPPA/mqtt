import asyncio
from typing import List
import aiofiles
import csv
import logging

from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
from lora_reciever import Receiver

class Listener:
    def __init__(self, host: str, port: int, csv_path: str) -> None:
        self.host = host # vos
        self.port = port # una puerta por la que van a entrar los datos
        self.path = csv_path # el csv donde guardar
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.x: List[float|int] = []
        self.y: List[float|int] = []
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        FuncAnimation(self.fig, self.animate, interval=100, repeat=False, fargs=(self.x,self.y, 3))
        plt.show()


    def animate(self,i,x,y, index):
        ## Sacar un dato
        try:
            async with aiofiles.open('output_1.csv', 'r') as file:
                lines = await file.readlines()
                data = lines[-20:]

                variable = data[index]

                self.x.append(dt.datetime.now().strftime('%H:%M:%S'))
                self.y.append(variable)

                self.x = self.x[-20:]
                self.y = self.y[-20:]
                self.ax.clear()
                self.ax.plot(x,y)
                self.ax.set_title(f'{names[index]} over time')
                self.ax.set_ylim(boundary[index])

                plt.xticks(rotation=45)
        except Exception as e:
            self.logger.error(f"Error starting server: {e}")

    async def start_listening(self):
        try:
            server = await asyncio.start_server(
                self.handle_connection, self.host, self.port
            )
            self.logger.info(f"Listening on {self.host}:{self.port}")
            async with server:
                await server.serve_forever()
        except Exception as e:
            self.logger.error(f"Error starting server: {e}")

    async def handle_connection(self, reader, writer):
        addr = writer.get_extra_info('peername')
        self.logger.info(f"New connection from {addr}")
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                message = data.decode('utf-8').strip()
                await self.write_to_csv(message)

        except Exception as e:
            self.logger.error(f"Error handling connection: {e}")
        finally:
            writer.close()
            await writer.wait_closed()
            self.logger.info(f"Connection closed from {addr}")

    async def write_to_csv(self, message):
        try:
            async with aiofiles.open(self.path, 'a', newline='') as file:
                writer = csv.writer(file)
                await writer.writerow([message])
            self.logger.info(f"Wrote message to {self.path}")
        except Exception as e:
            self.logger.error(f"Error writing to CSV: {e}")

async def main() -> None:
    listeners: List[Listener] = [Listener('127.0.0.1', idx, f'output_{idx}.csv') for idx in range(1,5)] ## 4 sensors
    while True:
        await asyncio.gather(*[listener.start_listening() for listener in listeners])

if __name__ == '__main__':
    asyncio.run(main())
