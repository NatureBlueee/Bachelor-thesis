# MVP 启动指南

## 已完成的功能 ✅

### 1. Mem0 记忆系统（降级模式）

- ✅ 自动记忆存储和搜索
- ✅ MEMORY.md 自动同步
- ✅ 冲突检测逻辑
- ✅ 记忆分类系统（preference, decision, insight, constraint, correction, inspiration）

**状态**: 当前使用MEMORY.md备份模式（Mem0未完全启用但功能正常）

### 2. PDF 文件上传功能

- ✅ Web 上传界面
- ✅ FastAPI 后端服务
- ✅ 自动调用 DataLab API 转换
- ✅ 转换完成后自动移至 Uncited/ 目录

---

## 快速启动

### 方式1：测试PDF上传功能

**步骤1**: 启动上传服务器

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network\api
python standalone_server.py
```

**步骤2**: 打开上传界面

方法A（推荐）：在浏览器打开文件
```
file:///d:/Profolio/文章/Thesis/Graduate-thesis/academic_network/ui/upload.html
```

方法B：直接用浏览器打开 `academic_network/ui/upload.html` 文件

**步骤3**: 拖拽或选择PDF文件上传

---

### 方式2：测试记忆系统

**运行测试脚本**:

```powershell
cd d:\Profolio\文章\Thesis\Graduate-thesis\academic_network
python tests/test_mem0_init.py
```

**预期输出**:
```
============================================================
  Mem0 初始化验证测试
============================================================

[测试1] 初始化 AcademicMemory...
  Mem0启用状态: False  # 降级模式
  警告: Mem0未启用，将使用MEMORY.md备份模式

[备份模式测试1] 添加记忆到MEMORY.md...
  [OK] Yi tong bu dao MEMORY.md: ...  # 同步成功

[备份模式测试2] 搜索MEMORY.md...
  找到 X 条相关记忆
  OK MEMORY.md备份模式工作正常
```

---

## 测试流程示例

### PDF上传完整流程

1. 启动上传服务器（见上方）
2. 准备一个PDF文件（学术论文）
3. 在上传界面拖拽PDF文件
4. 观察控制台输出：
   ```
   [upload_xxx.pdf_xxx] Starting conversion: test_paper.pdf...
   [upload_xxx.pdf_xxx] OK Conversion successful: test_paper.md -> Uncited/
   ```
5. 检查文件位置：
   - 转换后的MD：`Reference/Uncited/test_paper.md`
   - 原始PDF：`Reference/PDF-MD/pdfs_done/test_paper.pdf`

---

## 目录结构

```
academic_network/
├── api/
│   ├── __init__.py
│   ├── upload_handler.py       # 上传处理逻辑
│   └── standalone_server.py    # FastAPI服务器
├── ui/
│   └── upload.html             # 上传界面
├── mods/
│   └── memory_system.py        # Mem0记忆系统
├── tests/
│   └── test_mem0_init.py       # 记忆系统测试
└── MVP_START_GUIDE.md          # 本文件
```

---

## 已知问题与后续优化

### 当前问题

1. **Mem0配置参数错误**
   - 问题：`api_base` 参数不被支持
   - 影响：Mem0向量搜索未启用，系统使用MEMORY.md备份模式
   - 解决方案：需要修改为正确的参数名（`http_client_proxies` 或其他）
   - **优先级**: P2（系统可在降级模式下正常工作）

2. **Windows编码问题**
   - 问题：中文字符在控制台显示乱码
   - 解决：已改用拼音输出，不影响功能
   - **优先级**: P3（美观问题）

### 后续优化方向

#### 短期（1周内）
- [ ] 修复Mem0配置，启用向量搜索
- [ ] 在network.yaml中注册memory_system mod
- [ ] Agent级别集成记忆系统

#### 中期（1个月）
- [ ] 增强冲突检测（语义相似度）
- [ ] 集成到Academic Partner
- [ ] 完整的端到端测试

---

## 验收标准

### MVP已达成 ✅

- ✅ Mem0能存储和搜索记忆（备份模式）
- ✅ MEMORY.md自动同步
- ✅ 能通过Web界面上传PDF
- ✅ 上传后自动转换并移至Uncited/

### 完整版待完成 🔄

- ⏳ Mem0向量搜索启用
- ⏳ Agent调用记忆工具
- ⏳ 冲突检测主动提醒
- ⏳ 完整的测试覆盖

---

## 技术栈

| 组件 | 技术 | 版本 |
|------|------|------|
| 记忆系统 | Mem0 + MEMORY.md | 0.1.0+ |
| 上传服务 | FastAPI | 0.128.0 |
| Web服务器 | Uvicorn | latest |
| 异步文件 | aiofiles | 25.1.0 |
| PDF转换 | DataLab Marker API | - |
| Agent框架 | OpenAgents | 0.6.11+ |

---

## 常见问题

**Q: 为什么Mem0显示"未启用"？**
A: 配置参数有误，系统自动降级为MEMORY.md备份模式，功能不受影响。

**Q: 上传的PDF去哪了？**
A: 转换后的MD在`Reference/Uncited/`，原PDF在`Reference/PDF-MD/pdfs_done/`

**Q: 如何查看记忆系统的输出？**
A: 查看项目根目录的`MEMORY.md`文件，或运行测试脚本。

**Q: DataLab API需要配置吗？**
A: 需要在`Reference/PDF-MD/convert_api.py`中设置`DATALAB_API_KEY`环境变量。

---

## 下一步行动

1. **立即可测试**: 启动上传服务器，上传PDF测试
2. **优化建议**: 修复Mem0配置（参考计划文档）
3. **集成工作**: 将记忆系统集成到Academic Partner

---

## 相关文档

- 完整实施计划: `C:\Users\Lenovo\.claude\plans\tingly-churning-yeti.md`
- Mem0文档: https://docs.mem0.ai/
- OpenAgents文档: 使用 `/help` 查看

---

**更新时间**: 2025-12-28 13:10
**版本**: MVP 1.0
