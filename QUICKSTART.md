# 快速启动指南

## 🚀 3步快速启动

### 第1步：配置 API Key
编辑项目根目录下的 `.env` 文件，将 `DEEPSEEK_API_KEY=sk-xxxx` 替换为你的实际 API Key。

### 第2步：启动应用
双击运行 `start-all.bat` 文件，将自动启动后端服务和前端应用。

### 第3步：开始使用
Electron 窗口打开后，你就可以开始使用智能宣传稿生成助手了！

---

## 📋 详细说明

### 如果没有 API Key
1. 访问 [Deepseek 官网](https://www.deepseek.com/) 申请 API Key
2. 将获取的 API Key 填入 `.env` 文件
3. 重新启动应用

### 如果只想启动后端或前端
- **仅启动后端**：双击 `start-backend.bat`
- **仅启动前端**：双击 `start-frontend.bat`

### 手动启动（高级用户）
打开两个终端窗口：

**终端1（后端）：**
```bash
cd backend
python main.py
```

**终端2（前端）：**
```bash
cd frontend
npm run dev
```

---

## ✅ 验证是否成功

### 方法1：检查后端
在浏览器中访问：http://127.0.0.1:8000/health

如果看到 `{"status":"ok","llm_ready":true}`，说明后端运行正常。

### 方法2：检查前端
如果看到 Electron 窗口打开并显示应用界面，说明前端运行正常。

---

## 🎯 核心功能

1. **选择模板**：从6个预设模板中选择一个
2. **上传素材**：上传 Word、PPT 或 PDF 文件作为参考
3. **填写信息**：输入时间、地点、人物、核心内容
4. **生成初稿**：AI 自动生成宣传稿初稿
5. **编辑优化**：在编辑器中修改和完善
6. **导出文档**：一键导出为 Word 文档

---

## ❓ 常见问题

### Q: 启动失败怎么办？
A: 检查端口 8000 和 5173 是否被占用，关闭占用端口的程序后重试。

### Q: AI 生成功能不工作？
A: 确认 `.env` 文件中的 API Key 是否正确配置。

### Q: 如何停止应用？
A: 关闭对应的命令行窗口即可。

---

## 📞 获取帮助

- 查看 `DEPLOYMENT.md` 了解详细部署信息
- 查看 `README.md` 了解项目详情
- 访问 GitHub 仓库：https://github.com/Chiward/xuanchaungao2.git

---

**祝你使用愉快！** 🎉
