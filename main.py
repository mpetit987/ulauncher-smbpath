from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import smbpath


class SmbPathExtension(Extension):

    def __init__(self):
        super(SmbPathExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        arg = event.get_argument()
        if arg is None:
            return RenderResultListAction([ExtensionResultItem(icon='images/icon.png', name='Enter linux/windows samba path')])

        path = smbpath.convert_path(event.get_argument())
        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=path,
                                                           description='press alt+1 to copy this string to clipboard',
                                                           on_enter=CopyToClipboardAction(path))])


if __name__ == '__main__':
    SmbPathExtension().run()
