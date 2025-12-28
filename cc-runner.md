# 行动指南（cc-runner）

目标：在不泄露敏感信息的前提下，让本项目可重复启动、可验证、可发布，并最终推送到 GitHub 仓库。

约束：
- 先规划、后开发；本文件仅描述行动计划，不直接修改业务代码逻辑。
- 全程记录关键决策、问题与解决方案到 dev_log.md。
- 不在仓库中保留任何 API Key、Token、密码等敏感信息。

---

## 0. 基线检查（不改代码）
1. 检查项目根目录结构是否完整：
   - backend/（FastAPI 后端）
   - frontend/（Electron + Vite + React 前端）
   - README.md（使用说明）
2. 确认本地运行环境信息（仅记录到 dev_log.md）：
   - Windows 版本、Node 版本、Python 版本
   - 是否存在已运行占用端口的旧进程

---

## 1. 敏感信息与仓库卫生（先做这个再推送）
1. 全盘扫描敏感信息：
   - 搜索关键词：key、token、secret、Deepseek、OPENAI、API_KEY 等
   - 查找明显敏感文件（例如 “*key*.txt”）
2. 处理敏感信息（按优先级）：
   - 删除/移出仓库内的敏感文件（如包含 API Key 的文本文件）
   - 统一改为从环境变量或本地不入库配置文件读取（例如 .env）
3. 补齐 .gitignore（至少覆盖以下类别）：
   - Python：__pycache__/、venv/、.venv/、*.pyc、dist/、build/
   - Node：node_modules/、dist/、.vite/、*.log
   - Electron 打包产物：dist-electron/、release/ 等（以项目现状为准）
   - 本地配置：.env、.env.*、*.local
4. 在 dev_log.md 记录：
   - 哪些敏感点被发现与如何处理
   - .gitignore 的关键条目与原因

---

## 2. 后端可运行性验证（FastAPI）
1. 创建/激活 Python 虚拟环境（venv 或 .venv）。
2. 安装依赖：
   - 使用 backend/requirements.txt
3. 启动后端服务并验证：
   - 启动方式以 README.md 为准
   - 访问健康检查接口（如 /health 或等价路径）
4. 验证核心接口：
   - 文档解析接口（上传 docx/pptx/pdf，确认返回文本）
   - 生成接口（确认能够返回草稿，必要时验证流式返回）
5. 如出现错误：
   - 记录报错堆栈、复现步骤、修复方案到 dev_log.md

---

## 3. 前端可运行性验证（Vite + React + Electron）
1. 安装前端依赖：
   - 在 frontend/ 执行 npm install
2. 启动前端开发模式：
   - 在浏览器验证页面渲染与路由
3. 启动 Electron（如项目脚本支持）：
   - 验证窗口加载、与后端通信是否正常
4. 重点回归：
   - 编辑页渲染与内容展示区域是否正常填充
   - 生成结果展示是否存在截断/样式溢出
5. 如出现端口占用或资源加载错误：
   - 记录冲突进程与解决方式到 dev_log.md

---

## 4. 最小化质量门禁（在推送前完成）
1. 运行前端 lint / typecheck（以 package.json scripts 为准）。
2. 运行后端基础检查：
   - 至少能启动、关键接口可调用
3. 若存在测试框架：
   - 运行测试并确保通过
4. 将执行结果与异常处理记录到 dev_log.md。

---

## 5. Git 初始化与推送（最后做）
1. 确认仓库中不包含敏感信息与大体积构建产物。
2. 初始化 Git 仓库并配置 remote：
   - remote 指向：https://github.com/Chiward/xuanchaungao2.git
3. 进行一次干净的首次提交：
   - 提交信息说明本次内容（例如 “init project”）
4. 推送到远程分支（main/master 以仓库设置为准）。
5. 推送后自检：
   - GitHub 上浏览关键文件是否齐全
   - README 中的启动步骤能否复现

