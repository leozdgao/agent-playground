# 根据销售信息尝试绑定客户

from typing import Optional
import parlant.sdk as p

@p.tool
async def get_firm_info(context: p.ToolContext, firmId: Optional[str] = None) -> p.ToolResult:
  firmInfo = None

  # 已经拿到 firmId，通过 rpc 查询完整客户信息并返回
  if firmId:
    # firmInfo = await rpc.call("firm_service", "get_firm_info", firmId=firmId)
    firmInfo = {"id": 1000, "firmId": firmId, "name": "道琼斯有限公司"}
  else:
    # 如果从上下文中没有直接提供 firmId，通过会话 id 获取销售进线绑定的客户
    # firmInfo = await rpc.call("customer_service", "get_session_info", sessionId=context.session_id)
    firmInfo = {"id": 1001, "firmId": "400000400000", "name": "测试客户有限公司"}
    
  return p.ToolResult(data=firmInfo)
