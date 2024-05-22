import httpx
import asyncio
import os

async def knative_request(client,knative_service_url):

    print("starting")
    result = await client.get(
       knative_service_url,
       timeout=None,
    )
    print(result)



async def main() -> None:

    tasks = set()
    knative_service_url = os.environ.get('KNATIVE_SERVICE_URL', 'http://test.test.svc.cluster.local')
    request_number = int(os.environ.get('REQUEST_NUMBER'))

    async with httpx.AsyncClient() as client:

        long_running_requests = [knative_request(client, knative_service_url) for _ in range(request_number)]
        await asyncio.gather(*long_running_requests)


asyncio.run(main())