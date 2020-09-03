# Frameless window

Create a frameless window. The window can be moved around by dragging any point.

``` python
import webview


if __name__ == '__main__':
    webview.create_window('Frameless window',
                          'http://pywebview.flowrl.com/hello',
                          frameless=True)
    webview.start()
```

## Preserving window controls on MacOS
The standard window controls (maximize, minimize, close) can be preserved on frameless windows in MacOS

``` python
import webview


if __name__ == '__main__':
    webview.create_window('Frameless window',
                          'http://pywebview.flowrl.com/hello',
                          frameless=True, preserve_controls=True)
    webview.start()
```