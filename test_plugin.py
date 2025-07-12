#!/usr/bin/env python3
"""
测试脚本 - 用于验证 Draft Window 插件的基本功能
"""

import sys
from PyQt6.QtWidgets import QApplication
from DraftWindow import DraftWindow


def test_draft_window():
    """测试草稿窗口的基本功能"""
    app = QApplication(sys.argv)
    
    # 创建窗口实例
    window = DraftWindow()
    
    # 测试显示窗口
    print("测试显示窗口...")
    window.show_window()
    
    # 测试重置内容
    print("测试重置内容...")
    window.reset_content()
    
    # 测试保持内容
    print("测试保持内容...")
    window.keep_content()
    
    print("测试完成！窗口应该已经显示。")
    print("请在窗口中输入一些文本，然后关闭窗口。")
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    test_draft_window() 