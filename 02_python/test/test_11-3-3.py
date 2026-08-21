# 11장 3강 3-3
import httpx
import time
import asyncio

POST_IDS = list(range(1, 1000))
BASE_URL = "https://jsonplaceholder.typicode.com/todos"

async def fetch_todo_by_id(client: httpx.AsyncClient, post_id: int):
    try:
        if post_id == 999:
            raise httpx.HTTPStatusError("웹 요청 실패 상황 가정", request=None, response=None)
            
        response = await client.get(f"{BASE_URL}/{post_id}")
        response.raise_for_status()
        return response.json()
            
    except httpx.HTTPError as error:
        print(f"경고: {post_id}번 게시글 다운로드 실패 ({error}). 빈 값으로 대체 후 처리를 지속합니다.")
        return {"id": post_id, "title": "수집 에러 대체 데이터"}

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