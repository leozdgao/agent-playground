import asyncio
import parlant.sdk as p
from journey.inquiry import create_inquiry_journey

async def main():
    async with p.Server() as server:
        agent = await server.create_agent(
            name = "客服",
            description = "你是一位在 XTransfer 工作的专业客户服务人员"
        )

        # 声明查款流程
        journey = await create_inquiry_journey(server, agent)
        await journey.start()

if __name__ == "__main__":
    asyncio.run(main())

