import React, { useState } from 'react';
import { Form, Input, DatePicker, Button, Upload, message, Card, Typography } from 'antd';
import { InboxOutlined, ArrowLeftOutlined } from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';
import dayjs from 'dayjs';

const { Title } = Typography;
const { Dragger } = Upload;
const { TextArea } = Input;

const InputPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const template = location.state?.template || "通用";
  const [form] = Form.useForm();
  const [contextText, setContextText] = useState("");
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [parsing, setParsing] = useState(false);

  const onFinish = (values: any) => {
    const formattedValues = {
        ...values,
        time: values.time ? dayjs(values.time).format('YYYY-MM-DD HH:mm') : '',
    };
    
    navigate('/edit', { 
        state: { 
            template, 
            data: formattedValues,
            contextText 
        } 
    });
  };

  const uploadProps = {
    name: 'file',
    multiple: false,
    action: 'http://localhost:8000/parse',
    onChange(info: any) {
      const { status } = info.file;
      if (status === 'uploading') {
        setParsing(true);
      }
      if (status === 'done') {
        message.success(`${info.file.name} 解析成功`);
        setParsing(false);
        // Append parsed text
        if (info.file.response && info.file.response.content) {
             setContextText(prev => prev + "\n" + info.file.response.content);
        }
      } else if (status === 'error') {
        message.error(`${info.file.name} 解析失败`);
        setParsing(false);
      }
    },
    showUploadList: true,
  };

  return (
    <div>
      <Button icon={<ArrowLeftOutlined />} onClick={() => navigate(-1)} style={{ marginBottom: 20 }}>返回</Button>
      <Title level={3}>填写要素 - {template}</Title>
      
      <div style={{ display: 'flex', gap: 24, flexDirection: 'row' }}>
        <Card title="关键要素" style={{ flex: 1 }}>
            <Form form={form} layout="vertical" onFinish={onFinish}>
                <Form.Item name="topic" label="主题/标题" rules={[{ required: true }]}>
                    <Input placeholder="例如：2024年度总结大会" />
                </Form.Item>
                <Form.Item name="time" label="时间" rules={[{ required: true }]}>
                    <DatePicker showTime style={{ width: '100%' }} />
                </Form.Item>
                <Form.Item name="location" label="地点" rules={[{ required: true }]}>
                    <Input placeholder="例如：公司大会议室" />
                </Form.Item>
                <Form.Item name="people" label="关键人物" rules={[{ required: true }]}>
                    <Input placeholder="例如：张总、李经理" />
                </Form.Item>
                <Form.Item name="content" label="核心内容摘要">
                    <TextArea rows={4} placeholder="简要描述活动流程或核心讲话内容..." />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit" block size="large">
                        开始生成
                    </Button>
                </Form.Item>
            </Form>
        </Card>

        <Card title="参考素材 (支持 Word, PPT, PDF)" style={{ flex: 1 }}>
            <Dragger {...uploadProps} style={{ padding: 20 }}>
                <p className="ant-upload-drag-icon">
                    <InboxOutlined />
                </p>
                <p className="ant-upload-text">点击或拖拽文件到此区域上传</p>
                <p className="ant-upload-hint">
                    系统将自动提取文本作为生成参考
                </p>
            </Dragger>
            <div style={{ marginTop: 20 }}>
                <Typography.Text strong>已提取的上下文预览：</Typography.Text>
                <TextArea 
                    rows={10} 
                    value={contextText} 
                    onChange={e => setContextText(e.target.value)} 
                    placeholder="解析后的文本将显示在这里，您也可以手动粘贴补充..."
                    style={{ marginTop: 10 }}
                />
            </div>
        </Card>
      </div>
    </div>
  );
};

export default InputPage;
