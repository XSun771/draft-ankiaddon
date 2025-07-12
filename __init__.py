from anki.cards import Card
from aqt import gui_hooks, mw

from .DraftWindow import DraftWindow

# 全局变量存储窗口实例
_draft_window = None


def get_draft_window():
    """获取或创建草稿窗口实例"""
    global _draft_window
    if _draft_window is None:
        _draft_window = DraftWindow()
    return _draft_window


def on_reviewer_did_show_question(card: Card):
    """当显示新卡片时触发"""
    window = get_draft_window()
    # 显示窗口并重置内容
    window.reset_content()


# 注册钩子
gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)
