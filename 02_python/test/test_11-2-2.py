# 11장 2강 2-1
import asyncio

async def download_music(music_name, wait_seconds):
    print(f"[{music_name}] 다운로드를 시작합니다")
    
    await asyncio.sleep(wait_seconds) 
    
    print(f"[{music_name}] 다운로드가 완료되었습니다")

async def main():
    results = await asyncio.gather(
        download_music("첫 번째 음악", 2),
        download_music("두 번째 음악", 4)
    )

    print(results)

asyncio.run(main())