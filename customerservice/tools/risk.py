# 调用风控相关服务能力

import parlant.sdk as p

# 查看客户是否处于被调单的状态
@p.tool
async def check_dispute_retrieval(context: p.ToolContext, firmId: str) -> p.ToolResult:
  # dispute_retrieval_record = await rpc.call(
  #   service="collabaration",
  #   method="create_collabration_workorder",
  #   params={"firmId": firmId, "type": "deposite"},
  # )

  # Simulate checking the risk
  return p.ToolResult(data={ "record": None, "result": "No dispute retrieval record found." })
