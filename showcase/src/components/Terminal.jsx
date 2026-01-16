import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Terminal as TerminalIcon, Check, Loader2 } from 'lucide-react'

const commands = {
  '/start': {
    output: `论文项目状态

研究主题: AI素养对Z世代员工向上影响行为的影响
当前阶段: 理论框架完善

最近完成
  PR-0011 开题报告同步至论文正文

进行中
  PR-0012 访谈提纲设计

准备就绪。请问今天要做什么？`
  },
  '/create-pr': {
    output: `创建修改请求...

请回答：
1. 修改什么？（章节/段落）
2. 为什么修改？

示例输入：
> 修改P1表述，从"positively relates"改为"shapes"
> 理由：探索性研究不预设方向`
  },
  '/sync': {
    output: `同步检查...

  _CONTEXT.md ✓
  活动PR: PR-0012 (doing)
  MEMORY.md ✓

状态: 已同步，无需操作`
  },
  '/deep-read': {
    output: `深度阅读模式

请提供文献路径：
> Reference/PDF-MD/output_api/xxx.md

将输出：
  核心论点
  研究方法
  与本研究的关联
  可引用段落`
  },
  '/reflect': {
    output: `反思提取...

检查最近对话...
发现 2 条值得记录的洞见：

1. "探索性研究不预设方向" → 已记录
2. "shapes比positively relates更中性" → 已记录

MEMORY.md 已更新`
  }
}

const suggestions = Object.keys(commands)

export default function Terminal() {
  const [history, setHistory] = useState([])
  const [input, setInput] = useState('')
  const [typing, setTyping] = useState(false)
  const [showSuggestions, setShowSuggestions] = useState(false)
  const inputRef = useRef(null)
  const containerRef = useRef(null)

  const filteredSuggestions = suggestions.filter(s => s.startsWith(input) && input.length > 0)

  const typeOutput = (text) => {
    setTyping(true)
    let i = 0
    const interval = setInterval(() => {
      if (i < text.length) {
        setHistory(prev => {
          const newHistory = [...prev]
          newHistory[newHistory.length - 1].output = text.slice(0, i + 1)
          return newHistory
        })
        i += 3
      } else {
        clearInterval(interval)
        setTyping(false)
      }
    }, 10)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const cmd = input.trim()
    if (!cmd || typing) return

    const result = commands[cmd]
    setHistory(prev => [...prev, { cmd, output: '' }])
    setInput('')
    setShowSuggestions(false)

    if (result) {
      setTimeout(() => typeOutput(result.output), 100)
    } else {
      setTimeout(() => {
        setHistory(prev => {
          const newHistory = [...prev]
          newHistory[newHistory.length - 1].output = `未知命令: ${cmd}\n可用: ${suggestions.join(', ')}`
          return newHistory
        })
      }, 100)
    }
  }

  const handleSuggestionClick = (suggestion) => {
    setInput(suggestion)
    setShowSuggestions(false)
    inputRef.current?.focus()
  }

  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight
    }
  }, [history])

  return (
    <section className="py-32 px-6">
      <div className="max-w-3xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <h2 className="text-3xl mb-4">斜杠命令</h2>
          <p className="text-[var(--text-secondary)]">试试输入 / 开始</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="rounded-xl overflow-hidden border border-white/10"
          style={{ background: 'var(--bg-elevated)' }}
        >
          {/* Title bar */}
          <div className="flex items-center gap-3 px-4 py-3 border-b border-white/5" style={{ background: 'var(--bg-surface)' }}>
            <div className="flex gap-1.5">
              <div className="w-3 h-3 rounded-full bg-[var(--accent-coral)]/60" />
              <div className="w-3 h-3 rounded-full bg-[var(--accent-gold)]/60" />
              <div className="w-3 h-3 rounded-full bg-[var(--accent-sage)]/60" />
            </div>
            <div className="flex items-center gap-2 text-xs text-[var(--text-muted)]">
              <TerminalIcon size={12} />
              <span>thesis-terminal</span>
            </div>
            {typing && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="ml-auto flex items-center gap-1.5 text-xs text-[var(--accent-sage)]">
                <Loader2 size={12} className="animate-spin" />
                <span>运行中</span>
              </motion.div>
            )}
          </div>

          {/* Content */}
          <div
            ref={containerRef}
            className="p-4 h-80 overflow-y-auto"
            style={{ fontFamily: 'var(--font-mono)' }}
            onClick={() => inputRef.current?.focus()}
          >
            {history.length === 0 && (
              <div className="text-[var(--text-muted)] text-sm">
                <p>欢迎使用论文协作系统终端</p>
                <p className="mt-3 mb-2">可用命令：</p>
                {suggestions.map(s => (
                  <div
                    key={s}
                    onClick={() => handleSuggestionClick(s)}
                    className="text-[var(--accent-gold)] cursor-pointer hover:opacity-70 transition-opacity py-0.5"
                  >
                    {s}
                  </div>
                ))}
              </div>
            )}

            {history.map((item, i) => (
              <motion.div key={i} initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mb-4 text-sm">
                <div className="flex items-center gap-2 text-[var(--accent-gold)]">
                  <span>›</span>
                  <span>{item.cmd}</span>
                </div>
                <pre className="mt-2 text-[var(--text-secondary)] whitespace-pre-wrap leading-relaxed pl-4">
                  {item.output}
                  {typing && i === history.length - 1 && (
                    <motion.span animate={{ opacity: [1, 0] }} transition={{ duration: 0.5, repeat: Infinity }} className="text-[var(--accent-gold)]">▋</motion.span>
                  )}
                </pre>
              </motion.div>
            ))}

            {/* Input */}
            <div className="relative">
              <form onSubmit={handleSubmit} className="flex items-center gap-2 text-sm">
                <span className="text-[var(--accent-gold)]">›</span>
                <input
                  ref={inputRef}
                  type="text"
                  value={input}
                  onChange={(e) => { setInput(e.target.value); setShowSuggestions(e.target.value.startsWith('/')) }}
                  onFocus={() => setShowSuggestions(input.startsWith('/'))}
                  onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
                  className="flex-1 bg-transparent outline-none text-[var(--text-primary)]"
                  style={{ fontFamily: 'var(--font-mono)', caretColor: 'var(--accent-gold)' }}
                  disabled={typing}
                />
              </form>

              <AnimatePresence>
                {showSuggestions && filteredSuggestions.length > 0 && (
                  <motion.div
                    initial={{ opacity: 0, y: -5 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0 }}
                    className="absolute bottom-full left-4 mb-2 rounded-lg border border-white/10 overflow-hidden"
                    style={{ background: 'var(--bg-surface)' }}
                  >
                    {filteredSuggestions.map(s => (
                      <div key={s} onClick={() => handleSuggestionClick(s)} className="px-4 py-2 text-sm cursor-pointer hover:bg-white/5 text-[var(--text-secondary)] hover:text-[var(--accent-gold)]">
                        {s}
                      </div>
                    ))}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </motion.div>

        {/* Quick buttons */}
        <div className="flex justify-center gap-2 mt-6 flex-wrap">
          {suggestions.map(cmd => (
            <motion.button
              key={cmd}
              whileHover={{ y: -2 }}
              onClick={() => { setInput(cmd); inputRef.current?.focus() }}
              className="px-3 py-1.5 text-xs text-[var(--text-muted)] hover:text-[var(--accent-gold)] rounded-lg border border-white/5 hover:border-[var(--accent-gold)]/30 transition-all duration-300"
              style={{ fontFamily: 'var(--font-mono)' }}
            >
              {cmd}
            </motion.button>
          ))}
        </div>
      </div>
    </section>
  )
}
