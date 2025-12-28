import React, { useEffect, useState, useRef } from 'react';
import { Button, Card, Spin, message, Space } from 'antd';
import { ArrowLeftOutlined, CopyOutlined, FileWordOutlined } from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import { marked } from 'marked';

const EditPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { template, data, contextText } = location.state || {};
  
  const [content, setContent] = useState("");
  const [isGenerating, setIsGenerating] = useState(true);
  const [rawMarkdown, setRawMarkdown] = useState("");
  const hasFetched = useRef(false);

  useEffect(() => {
    if (!location.state) {
        navigate('/');
        return;
    }
    if (hasFetched.current) return;
    hasFetched.current = true;

    generateDraft();
  }, []);

  const generateDraft = async () => {
    setIsGenerating(true);
    setRawMarkdown("");

    try {
        const response = await fetch('http://localhost:8000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                template_type: template,
                topic: data.topic,
                time: data.time,
                location: data.location,
                people: data.people,
                content: data.content,
                context_text: contextText
            }),
        });

        if (!response.body) return;
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let accumulatedMarkdown = "";

        // eslint-disable-next-line no-constant-condition
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            const chunk = decoder.decode(value, { stream: true });
            accumulatedMarkdown += chunk;
            setRawMarkdown(accumulatedMarkdown);
        }
        
        // Generation complete
        setIsGenerating(false);
        const html = await marked(accumulatedMarkdown);
        setContent(html);

    } catch (error) {
        console.error("Generation error:", error);
        message.error("生成出错");
        setIsGenerating(false);
    }
  };

  const handleCopy = () => {
      const editor = document.querySelector('.ql-editor');
      if (editor) {
          navigator.clipboard.writeText(editor.innerHTML).then(() => {
              message.success("已复制 HTML 内容");
          });
      }
  };

  const handleExport = () => {
      const header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' "+
            "xmlns:w='urn:schemas-microsoft-com:office:word' "+
            "xmlns='http://www.w3.org/TR/REC-html40'>"+
            "<head><meta charset='utf-8'><title>Export HTML to Word Document with JavaScript</title></head><body>";
       const footer = "</body></html>";
       const sourceHTML = header+content+footer;
       
       const source = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(sourceHTML);
       const fileDownload = document.createElement("a");
       document.body.appendChild(fileDownload);
       fileDownload.href = source;
       fileDownload.download = `${data.topic || '宣传稿'}.doc`;
       fileDownload.click();
       document.body.removeChild(fileDownload);
  };

  return (
    <div style={{ height: 'calc(100vh - 100px)', display: 'flex', flexDirection: 'column' }}>
        <div style={{ marginBottom: 16, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Button icon={<ArrowLeftOutlined />} onClick={() => navigate(-1)}>返回修改要素</Button>
            <Space>
                {isGenerating && <Spin tip="正在生成..." />}
                <Button icon={<CopyOutlined />} onClick={handleCopy} disabled={isGenerating}>复制全文</Button>
                <Button type="primary" icon={<FileWordOutlined />} onClick={handleExport} disabled={isGenerating}>导出 Word</Button>
            </Space>
        </div>
        
        <Card style={{ flex: 1, display: 'flex', flexDirection: 'column' }} bodyStyle={{ flex: 1, display: 'flex', flexDirection: 'column', padding: 0 }}>
             {isGenerating ? (
                 <div style={{ padding: 24, flex: 1, overflowY: 'auto', backgroundColor: '#f5f5f5', whiteSpace: 'pre-wrap', fontFamily: 'monospace' }}>
                     {rawMarkdown || "等待生成..."}
                 </div>
             ) : (
                <ReactQuill 
                    theme="snow" 
                    value={content} 
                    onChange={setContent} 
                    style={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                    modules={{
                        toolbar: [
                            [{ 'header': [1, 2, false] }],
                            ['bold', 'italic', 'underline', 'strike', 'blockquote'],
                            [{'list': 'ordered'}, {'list': 'bullet'}],
                            ['link', 'image'],
                            ['clean']
                        ],
                    }}
                />
             )}
             <style>{`
                .quill { display: flex; flex-direction: column; flex: 1; overflow: hidden; }
                .ql-container { flex: 1; overflow-y: auto; }
             `}</style>
        </Card>
    </div>
  );
};

export default EditPage;
