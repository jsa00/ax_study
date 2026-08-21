# 11장 3강 2-1
import httpx
import time
import asyncio

POST_IDS = list(range(1, 6))
BASE_URL = "https://jsonplaceholder.typicode.com/todos"

async def fetch_todo_by_id(client: httpx.AsyncClient, post_id: int):
    response = await client.get(f"{BASE_URL}/{post_id}")
    response.raise_for_status()
    data = response.json()
    return {"id": data["id"], "title": data["title"]}

async def run_benchmark():
    start_time_async = time.perf_counter()

    async with httpx.AsyncClient() as client:
        tasks = [fetch_todo_by_id(client, post_id) for post_id in POST_IDS]
        async_results = await asyncio.gather(*tasks)

    end_time_async = time.perf_counter()
    total_time_async = end_time_async - start_time_async

    for res in async_results:
        print(f"  [수집 완료] ID: {res['id']:02d} | 제목: {res['title'][:30]}...")
    print(f">>총 소요 시간: {total_time_async:.4f} 초\n")

asyncio.run(run_benchmark())