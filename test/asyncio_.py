import asyncio
import time

async def main():
    start=time.time()
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    print(start-time.time())

# Python 3.7+
# asyncio.run(main())

main()