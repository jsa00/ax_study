import httpx
import asyncio

async def get_post(num):
    async with httpx.AsyncClient() as client:
        url = f"https://jsonplaceholder.typicode.com/posts/{num}"

        res = await client.get(url)
        result = res.json()

        return result['id'], result['title']

# 10개 작업 반복 실행 - 하나씩 출력
# async def main():
#     for i in range(1, 11):
#         result = await get_post(i)
#         print(result)

# 10개 작업 반복 실행 - 한꺼번에 출력
async def main():
    get_posts = [get_post(i) for i in range(1, 11)]

    results = await asyncio.gather(*get_posts)

    print(results)

asyncio.run(main())