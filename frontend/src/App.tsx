import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Input from './pages/Input';
import Edit from './pages/Edit';
import { Layout } from 'antd';
import './App.css';

const { Header, Content } = Layout;

function App() {
  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        <Header style={{ color: 'white', fontSize: '20px', fontWeight: 'bold' }}>
          智能宣传稿生成助手
        </Header>
        <Content style={{ padding: '24px' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/input" element={<Input />} />
            <Route path="/edit" element={<Edit />} />
          </Routes>
        </Content>
      </Layout>
    </Router>
  );
}

export default App;
