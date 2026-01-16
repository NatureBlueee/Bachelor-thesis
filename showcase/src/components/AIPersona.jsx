import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Search, BookOpen, Target, Play, Bot } from 'lucide-react'

const conversation = [
  { role: 'user', text: '我觉得这个论点很有说服力。' },
  { role: 'ai', text: '等等，让我挑战一下。你的论据来自哪篇文献？', highlight: '挑战' },
  { role: 'user', text: '呃...我觉得这是常识？' },
  { role: 'ai', text: '在学术写作中，"常识"需要文献支撑。让我帮你在 Reference/ 里找找。', highlight: '文献支撑' },
  { role: 'user', text: '找到了 Qin et al. (2018) 的研究！' },
  { role: 'ai', text: '很好。现在用 /create-pr 把这个引用加进去，记得写清楚修改理由。', highlight: '/create-pr' },
]

const traits = [
  { icon: Search, label: '质疑假设' },
  { icon: BookOpen, label: '文献为证' },
  { icon: Target, label: '追问细节' },
]

export default function AIPersona() {
  const [visibleCount, setVisibleCount] = useState(conversation.length)
  const [isPlaying, setIsPlaying] = useState(false)

  const playConversation = () => {
    if (isPlaying) return
    setIsPlaying(true)
    setVisibleCount(0)
    conversation.forEach((_, i) => {
      setTimeout(() => {
        setVisibleCount(i + 1)
        if (i === conversation.length - 1) setIsPlaying(false)
      }, (i + 1) * 800)
    })
  }

  const highlightText = (text, highlight) => {
    if (!highlight) return text
    const parts = text.split(highlight)
    return parts.map((part, i) => (
      <span key={i}>
        {part}
        {i < parts.length - 1 && <span className="text-[var(--accent-gold)]">{highlight}</span>}
      </span>
    ))
  }

  return (
    <section className="py-32 px-6" style={{ background: 'var(--bg-surface)' }}>
      <div className="max-w-2xl mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} className="text-center mb-8">
          <h2 className="text-3xl mb-4">批判性 AI</h2>
          <p className="text-[var(--text-secondary)]">不是应声虫，而是会挑战假设的伙伴</p>
        </motion.div>

        {/* Traits */}
        <div className="flex justify-center gap-4 mb-8">
          {traits.map((t, i) => (
            <motion.div
              key={t.label}
              initial={{ opacity: 0, y: 10 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -3 }}
              className="px-4 py-3 rounded-lg border border-white/5 text-center"
              style={{ background: 'var(--bg-elevated)' }}
            >
              <t.icon size={18} className="mx-auto mb-2 text-[var(--accent-gold)]" />
              <div className="text-xs text-[var(--text-secondary)]">{t.label}</div>
            </motion.div>
          ))}
        </div>

        {/* Chat */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="rounded-xl p-5 border border-white/10"
          style={{ background: 'var(--bg-elevated)' }}
        >
          <div className="flex items-center justify-between mb-5 pb-4 border-b border-white/5">
            <div className="flex items-center gap-2 text-sm text-[var(--text-muted)]">
              <div className="w-2 h-2 rounded-full bg-[var(--accent-sage)]" />
              AI 协作对话
            </div>
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              onClick={playConversation}
              disabled={isPlaying}
              className="px-3 py-1.5 rounded-lg text-xs flex items-center gap-1.5 transition-colors disabled:opacity-50"
              style={{ background: 'var(--accent-gold)20', color: 'var(--accent-gold)' }}
            >
              <Play size={12} /> {isPlaying ? '播放中...' : '演示对话'}
            </motion.button>
          </div>

          <div className="space-y-3 min-h-[240px]">
            <AnimatePresence>
              {conversation.slice(0, visibleCount).map((msg, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 8 }}
                  animate={{ opacity: 1, y: 0 }}
                  className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  {msg.role === 'ai' && (
                    <div className="w-7 h-7 rounded-full flex items-center justify-center mr-2 flex-shrink-0" style={{ background: 'var(--accent-gold)20' }}>
                      <Bot size={14} className="text-[var(--accent-gold)]" />
                    </div>
                  )}
                  <div
                    className={`max-w-[75%] px-4 py-2.5 rounded-xl text-sm ${
                      msg.role === 'user' ? 'rounded-br-sm' : 'rounded-bl-sm border'
                    }`}
                    style={{
                      background: msg.role === 'user' ? 'var(--bg-deep)' : 'var(--bg-surface)',
                      borderColor: msg.role === 'ai' ? 'var(--accent-gold)20' : 'transparent',
                      color: 'var(--text-secondary)'
                    }}
                  >
                    {highlightText(msg.text, msg.highlight)}
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>

            {isPlaying && visibleCount < conversation.length && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex items-center gap-2">
                <div className="w-7 h-7 rounded-full flex items-center justify-center" style={{ background: 'var(--accent-gold)20' }}>
                  <Bot size={14} className="text-[var(--accent-gold)]" />
                </div>
                <div className="flex gap-1 px-4 py-2.5 rounded-xl rounded-bl-sm" style={{ background: 'var(--bg-surface)' }}>
                  {[0, 1, 2].map(i => (
                    <motion.div
                      key={i}
                      animate={{ y: [0, -3, 0] }}
                      transition={{ duration: 0.5, repeat: Infinity, delay: i * 0.15 }}
                      className="w-1.5 h-1.5 rounded-full bg-[var(--accent-gold)]"
                    />
                  ))}
                </div>
              </motion.div>
            )}
          </div>
        </motion.div>

        <div className="mt-6 text-center text-xs text-[var(--text-muted)]">
          核心原则：文献是真相，讨论是中心
        </div>
      </div>
    </section>
  )
}
