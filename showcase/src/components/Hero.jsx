import { motion } from 'framer-motion'
import { useState, useEffect } from 'react'
import { GitPullRequest, Check, GitMerge } from 'lucide-react'

export default function Hero() {
  const [stage, setStage] = useState(0) // 0: typing, 1: pending, 2: merged

  useEffect(() => {
    const timers = [
      setTimeout(() => setStage(1), 2000),
      setTimeout(() => setStage(2), 4000),
    ]
    return () => timers.forEach(clearTimeout)
  }, [])

  return (
    <section className="min-h-screen flex items-center justify-center px-6 relative overflow-hidden">
      <div className="max-w-5xl mx-auto w-full grid md:grid-cols-2 gap-12 items-center">

        {/* Left: Title */}
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="text-5xl md:text-6xl tracking-tight mb-6 leading-tight">
            用 <span className="text-[var(--accent-gold)]">PR</span> 写论文
          </h1>
          <p className="text-xl text-[var(--text-secondary)] mb-8">
            工程化思维 × AI 协作
          </p>
          <div className="flex gap-3 text-sm text-[var(--text-muted)]">
            <span className="px-3 py-1.5 rounded-full" style={{ background: 'var(--bg-surface)' }}>可追溯</span>
            <span className="px-3 py-1.5 rounded-full" style={{ background: 'var(--bg-surface)' }}>有记忆</span>
            <span className="px-3 py-1.5 rounded-full" style={{ background: 'var(--bg-surface)' }}>批判性</span>
          </div>
        </motion.div>

        {/* Right: Animated PR Card */}
        <motion.div
          initial={{ opacity: 0, x: 30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="rounded-2xl p-6 border"
          style={{ background: 'var(--bg-elevated)', borderColor: stage === 2 ? 'var(--accent-sage)' : 'var(--accent-gold)30' }}
        >
          {/* PR Header */}
          <div className="flex items-center gap-3 mb-4">
            <div className="w-10 h-10 rounded-xl flex items-center justify-center" style={{ background: stage === 2 ? 'var(--accent-sage)20' : 'var(--accent-gold)20' }}>
              {stage === 2 ? <GitMerge size={20} className="text-[var(--accent-sage)]" /> : <GitPullRequest size={20} className="text-[var(--accent-gold)]" />}
            </div>
            <div className="flex-1">
              <div className="font-medium">PR-0006</div>
              <div className="text-sm text-[var(--text-muted)]">方法论调整</div>
            </div>
            <motion.div
              animate={{ scale: stage === 2 ? [1, 1.1, 1] : 1 }}
              className="px-3 py-1 rounded-full text-xs"
              style={{
                background: stage === 2 ? 'var(--accent-sage)20' : 'var(--accent-gold)20',
                color: stage === 2 ? 'var(--accent-sage)' : 'var(--accent-gold)'
              }}
            >
              {stage === 2 ? 'merged' : 'pending'}
            </motion.div>
          </div>

          {/* Diff Preview */}
          <div className="rounded-lg p-4 text-sm font-mono" style={{ background: 'var(--bg-deep)' }}>
            <div className="text-[var(--accent-coral)] opacity-70">- AI literacy determines...</div>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: stage >= 1 ? 1 : 0 }}
              className="text-[var(--accent-sage)]"
            >
              + AI literacy <span className="underline">shapes</span>...
            </motion.div>
          </div>

          {/* Reason */}
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: stage >= 1 ? 1 : 0, y: stage >= 1 ? 0 : 10 }}
            className="mt-4 text-sm text-[var(--text-secondary)] flex items-start gap-2"
          >
            <Check size={16} className="mt-0.5 text-[var(--accent-sage)]" />
            <span>探索性研究应使用中性动词</span>
          </motion.div>
        </motion.div>

      </div>

      {/* Scroll hint */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 3 }}
        className="absolute bottom-12 left-1/2 -translate-x-1/2 text-[var(--text-muted)] text-sm"
      >
        <motion.span animate={{ y: [0, 4, 0] }} transition={{ duration: 2, repeat: Infinity }} className="inline-block">
          ↓
        </motion.span>
      </motion.div>
    </section>
  )
}
