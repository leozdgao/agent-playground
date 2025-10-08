import asyncio
import parlant.sdk as p
from journey.inquiry import create_inquiry_journey

async def main():
    async with p.Server(nlp_service=p.NLPServices.litellm) as server:
        agent = await server.create_agent(
            name = "客服",
            description = "你是一位在B2B外贸收款公司工作的专业客户服务人员"
        )
        # 声明查款流程
        journey = await create_inquiry_journey(server, agent)

if __name__ == "__main__":
    asyncio.run(main())

