# MVP 启动指南

## 已完成的功能 ✅

### 1. Mem0 记忆系统（完整向量搜索模式）

- ✅ 自动记忆存储和搜索（Mem0 向量搜索）
- ✅ MEMORY.md 自动同步
- ✅ 冲突检测逻辑
- ✅ 记忆分类系统（preference, decision, insight, constraint, correction, inspiration）
- ✅ ZhipuAI embeddings (embedding-3, 2048维)
- ✅ LangChain集成
- ✅ Agent级别集成（Academic Partner）

**状态**: ✅ Mem0向量搜索已完全启用，双层记忆系统（Mem0 + MEMORY.md）正常工作

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

**基础测试**:

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
  [OK] Mem0 memory layer enabled (Zhipu AI via LangChain)
  Mem0启用状态: True  # 向量搜索模式
  Mem0实例: True

[测试2] 添加测试记忆...
  [OK] Memory added successfully: {'added': True, ...}

[测试3] 搜索记忆...
  [OK] Found X related memories
  OK 所有测试通过（Mem0模式）
```

**完整集成测试**:

```powershell
python tests/test_memory_integration.py
```

**测试内容**:
- ✅ Mem0向量搜索
- ✅ 记忆添加和检索
- ✅ 冲突检测
- ✅ 分类过滤（6种类别）
- ✅ 项目上下文获取
- ✅ MEMORY.md自动同步

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

## 已完成的优化 ✅

1. **Mem0配置问题已解决**
   - ✅ 修复：使用 `openai_base_url` 参数替代 `api_base`
   - ✅ 集成：通过LangChain provider使用ZhipuAI embeddings
   - ✅ 结果：Mem0向量搜索完全启用，2048维embedding正常工作

2. **记忆系统完整集成**
   - ✅ 在network.yaml中注册memory_system mod
   - ✅ 创建memory_tools.py工具包装器
   - ✅ Agent级别集成（Academic Partner）
   - ✅ 完整的端到端测试

3. **Windows编码问题**
   - ✅ 解决：测试脚本使用English输出
   - ✅ 影响：不影响功能，仅改善显示

### 后续优化方向

#### 短期（1-2周）
- [ ] 增强冲突检测（使用语义相似度阈值）
- [ ] 添加记忆系统Web UI界面
- [ ] 记忆导出/导入功能

#### 中期（1个月）
- [ ] Literature Agent集成记忆系统
- [ ] PR Manager集成历史决策查询
- [ ] 记忆系统性能优化（缓存、批量操作）

---

## 验收标准

### 完整版已达成 ✅

#### 记忆系统
- ✅ Mem0向量搜索启用（ZhipuAI embedding-3）
- ✅ MEMORY.md自动同步（双层记忆）
- ✅ Agent调用记忆工具（Academic Partner集成）
- ✅ 冲突检测主动提醒
- ✅ 完整的测试覆盖（基础测试 + 集成测试）
- ✅ 6种记忆分类全部工作

#### PDF上传系统
- ✅ 能通过Web界面上传PDF
- ✅ 上传后自动转换并移至Uncited/
- ✅ FastAPI后端服务
- ✅ DataLab API集成

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

**Q: Mem0向量搜索已启用吗？**
A: ✅ 是的！系统使用ZhipuAI embedding-3 (2048维) 进行向量搜索，同时保留MEMORY.md备份。

**Q: 如何验证记忆系统工作状态？**
A: 运行 `python tests/test_mem0_init.py` 或 `python tests/test_memory_integration.py`，应显示 "Mem0启用状态: True"。

**Q: 上传的PDF去哪了？**
A: 转换后的MD在`Reference/Uncited/`，原PDF在`Reference/PDF-MD/pdfs_done/`。

**Q: 如何查看记忆系统的输出？**
A: 查看项目根目录的`MEMORY.md`文件（自动同步），或通过memory_tools.py API查询。

**Q: DataLab API需要配置吗？**
A: 需要在`Reference/PDF-MD/convert_api.py`中设置`DATALAB_API_KEY`环境变量。

**Q: 记忆系统支持哪些类别？**
A: 6种类别：preference（偏好）、decision（决策）、insight（洞察）、constraint（约束）、correction（纠正）、inspiration（灵感）。

---

## 下一步行动

1. **立即可测试**: 运行 `python tests/test_memory_integration.py` 验证完整功能
2. **启动网络**: 启动Academic Network，测试Agent与记忆系统交互
3. **优化方向**: 考虑添加记忆系统Web UI界面，导出/导入功能

---

## 相关文档

- 完整实施计划: `C:\Users\Lenovo\.claude\plans\tingly-churning-yeti.md`
- Mem0文档: https://docs.mem0.ai/
- OpenAgents文档: 使用 `/help` 查看

---

**更新时间**: 2025-12-28 16:00
**版本**: v2.0 - Full Vector Search Release
