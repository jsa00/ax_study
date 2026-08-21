# 11장 2강 3-1
import asyncio
import time

async def send_notification(customer_name, wait_seconds):
    print(f"[{customer_name}]님께 문자를 발송합니다")
        
    await asyncio.sleep(wait_seconds) 
    
    print(f"[{customer_name}]님께 문자가 전송되었습니다")

async def main():
    start_time = time.time()

    results = await asyncio.gather(
        send_notification("고객 A", 1),
        send_notification("고객 B", 3),
        send_notification("고객 C", 2)
    )

    end_time = time.time()

    print(results)
    print(f"총 소요 시간: {end_time - start_time:.2f}초가 걸렸습니다.")

asyncio.run(main())