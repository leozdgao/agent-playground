# 知识库搜索工具

import parlant.sdk as p

@p.tool
async def search_knowledge(context: p.ToolContext, query: str) -> p.ToolResult:
  # 实际应该是一个 RAG 应用
  # Simulate searching the knowledge base
  return p.ToolResult(data=f"Searching knowledge base for: {query}")
