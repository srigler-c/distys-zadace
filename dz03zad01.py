import asyncio
import os

async def afun1(x):
    assert isinstance(x, list)
    asyncio.sleep(0.2)
    return  [{"naziv":n,"velicina":v} for v,n in enumerate(x)]


def fun2():
    os.listdir(["datoteka1", "datoteka2", "datoteka3"])
    assert isinstance(x, list) and all([isinstance(d, dict)] for d in x)
    return [{**d, **{"naziv": np.random.randint(1, 10)}} for d in x]

async def main():
    os.mkdir([{"naziv":n} for n in ["datoteka1", "datoteka2", "datoteka3"]])
    await fun1()
    fun2()


if __name__ == "__main__":
    asyncio.run(main())

