# 智能宣传稿生成助手

基于 AI 大模型的企业宣传稿智能生成工具，支持多场景模板、素材解析与智能写作。

## ✨ 核心功能

*   **多场景模板**：内置重要会议、培训活动、领导带队检查、项目中标、项目重大进展、科技创新 6 大核心场景模板。
*   **智能素材解析**：支持上传 Word (.docx)、PPT (.pptx)、PDF 等格式的参考素材，自动提取核心内容。
*   **AI 智能写作**：基于 Deepseek 大模型，结合用户输入的关键要素（时间、地点、人物、核心内容），一键生成高质量初稿。
*   **范文参考功能**：自动加载 `examples` 文件夹中对应类型的范文，遵循其文章结构框架、语言表达风格及内容组织逻辑，确保生成的宣传稿风格一致。
*   **富文本编辑**：内置所见即所得编辑器，支持 Markdown 实时预览与格式转换，生成结果自动排版。
*   **一键导出**：支持将编辑好的宣传稿一键导出为 Word 文档 (.doc)。

## 🛠 技术栈

*   **前端**：Electron + React + TypeScript + Ant Design + Vite
*   **后端**：Python + FastAPI + Uvicorn
*   **AI 服务**：Deepseek API (OpenAI Compatible)
*   **文档处理**：python-docx, python-pptx, PyPDF2

## 🚀 快速开始

### 前置要求

*   [Node.js](https://nodejs.org/) (v16+)
*   [Python](https://www.python.org/) (v3.10+)
*   Deepseek API Key (请申请并准备好 key)

### 1. 后端环境配置

```bash
cd backend

# 创建并激活虚拟环境 (可选)
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

**配置 API Key**：
使用环境变量 `DEEPSEEK_API_KEY`（推荐），或在项目根目录创建 `.env` 文件写入 `DEEPSEEK_API_KEY=sk-xxxx`。

Windows（PowerShell）示例：

```powershell
$env:DEEPSEEK_API_KEY="sk-xxxx"
```

### 2. 前端环境配置

```bash
cd frontend

# 安装依赖
npm install
```

### 3. 启动应用

**开发模式（推荐）**：

需要同时启动后端和前端服务。

*   **终端 1 (后端)**：
    ```bash
    cd backend
    # 确保虚拟环境已激活
    python main.py
    # 服务将运行在 http://127.0.0.1:8000
    ```

*   **终端 2 (前端)**：
    ```bash
    cd frontend
    npm run dev
    ```
    该命令将启动 Electron 窗口并加载应用。

## 📦 打包部署

### 后端打包

```bash
cd backend
pyinstaller main.py --onefile --name server --clean --distpath dist
```
打包完成后，生成的 `server.exe` 位于 `backend/dist` 目录。

### 前端打包 (Electron)

确保后端打包好的 `server.exe` 已经复制到 `frontend/resources` 目录下（开发脚本中已包含此逻辑，手动操作请注意）。

```bash
cd frontend
npm run build
npm run dist
```
打包后的安装包将位于 `frontend/dist` 目录。

## 📂 项目结构

```
xuanchuangao2/
├── backend/                # Python 后端
│   ├── service/            # 核心服务逻辑 (LLM, Parser)
│   ├── main.py             # FastAPI 入口
│   ├── config.py           # 配置加载
│   └── requirements.txt    # Python 依赖
├── frontend/               # React + Electron 前端
│   ├── electron/           # Electron 主进程代码
│   ├── src/                # React 页面与组件
│   │   ├── pages/          # 页面 (Home, Input, Edit)
│   │   └── App.tsx         # 路由配置
│   ├── resources/          # 静态资源 (含后端 exe)
│   └── package.json        # Node 依赖与脚本
├── cc-runner.md            # 项目行动指南
├── dev_log.md              # 研发日志
└── README.md               # 项目说明文档
```

## 📄 许可证

MIT License
