# 客户查款类相关处理流程

import parlant.sdk as p
from customerservice.tools import account
from tools import fund, collabration, risk

async def create_inquiry_journey(server: p.Server, agent: p.Agent) -> p.Journey:
  # Create the journey
  journey = await agent.create_journey(
    title="收款查款流程",
    description="收款查款流程",
    conditions=["客户遇到款项收不到或者款项状态不更新等情况来咨询"],
  )

  # 先绑定客户
  t0 = await journey.initial_state.transition_to(chat_state="确认是哪个客户出的问题，需要提供 firmId")

  # 获取完整客户信息
  t1 = await t0.target.transition_to(tool_state=account.get_firm_info)

  # 询问付款金额/币种
  t2 = await t1.target.transition_to(chat_state="确认问题款项的付款金额/币种")

  # 入金记录查询
  t3 = await t2.target.transition_to(tool_state=fund.deposit_query)

  # 查到款项，如果是待入账/审核中，则直接按标准话术回复
  t3_0 = await t3.target.transition_to(
    chat_state="直接回复：'款项目前状态在风控审核中，今天（工作日）会审核完成的，请您耐心等待，如有问题我们也会第一时间联系您'",
    condition="收款记录存在并且状态为 auditing",
  )
  await t3_0.target.transition_to(state=p.END_JOURNEY)
  # 查到款项，其他状态都认为是正常状态，让客户自行前往 App 确认即可
  t3_1 = await t3.target.transition_to(
    chat_state="直接回复：'款项目前状态为已入账，您可以让客户在 App 查询款项状态'",
    condition="收款记录存在并且状态为除 auditing 外的其他状态",
  )
  await t3_1.target.transition_to(state=p.END_JOURNEY)

  # 没有查到款项，进入接下去的异常排查，查看是否存在 VA 异常入账
  t4 = await t3.target.transition_to(
    chat_state="告知对方系统中未查到相关款项记录，正在确认是否有 VA 异常入账",
    condition="收款记录不存在",
  )
  t5 = await t4.target.transition_to(
    tool_state=fund.check_va_expection,
  )
  # 没有查到款项，进入接下去的异常排查，查看是否存在 VA 异常入账
  t5_0 = await t5.target.transition_to(
    chat_state="回复说发现客户存在 VA 异常入账的情况，准备创建协同工单协同客资来解决",
    condition="存在VA异常入账",
  )
  t5_1 = await t5_0.target.transition_to(
    tool_state=collabration.create_collabration_workorder,
  )
  t5_2 = await t5_1.target.transition_to(
    chat_state="向咨询人回复已创建协同工单转交客资同时进一步排查，请耐心等待",
  )
  await t5_2.target.transition_to(state=p.END_JOURNEY)

  t6 = await t5.target.transition_to(
    chat_state="告知对方系统中未查到VA异常入账工单，需要确认是否有被调单的情况",
    condition="不存在VA异常入账",
  )
  t7 = await t6.target.transition_to(
    tool_state=risk.check_dispute_retrieval,
  )
  t7_1 = await t7.target.transition_to(
    chat_state="回复说客户存在被调单的情况，目前已在跟进中了，需要客户等待 3 个工作日左右",
    condition="存在调单工单",
  )
  await t7_1.target.transition_to(state=p.END_JOURNEY)

  t8 = await t7.target.transition_to(
    chat_state="回复说客户不存在被调单的情况，目前系统中不存在相关工单",
    condition="不存在调单工单",
  )
  t8_1 = await t8.target.transition_to(
    tool_state=collabration.create_collabration_workorder,
  )
  t8_2 = await t8_1.target.transition_to(
    chat_state="向咨询人回复已创建协同工单转交客资同时进一步排查，请耐心等待",
  )
  await t8_2.target.transition_to(state=p.END_JOURNEY)

  return journey


