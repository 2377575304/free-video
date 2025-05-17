import sys
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel,
    QHBoxLayout, QComboBox
)

class VideoParser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("视频网站视频解析播放")
        self.setGeometry(400, 200, 600, 250)
        layout = QVBoxLayout()

        # 视频名称搜索部分
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("输入视频名称进行搜索")
        search_layout.addWidget(self.search_input)
        self.search_button = QPushButton("搜索")
        self.search_button.clicked.connect(self.search_video)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.search_label = QLabel("")
        layout.addWidget(self.search_label)

        # 解析接口选择部分
        api_layout = QHBoxLayout()
        api_label = QLabel("选择解析接口：")
        api_layout.addWidget(api_label)
        self.api_combo = QComboBox()
        # 推荐一些当前较为常用且响应较快的免费解析接口（仅供学习测试）
        self.api_list = [
            "https://jx.playerjy.com/?url=",
            "https://jx.jsonplayer.com/player/?url=",
            "https://www.ckplayer.vip/jiexi/?url=",
            "https://jx.m3u8.tv/jiexi/?url=",
            "https://vip.bljiex.com/?v=",
            "https://jx.xmflv.com/?url=",
            "https://jx.618g.com/?url=",
            "https://jx.yparse.com/index.php?url=",
            "https://jx.parwix.com:4433/player/?url=",
            "https://www.8090g.cn/jiexi/?url=",
            "https://jx.ergan.top/?url=",
            "https://jx.52xq.vip/?url=",
            "https://jx.777jiexi.com/player/?url=",
            "https://jx.000180.top/jx/?url=",
            "https://jx.2ok.com.cn/player/?url=",
        ]
        self.api_combo.addItems(self.api_list)
        api_layout.addWidget(self.api_combo)
        layout.addLayout(api_layout)

        # 视频链接解析部分
        self.label = QLabel("请输入视频网站视频链接：")
        layout.addWidget(self.label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.parse_button = QPushButton("解析并播放")
        self.parse_button.clicked.connect(self.parse_video)
        layout.addWidget(self.parse_button)

        self.setLayout(layout)

    def search_video(self):
        video_name = self.search_input.text().strip()
        if not video_name:
            self.search_label.setText("请输入视频名称！")
            return
        # 跳转到爱奇艺和腾讯视频的搜索页面（分别打开两个标签页）
        iqiyi_url = f"https://so.iqiyi.com/so/q_{video_name}"
        tencent_url = f"https://v.qq.com/x/search/?q={video_name}"
        webbrowser.open(iqiyi_url)
        webbrowser.open(tencent_url)
        self.search_label.setText("正在用浏览器打开爱奇艺和腾讯视频搜索结果...")

    def parse_video(self):
        video_url = self.url_input.text().strip()
        if not video_url:
            self.label.setText("请输入有效的视频链接！")
            return

        # 获取当前选择的解析接口
        parse_api = self.api_combo.currentText()
        full_url = parse_api + video_url
        webbrowser.open(full_url)
        self.label.setText("正在用浏览器打开解析页面...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoParser()
    window.show()
    sys.exit(app.exec_())