import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Folder, FileText, BookOpen, GitPullRequest, MessageSquare, Brain, Settings, ChevronRight } from 'lucide-react'

const files = [
  {
    name: 'Target/',
    icon: Folder,
    desc: '论文正文',
    color: 'var(--accent-sage)',
    children: [{ name: 'Draft.md', icon: FileText, desc: '主文档，所有修改通过PR' }]
  },
  {
    name: 'Reference/',
    icon: BookOpen,
    desc: 'PDF→Markdown 文献库',
    color: 'var(--accent-azure)',
    children: [
      { name: 'PDF-MD/', icon: Folder, desc: '转换后的文献' },
      { name: 'pdfs/', icon: Folder, desc: '原始PDF' }
    ]
  },
  {
    name: 'PR/',
    icon: GitPullRequest,
    desc: '修改请求记录',
    color: 'var(--accent-gold)',
    children: [
      { name: 'PR-0006.md', icon: FileText, desc: '方法论调整' },
      { name: '_INDEX.md', icon: FileText, desc: 'PR索引' }
    ]
  },
  { name: 'Consensus/', icon: MessageSquare, desc: '学术讨论记录', color: 'var(--accent-coral)' },
  { name: 'MEMORY.md', icon: Brain, desc: 'AI 记忆', color: 'var(--accent-gold)' },
  { name: '.agent/', icon: Settings, desc: '规则与工作流', color: 'var(--text-muted)' },
]

export default function FileTree() {
  const [expanded, setExpanded] = useState({})

  const toggle = (i) => setExpanded(prev => ({ ...prev, [i]: !prev[i] }))

  return (
    <section className="py-32 px-6">
      <div className="max-w-2xl mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} className="text-center mb-12">
          <h2 className="text-3xl mb-4">项目结构</h2>
          <p className="text-[var(--text-secondary)]">点击文件夹展开</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="rounded-xl p-6 border border-white/10"
          style={{ background: 'var(--bg-elevated)', fontFamily: 'var(--font-mono)' }}
        >
          <div className="text-sm text-[var(--text-muted)] mb-4 flex items-center gap-2">
            <Folder size={16} />
            Bachelor-thesis/
          </div>

          {files.map((f, i) => (
            <div key={f.name}>
              <motion.div
                initial={{ opacity: 0, x: -10 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ delay: i * 0.05 }}
                onClick={() => f.children && toggle(i)}
                whileHover={{ x: 4 }}
                className={`flex items-center gap-3 py-2 px-2 -mx-2 rounded-lg transition-colors text-sm ${f.children ? 'cursor-pointer hover:bg-white/5' : ''}`}
              >
                <f.icon size={16} style={{ color: f.color }} />
                <span className="text-[var(--text-primary)]">{f.name}</span>
                {f.children && (
                  <motion.span animate={{ rotate: expanded[i] ? 90 : 0 }} className="text-[var(--text-muted)]">
                    <ChevronRight size={14} />
                  </motion.span>
                )}
                <span className="ml-auto text-xs text-[var(--text-muted)]">{f.desc}</span>
              </motion.div>

              <AnimatePresence>
                {expanded[i] && f.children && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                    className="ml-5 pl-4 border-l border-white/10 overflow-hidden"
                  >
                    {f.children.map((child, j) => (
                      <motion.div
                        key={child.name}
                        initial={{ opacity: 0, x: -5 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: j * 0.05 }}
                        className="py-2 flex items-center gap-2 text-sm text-[var(--text-secondary)]"
                      >
                        <child.icon size={14} />
                        <span>{child.name}</span>
                        <span className="text-xs text-[var(--text-muted)] ml-auto">{child.desc}</span>
                      </motion.div>
                    ))}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}
