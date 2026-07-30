#!/usr/bin/env python3
"""客服速查 - 手机访问服务器
Usage: python3 server.py
手机和电脑连同一个 WiFi，手机浏览器打开下面地址即可。
"""
import http.server, socket, os

PORT = 8765
os.chdir(os.path.dirname(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]

print(f'''
╔══════════════════════════════════════╗
║   客服速查 — 麦麦教研              ║
╠══════════════════════════════════════╝
║  电脑: 双击「客服速查.command」
║  手机: 浏览器打开下面地址
║
║  ▶ http://{ip}:{PORT}
║
║  打开后点浏览器「添加到主屏幕」
║  之后就像 App 一样直接点图标用
║  Ctrl+C 停止服务器
╚══════════════════════════════════════
''')

http.server.HTTPServer(('0.0.0.0', PORT), Handler).serve_forever()
