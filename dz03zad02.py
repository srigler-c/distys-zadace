import asyncio
import numpy as np
import psutil

async def afun1():
    np.random.normal(loc=0.0, scale=10.0, size=1000000)
    await asyncio.sleep(0.9)

async def afun2():
    print('The CPU usage is: ', psutil.cpu_percent(10))

async def main():
    await afun1()
    await afun2()

if __name__ == "__main__":
    asyncio.run(main())
