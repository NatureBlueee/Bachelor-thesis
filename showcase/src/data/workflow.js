export const workflows = [
  {
    name: '研究循环',
    color: '#3b82f6',
    nodes: [
      { id: 'ask', label: '/ask-academic-ai', desc: '向学术AI提问，获取文献支持' },
      { id: 'add', label: '/add-paper', desc: '将PDF文献转换为Markdown' },
      { id: 'read', label: '/deep-read', desc: '深度阅读，输出结构化笔记' },
    ],
  },
  {
    name: '修改循环',
    color: '#10b981',
    nodes: [
      { id: 'create', label: '/create-pr', desc: '创建修改请求' },
      { id: 'discuss', label: '讨论', desc: '与AI讨论修改内容' },
      { id: 'merge', label: '/merge-pr', desc: '合并修改到正文' },
    ],
  },
  {
    name: '维护循环',
    color: '#f59e0b',
    nodes: [
      { id: 'sync', label: '/sync', desc: '同步系统状态' },
      { id: 'reflect', label: '/reflect', desc: '提取讨论洞见' },
    ],
  },
]

export const fileTree = [
  { name: 'Target/', desc: '论文正文', children: [{ name: 'Draft.md', desc: '通过PR修改' }] },
  { name: 'Reference/', desc: '文献库 (PDF→Markdown)' },
  { name: 'PR/', desc: '修改请求记录' },
  { name: 'Consensus/', desc: '学术讨论记录' },
  { name: 'MEMORY.md', desc: 'AI记忆（偏好、洞见）' },
  { name: '.agent/', desc: 'AI规则与工作流' },
]
