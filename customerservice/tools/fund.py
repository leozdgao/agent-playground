# 查款工具

import parlant.sdk as p

@p.tool
async def deposit_query(context: p.ToolContext, amount: float, currency: str) -> p.ToolResult:
  # rpc call to firm service
  # Simulate getting the deposit query
  return p.ToolResult(data={"amount": amount, "currency": currency, "status": "auditing"})

@p.tool
async def check_va_expection(context: p.ToolContext, firmId: str, amount: float, currency: str) -> p.ToolResult:
  # 获取客户的 DBS 收款账户
  # dbs_va = await rpc.call(
  #   service="account",
  #   method="get_accounts",
  #   params={"firmId": firmId, "channel": "dbs"},
  # )

  # if dbs_va is not None:
  #   # 检查 DBS 渠道的异常入账
    # va_expection = await rpc.call(
    #   service="fund",
    #   method="check_va_expection_for_dbs",
    #   params={"accountId": dbs_va["accountId"], "amount": amount, "currency": currency},
    # )

    # if (va_expection is not None):
    #   return p.ToolResult(data={"expection": va_expection, "message": "DBS渠道VA账户存在异常入账"})

  # va_expection = await rpc.call(
  #   service="fund",
  #   method="check_va_expection",
  #   params={"firmId": firmId, "amount": amount, "currency": currency},
  # )

  # if va_expection is not None:
  #   return p.ToolResult(data={"expection": va_expection, "message": "VA账户存在异常入账"})

  # rpc call to risk service
  # Simulate checking the risk
  return p.ToolResult(data={"expection": None, "message": "VA账户不存在异常入账"})
  
