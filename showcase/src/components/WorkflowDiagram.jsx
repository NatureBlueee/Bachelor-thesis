import { motion } from 'framer-motion'
import { GitPullRequest, BookOpen, Brain, Search } from 'lucide-react'

const features = [
  {
    icon: GitPullRequest,
    title: 'PR 驱动写作',
    desc: '每次修改都有记录、有理由、可追溯',
    color: 'var(--accent-gold)',
  },
  {
    icon: BookOpen,
    title: '文献即代码',
    desc: 'PDF 转 Markdown，引用自动检索',
    color: 'var(--accent-azure)',
  },
  {
    icon: Brain,
    title: '持久记忆',
    desc: '偏好、风格、规范，说一次就记住',
    color: 'var(--accent-sage)',
  },
  {
    icon: Search,
    title: '批判性伙伴',
    desc: '质疑假设，追问来源，不做应声虫',
    color: 'var(--accent-coral)',
  },
]

export default function WorkflowDiagram() {
  return (
    <section className="py-24 px-6 min-h-screen flex items-center" style={{ background: 'var(--bg-surface)' }}>
      <div className="max-w-4xl mx-auto w-full">

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl mb-4">四个核心能力</h2>
          <p className="text-lg text-[var(--text-secondary)]">工程化思维 × AI 协作</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {features.map((f, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -4 }}
              className="rounded-2xl p-6"
              style={{ background: 'var(--bg-elevated)' }}
            >
              <div className="w-12 h-12 rounded-xl flex items-center justify-center mb-4" style={{ background: `${f.color}15` }}>
                <f.icon size={24} style={{ color: f.color }} />
              </div>
              <h3 className="text-xl font-medium mb-2">{f.title}</h3>
              <p className="text-[var(--text-secondary)]">{f.desc}</p>
            </motion.div>
          ))}
        </div>

      </div>
    </section>
  )
}
