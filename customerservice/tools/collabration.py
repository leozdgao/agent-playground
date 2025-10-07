# 查款工具

import parlant.sdk as p

# 创建协同工单协同客资
@p.tool
async def create_collabration_workorder(context: p.ToolContext, firmId: str, amount: float, currency: str) -> p.ToolResult:
  # await rpc.call(
  #   service="collabaration",
  #   method="create_collabration_workorder",
  #   params={"firmId": firmId, "target": "", "channel": "dbs"},
  # )

  return p.ToolResult(data={"result": "success", "workorderId": "10000000000000000000000000000000"})
