import webview
from .util import run_test


def test_frameless():
    window = webview.create_window('Frameless test', 'https://www.example.org', frameless=True, preserve_controls=True)
    run_test(webview, window)


