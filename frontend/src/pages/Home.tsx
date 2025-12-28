import React, { useEffect, useState } from 'react';
import { Card, Row, Col, Typography, message } from 'antd';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const { Title } = Typography;

const Home: React.FC = () => {
  const navigate = useNavigate();
  const [templates, setTemplates] = useState<string[]>([]);

  useEffect(() => {
    // Fetch templates from backend
    axios.get('http://localhost:8000/templates')
      .then(res => setTemplates(res.data))
      .catch(err => {
        console.error(err);
        // Fallback
        setTemplates(["重要会议", "培训活动", "领导带队检查", "项目中标", "项目重大进展", "科技创新"]);
      });
  }, []);

  const handleSelect = (template: string) => {
    navigate('/input', { state: { template } });
  };

  return (
    <div>
      <Title level={2} style={{ textAlign: 'center', marginBottom: 40 }}>请选择写作场景</Title>
      <Row gutter={[24, 24]}>
        {templates.map(t => (
          <Col span={8} key={t}>
            <Card 
              hoverable 
              onClick={() => handleSelect(t)}
              style={{ textAlign: 'center', height: 150, display: 'flex', alignItems: 'center', justifyContent: 'center' }}
            >
              <Title level={4}>{t}</Title>
            </Card>
          </Col>
        ))}
        <Col span={8}>
           <Card 
              hoverable 
              style={{ textAlign: 'center', height: 150, display: 'flex', alignItems: 'center', justifyContent: 'center', border: '2px dashed #d9d9d9' }}
              onClick={() => message.info("自定义模板功能开发中")}
            >
              <Title level={4} type="secondary">+ 新增场景</Title>
            </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Home;
