# 11장 2강 1-1
import asyncio

async def cook_ramen():
    print(f"라면 조리를 시작합니다")

    await asyncio.sleep(3)

    print(f"라면 조리가 완료되었습니다")

asyncio.run(cook_ramen())