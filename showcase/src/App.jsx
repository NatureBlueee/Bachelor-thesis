import Hero from './components/Hero'
import WorkflowDiagram from './components/WorkflowDiagram'
import Terminal from './components/Terminal'
import PRShowcase from './components/PRShowcase'
import FileTree from './components/FileTree'
import AIPersona from './components/AIPersona'

export default function App() {
  return (
    <div className="min-h-screen text-[var(--text-primary)] relative" style={{ background: 'var(--bg-deep)' }}>
      {/* Subtle grid texture */}
      <div
        className="fixed inset-0 pointer-events-none opacity-[0.03]"
        style={{
          backgroundImage: `linear-gradient(var(--text-muted) 1px, transparent 1px),
                           linear-gradient(90deg, var(--text-muted) 1px, transparent 1px)`,
          backgroundSize: '64px 64px'
        }}
      />

      <div className="relative z-10">
        <Hero />
        <WorkflowDiagram />
        <Terminal />
        <PRShowcase />
        <FileTree />
        <AIPersona />

        <footer className="py-16 text-center border-t border-white/5">
          <p className="text-[var(--text-muted)] text-sm tracking-wide mb-3">论文工程化协作系统</p>
          <a
            href="https://github.com"
            className="text-xs text-[var(--text-muted)] hover:text-[var(--accent-gold)] transition-colors duration-300"
          >
            MIT License · GitHub
          </a>
        </footer>
      </div>
    </div>
  )
}
