import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Check, Play, Circle, Loader2 } from 'lucide-react'

const prExample = {
  id: 'PR-0006',
  title: 'Methodology路线调整',
  date: '2025-12-20',
  scope: '命题表述 + 理论补丁 + 方法陈述',
  changes: [
    {
      location: 'P1表述 (Line 374)',
      before: 'AI literacy positively relates to employees\' perceived resource advantage.',
      after: 'AI literacy shapes employees\' perception of resource advantage.',
      reason: '"positively relates"是定量研究预设方向的写法。我们是探索，不是验证。"shapes"中性，不预设正负。',
      highlight: { before: 'positively relates', after: 'shapes' }
    },
    {
      location: 'P2表述 (Line 378)',
      before: 'Perceived resource advantage enables employees to engage in upward influence behavior.',
      after: 'Perceived resource advantage influences employees\' engagement in upward influence behavior.',
      reason: '"enables"太强——像是"有感知就一定会行动"。"influences"留出探索空间。',
      highlight: { before: 'enables', after: 'influences' }
    },
    {
      location: 'P3后 (Line 384)',
      before: '（无）',
      after: 'According to Tripathi (2021), employees who hold tacit resources must engage in "claiming" behaviors...',
      reason: '引入"claiming"概念，解释为什么感知是行动前提。',
      highlight: { before: '', after: 'Tripathi (2021)' }
    },
    {
      location: '3.5.2开头 (Line 612)',
      before: 'The coding process will combine deductive and inductive approaches.',
      after: 'This study employs theory-driven thematic analysis (Braun & Clarke, 2006).',
      reason: '上来就讲coding，没点明整体方法取向。一句话点明取向。',
      highlight: { before: '', after: 'theory-driven thematic analysis' }
    },
  ],
  checklist: [
    { text: 'P1: positively relates → shapes' },
    { text: 'P2: enables → influences' },
    { text: 'P3后: 加Tripathi引用' },
    { text: '3.5.2: 加theory-driven thematic analysis' },
    { text: '引用检查: Braun & Clarke (2006), Tripathi (2021)' },
  ],
}

const statusConfig = {
  pending: { color: 'var(--status-pending)', label: '待处理' },
  doing: { color: 'var(--status-doing)', label: '进行中' },
  merged: { color: 'var(--status-merged)', label: '已合并' }
}

export default function PRShowcase() {
  const [activeChange, setActiveChange] = useState(0)
  const [showChecklist, setShowChecklist] = useState(false)
  const [status, setStatus] = useState('merged')
  const [checkProgress, setCheckProgress] = useState(prExample.checklist.length)

  const simulateFlow = () => {
    setStatus('pending')
    setCheckProgress(0)
    setTimeout(() => setStatus('doing'), 800)
    prExample.checklist.forEach((_, i) => {
      setTimeout(() => setCheckProgress(i + 1), 1500 + i * 400)
    })
    setTimeout(() => setStatus('merged'), 1500 + prExample.checklist.length * 400 + 500)
  }

  const highlightText = (text, highlight) => {
    if (!highlight) return text
    const parts = text.split(highlight)
    return parts.map((part, i) => (
      <span key={i}>
        {part}
        {i < parts.length - 1 && <span className="bg-[var(--accent-gold)]/20 px-1 rounded">{highlight}</span>}
      </span>
    ))
  }

  return (
    <section className="py-32 px-6" style={{ background: 'var(--bg-surface)' }}>
      <div className="max-w-4xl mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} className="text-center mb-12">
          <h2 className="text-3xl mb-4">真实案例</h2>
          <p className="text-[var(--text-secondary)]">每次修改都有理由，都可追溯</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="rounded-xl p-6 border border-white/10"
          style={{ background: 'var(--bg-elevated)' }}
        >
          {/* Header */}
          <div className="flex items-start justify-between mb-6 flex-wrap gap-4">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <span className="text-[var(--accent-gold)] text-sm" style={{ fontFamily: 'var(--font-mono)' }}>{prExample.id}</span>
                <motion.span
                  key={status}
                  initial={{ scale: 0.9, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  className="px-2.5 py-1 rounded-md text-xs flex items-center gap-1.5"
                  style={{ backgroundColor: statusConfig[status].color + '20', color: statusConfig[status].color }}
                >
                  {status === 'doing' ? <Loader2 size={12} className="animate-spin" /> : <Circle size={10} fill="currentColor" />}
                  {statusConfig[status].label}
                </motion.span>
              </div>
              <h3 className="text-lg">{prExample.title}</h3>
              <p className="text-sm text-[var(--text-muted)] mt-1">{prExample.scope}</p>
            </div>
            <div className="text-right">
              <div className="text-sm text-[var(--text-muted)]">{prExample.date}</div>
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                onClick={simulateFlow}
                className="mt-2 px-4 py-2 rounded-lg text-sm flex items-center gap-2 transition-colors duration-300"
                style={{ background: 'var(--accent-gold)20', color: 'var(--accent-gold)' }}
              >
                <Play size={14} /> 演示流程
              </motion.button>
            </div>
          </div>

          {/* Change Tabs */}
          <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
            {prExample.changes.map((_, i) => (
              <motion.button
                key={i}
                onClick={() => setActiveChange(i)}
                whileHover={{ y: -2 }}
                className="px-4 py-2 rounded-lg text-sm whitespace-nowrap transition-all duration-300"
                style={{
                  background: activeChange === i ? 'var(--bg-deep)' : 'transparent',
                  border: `1px solid ${activeChange === i ? 'var(--accent-gold)' : 'rgba(255,255,255,0.05)'}`,
                  color: activeChange === i ? 'var(--accent-gold)' : 'var(--text-secondary)'
                }}
              >
                修改 {i + 1}
              </motion.button>
            ))}
          </div>

          {/* Change Detail */}
          <AnimatePresence mode="wait">
            <motion.div key={activeChange} initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
              <div className="text-xs text-[var(--text-muted)]" style={{ fontFamily: 'var(--font-mono)' }}>
                {prExample.changes[activeChange].location}
              </div>

              <div className="grid md:grid-cols-2 gap-4">
                <div className="rounded-lg p-4 border" style={{ background: 'var(--bg-deep)', borderColor: 'var(--accent-coral)30' }}>
                  <div className="text-xs text-[var(--accent-coral)] mb-2 flex items-center gap-2">− 原文</div>
                  <p className="text-sm text-[var(--text-secondary)] leading-relaxed">
                    {highlightText(prExample.changes[activeChange].before, prExample.changes[activeChange].highlight?.before)}
                  </p>
                </div>
                <div className="rounded-lg p-4 border" style={{ background: 'var(--bg-deep)', borderColor: 'var(--accent-sage)30' }}>
                  <div className="text-xs text-[var(--accent-sage)] mb-2 flex items-center gap-2">+ 修改后</div>
                  <p className="text-sm text-[var(--text-secondary)] leading-relaxed">
                    {highlightText(prExample.changes[activeChange].after, prExample.changes[activeChange].highlight?.after)}
                  </p>
                </div>
              </div>

              <div className="rounded-lg p-4 border border-white/5" style={{ background: 'var(--bg-deep)' }}>
                <div className="text-xs text-[var(--text-muted)] mb-2">修改理由</div>
                <p className="text-sm text-[var(--text-secondary)] leading-relaxed">{prExample.changes[activeChange].reason}</p>
              </div>
            </motion.div>
          </AnimatePresence>

          {/* Checklist */}
          <motion.button
            onClick={() => setShowChecklist(!showChecklist)}
            className="mt-6 text-sm text-[var(--text-muted)] hover:text-[var(--text-secondary)] flex items-center gap-2 transition-colors"
          >
            <motion.span animate={{ rotate: showChecklist ? 90 : 0 }} className="text-xs">▶</motion.span>
            验收清单 ({checkProgress}/{prExample.checklist.length})
          </motion.button>

          <AnimatePresence>
            {showChecklist && (
              <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }} className="mt-4 space-y-2 overflow-hidden">
                {prExample.checklist.map((item, i) => (
                  <motion.div key={i} initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.05 }} className="flex items-center gap-3 text-sm">
                    <motion.div
                      animate={{ backgroundColor: i < checkProgress ? 'var(--accent-sage)20' : 'transparent', borderColor: i < checkProgress ? 'var(--accent-sage)' : 'var(--text-muted)' }}
                      className="w-5 h-5 rounded border flex items-center justify-center"
                    >
                      {i < checkProgress && <Check size={12} className="text-[var(--accent-sage)]" />}
                    </motion.div>
                    <span className={i < checkProgress ? 'text-[var(--text-secondary)]' : 'text-[var(--text-muted)]'}>{item.text}</span>
                  </motion.div>
                ))}
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      </div>
    </section>
  )
}
