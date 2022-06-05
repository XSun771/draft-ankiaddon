from anki.cards import Card
from aqt import gui_hooks, mw

from .DraftWindow import DraftWindow


def myfunc(card: Card):
    if not hasattr(mw, 'myWidget'):
        mw.myWidget = DraftWindow(card)

    mw.myWidget.clearAndShow()


gui_hooks.reviewer_did_show_question.append(myfunc)
