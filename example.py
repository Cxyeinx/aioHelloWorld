import aioHelloWorld
import asyncio


async def main():
    await aioHelloWorld.say()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
