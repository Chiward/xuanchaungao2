"""
范文加载功能测试脚本
测试 examples 文件夹中的范文是否能够正确加载
"""
import os
import sys

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from service.example_loader import load_example, get_all_examples

def test_load_single_example():
    """测试加载单个范文"""
    print("=" * 60)
    print("测试 1: 加载单个范文")
    print("=" * 60)
    
    template_types = ["重要会议", "培训活动", "领导带队检查", "项目中标", "项目重大进展", "科技创新"]
    
    for template_type in template_types:
        print(f"\n加载 '{template_type}' 范文...")
        content = load_example(template_type)
        
        if content:
            preview = content[:200] if len(content) > 200 else content
            print(f"✓ 成功加载")
            print(f"  预览: {preview}...")
            print(f"  总长度: {len(content)} 字符")
        else:
            print(f"✗ 加载失败或未找到范文")
    
    print("\n")

def test_load_all_examples():
    """测试加载所有范文"""
    print("=" * 60)
    print("测试 2: 加载所有范文")
    print("=" * 60)
    
    examples = get_all_examples()
    
    print(f"\n找到 {len(examples)} 个范文:")
    for template_type, content in examples.items():
        print(f"  - {template_type}: {len(content)} 字符")
    
    if len(examples) == 6:
        print("\n✓ 所有范文加载成功")
    else:
        print(f"\n⚠️  预期 6 个范文，实际找到 {len(examples)} 个")
    
    print("\n")

def test_example_content():
    """测试范文内容质量"""
    print("=" * 60)
    print("测试 3: 范文内容质量检查")
    print("=" * 60)
    
    examples = get_all_examples()
    
    for template_type, content in examples.items():
        print(f"\n'{template_type}' 范文分析:")
        
        # 检查内容长度
        if len(content) < 100:
            print(f"  ⚠️  内容过短 ({len(content)} 字符)")
        else:
            print(f"  ✓ 内容长度适中 ({len(content)} 字符)")
        
        # 检查段落结构
        paragraphs = content.split('\n')
        non_empty_paragraphs = [p for p in paragraphs if p.strip()]
        print(f"  ✓ 段落数量: {len(non_empty_paragraphs)}")
        
        # 检查关键词
        keywords = {
            "重要会议": ["会议", "学习", "精神", "部署"],
            "培训活动": ["培训", "学习", "提升", "课程"],
            "领导带队检查": ["检查", "督导", "现场", "整改"],
            "项目中标": ["中标", "项目", "合同", "签约"],
            "项目重大进展": ["进展", "完成", "交付", "通过"],
            "科技创新": ["技术", "创新", "研发", "突破"]
        }
        
        if template_type in keywords:
            found_keywords = [kw for kw in keywords[template_type] if kw in content]
            print(f"  ✓ 关键词: {', '.join(found_keywords)}")
    
    print("\n")

def main():
    """主测试函数"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "范文加载功能测试" + " " * 15 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    # 运行所有测试
    test_load_single_example()
    test_load_all_examples()
    test_example_content()
    
    print("=" * 60)
    print("测试完成")
    print("=" * 60)
    print("\n")

if __name__ == "__main__":
    main()
