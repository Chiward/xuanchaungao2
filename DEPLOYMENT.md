# 部署说明文档

## 部署完成时间
2025-01-05

## 部署步骤总结

### 1. 克隆仓库
✅ 已成功从 GitHub 仓库 `https://github.com/Chiward/xuanchaungao2.git` 克隆到 `d:\AI project\xuanchuangao`

### 2. 安装后端依赖
✅ 已在 `backend` 目录下安装所有 Python 依赖：
- fastapi
- uvicorn
- python-docx
- python-pptx
- PyPDF2
- openai
- pydantic
- python-multipart
- pyinstaller

### 3. 安装前端依赖
✅ 已在 `frontend` 目录下安装所有 Node.js 依赖（627个包）

### 4. 配置环境变量
✅ 已创建 `.env` 文件和 `.env.example` 文件
⚠️ **重要提示**：需要将 `.env` 文件中的 `DEEPSEEK_API_KEY=sk-xxxx` 替换为实际的 Deepseek API Key

### 5. 项目结构
```
xuanchuangao/
├── .env                    # 环境变量配置文件（需要配置 API Key）
├── .env.example            # 环境变量示例文件
├── .gitignore
├── .vscode/
├── README.md
├── DEPLOYMENT.md           # 本部署说明文档
├── backend/
│   ├── config.py           # 配置加载
│   ├── main.py             # FastAPI 入口
│   ├── requirements.txt    # Python 依赖
│   └── service/            # 核心服务逻辑
│       ├── __init__.py
│       ├── llm.py          # LLM 服务
│       ├── parser.py       # 文档解析
│       └── prompts.py      # 提示词模板
└── frontend/
    ├── electron/           # Electron 主进程
    ├── index.html
    ├── package.json
    ├── src/                # React 源代码
    ├── tsconfig.electron.json
    └── vite.config.ts
```

## 启动应用

### 方法 1：使用启动脚本（推荐）

#### 一键启动（后端 + 前端）
双击运行 `start-all.bat` 文件，将自动启动后端服务和前端应用。

#### 单独启动后端
双击运行 `start-backend.bat` 文件，启动后端服务。

#### 单独启动前端
双击运行 `start-frontend.bat` 文件，启动前端应用。

### 方法 2：手动启动

#### 终端 1 - 启动后端服务
```bash
cd "d:\AI project\xuanchuangao\backend"
python main.py
```
后端服务将运行在 http://127.0.0.1:8000

#### 终端 2 - 启动前端应用
```bash
cd "d:\AI project\xuanchuangao\frontend"
npm run dev
```
该命令将启动 Electron 窗口并加载应用

### 验证部署

#### 1. 后端健康检查
启动后端服务后，访问：http://127.0.0.1:8000/health

预期响应：
```json
{
  "status": "ok",
  "llm_ready": true
}
```

如果 `llm_ready` 为 `false`，说明 API Key 未正确配置。

#### 2. 获取模板列表
访问：http://127.0.0.1:8000/templates

预期响应：包含 6 个模板名称的列表

## 配置 Deepseek API Key

### 方法 1：修改 .env 文件（推荐）
编辑 `d:\AI project\xuanchuangao\.env` 文件：
```
DEEPSEEK_API_KEY=your-actual-api-key-here
```

### 方法 2：使用环境变量
在 PowerShell 中设置：
```powershell
$env:DEEPSEEK_API_KEY="your-actual-api-key-here"
```

### 方法 3：创建 backend/.env 文件
在 `backend` 目录下创建 `.env` 文件：
```
DEEPSEEK_API_KEY=your-actual-api-key-here
```

## 功能特性

### 核心功能
1. **多场景模板**：内置 6 大核心场景模板
   - 重要会议
   - 培训活动
   - 领导带队检查
   - 项目中标
   - 项目重大进展
   - 科技创新

2. **智能素材解析**：支持多种文档格式
   - Word (.docx)
   - PPT (.pptx)
   - PDF

3. **AI 智能写作**：基于 Deepseek 大模型
   - 结合关键要素生成初稿
   - 支持流式输出

4. **富文本编辑**：所见即所得编辑器
   - Markdown 实时预览
   - 格式转换

5. **一键导出**：导出为 Word 文档 (.doc)

## 技术栈

- **前端**：Electron + React + TypeScript + Ant Design + Vite
- **后端**：Python + FastAPI + Uvicorn
- **AI 服务**：Deepseek API (OpenAI Compatible)
- **文档处理**：python-docx, python-pptx, PyPDF2

## 注意事项

1. **API Key 配置**：必须配置有效的 Deepseek API Key 才能使用 AI 生成功能
2. **端口占用**：确保 8000 端口（后端）和 5173 端口（前端开发服务器）未被占用
3. **Python 版本**：需要 Python 3.10 或更高版本
4. **Node.js 版本**：需要 Node.js 16 或更高版本

## 打包部署（可选）

### 后端打包
```bash
cd "d:\AI project\xuanchuangao\backend"
pyinstaller main.py --onefile --name server --clean --distpath dist
```

### 前端打包
```bash
cd "d:\AI project\xuanchuangao\frontend"
npm run build
npm run dist
```

## 故障排除

### 问题 1：后端启动失败
- 检查 Python 版本是否 >= 3.10
- 确认所有依赖已正确安装
- 检查端口 8000 是否被占用

### 问题 2：前端启动失败
- 检查 Node.js 版本是否 >= 16
- 确认所有依赖已正确安装
- 检查端口 5173 是否被占用

### 问题 3：AI 生成功能不工作
- 确认 API Key 已正确配置
- 检查网络连接
- 验证 API Key 是否有效

## 部署验证清单

- [x] 仓库已成功克隆
- [x] 后端依赖已安装
- [x] 前端依赖已安装
- [x] 环境变量配置文件已创建
- [ ] Deepseek API Key 已配置（需要用户手动配置）
- [x] 后端服务能够正常启动
- [x] 前端应用能够正常启动
- [x] 健康检查接口正常响应
- [x] 模板列表接口正常响应

## 下一步操作

1. **配置 API Key**：将 `.env` 文件中的 `DEEPSEEK_API_KEY` 替换为实际的 API Key
2. **启动后端服务**：在终端 1 中运行 `cd backend && python main.py`
3. **启动前端应用**：在终端 2 中运行 `cd frontend && npm run dev`
4. **验证功能**：在 Electron 应用中测试各个功能模块

## 联系方式

如有问题，请参考项目 README.md 或访问 GitHub 仓库：
https://github.com/Chiward/xuanchaungao2.git


