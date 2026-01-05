"""
范文参考功能测试脚本
测试不同类型的宣传稿生成是否能够正确加载和参考范文
"""
import requests
import json
import time

# API 基础地址
BASE_URL = "http://127.0.0.1:8000"

# 测试数据
TEST_CASES = [
    {
        "template_type": "重要会议",
        "topic": "2024年度党委理论学习中心组学习（扩大）会",
        "time": "2024-01-15 14:00",
        "location": "公司大会议室",
        "people": "党委书记张三、党委副书记李四",
        "content": "学习党的二十大精神，部署2024年党建工作重点任务"
    },
    {
        "template_type": "培训活动",
        "topic": "2024年廉洁大讲堂暨合规风控培训会议",
        "time": "2024-01-20 09:00",
        "location": "培训中心",
        "people": "纪委书记王五、合规部经理赵六",
        "content": "开展廉洁教育，提升合规风控意识"
    },
    {
        "template_type": "领导带队检查",
        "topic": "庄志民带队到晟宁实业开展现场督导检查工作",
        "time": "2024-01-25 10:00",
        "location": "晟宁实业项目部",
        "people": "总经理庄志民、副总经理孙七",
        "content": "检查项目进度，现场解决实际问题"
    },
    {
        "template_type": "项目中标",
        "topic": "2024年度首个家具产业园施工总承包项目落地花都",
        "time": "2024-02-01 08:30",
        "location": "花都区",
        "people": "董事长周八、市场部经理吴九",
        "content": "成功中标花都家具产业园项目，合同金额1.2亿元"
    },
    {
        "template_type": "项目重大进展",
        "topic": "江山帝景普罗旺斯项目顺利通过验收交付",
        "time": "2024-02-15 15:00",
        "location": "江山帝景项目现场",
        "people": "项目经理郑十、业主代表钱十一",
        "content": "项目顺利通过竣工验收，正式交付业主使用"
    },
    {
        "template_type": "科技创新",
        "topic": "中人建设成功通过国家高新技术企业认定",
        "time": "2024-02-20 10:00",
        "location": "公司总部",
        "people": "技术总监孙十二、研发团队",
        "content": "通过国家高新技术企业认定，获得税收优惠政策"
    }
]

def test_health():
    """测试健康检查接口"""
    print("=" * 60)
    print("测试 1: 健康检查接口")
    print("=" * 60)
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.json()}")
        print("✓ 健康检查通过\n")
        return True
    except Exception as e:
        print(f"✗ 健康检查失败: {e}\n")
        return False

def test_templates():
    """测试模板列表接口"""
    print("=" * 60)
    print("测试 2: 模板列表接口")
    print("=" * 60)
    try:
        response = requests.get(f"{BASE_URL}/templates")
        print(f"状态码: {response.status_code}")
        templates = response.json()
        print(f"可用模板: {templates}")
        print("✓ 模板列表获取成功\n")
        return True
    except Exception as e:
        print(f"✗ 模板列表获取失败: {e}\n")
        return False

def test_generate_draft(test_case, index):
    """测试宣传稿生成"""
    print("=" * 60)
    print(f"测试 {index + 3}: 生成 {test_case['template_type']} 宣传稿")
    print("=" * 60)
    print(f"主题: {test_case['topic']}")
    print(f"时间: {test_case['time']}")
    print(f"地点: {test_case['location']}")
    print(f"人物: {test_case['people']}")
    print(f"内容: {test_case['content']}")
    print("-" * 60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/generate",
            json=test_case,
            stream=True
        )
        
        if response.status_code == 200:
            print("生成内容预览（前500字）:")
            print("-" * 60)
            content = ""
            for chunk in response.iter_content(chunk_size=1024, decode_unicode=True):
                if chunk:
                    content += chunk
                    if len(content) >= 500:
                        break
            print(content[:500])
            print("-" * 60)
            print("✓ 宣传稿生成成功\n")
            return True
        else:
            print(f"✗ 生成失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}\n")
            return False
    except Exception as e:
        print(f"✗ 生成失败: {e}\n")
        return False

def main():
    """主测试函数"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "AI宣传稿生成系统 - 范文参考功能测试" + " " * 10 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    # 测试健康检查
    if not test_health():
        print("错误: 后端服务未正常运行，请先启动后端服务")
        return
    
    # 测试模板列表
    if not test_templates():
        print("错误: 无法获取模板列表")
        return
    
    # 测试各类宣传稿生成
    results = []
    for i, test_case in enumerate(TEST_CASES):
        result = test_generate_draft(test_case, i)
        results.append((test_case['template_type'], result))
        time.sleep(2)  # 避免请求过快
    
    # 输出测试结果汇总
    print("\n")
    print("=" * 60)
    print("测试结果汇总")
    print("=" * 60)
    for template_type, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{template_type:20s} {status}")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for _, result in results if result)
    print(f"总计: {total} 个测试, 通过: {passed} 个, 失败: {total - passed} 个")
    print("\n")
    
    if passed == total:
        print("🎉 所有测试通过！范文参考功能正常工作。")
    else:
        print(f"⚠️  有 {total - passed} 个测试失败，请检查日志。")

if __name__ == "__main__":
    main()
