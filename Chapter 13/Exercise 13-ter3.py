# Source: https://codepal.ai/code-generator/query/xmfZtOpn/python-audio-player-pyqt5-module-without-pygame
# Small adaptions

import os

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QSlider, QLabel


class AudioPlayer(QWidget):
    """
    A simple audio player that uses PyQt5 and QMediaPlayer to play audio files.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Player")
        self.setGeometry(100, 100, 500, 300)
        self.media_player = QMediaPlayer()
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.add_button = QPushButton("Add File")
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.add_button.clicked.connect(self.add_file)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(30)
        self.volume_slider.setTickPosition(QSlider.TicksBelow)
        self.volume_slider.setTickInterval(5)
        self.volume_slider.valueChanged.connect(self.value_change)

        self.volume_label = QLabel('', self)
        self.volume_label.setFont(QFont('Arial', 12))

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.add_button)

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.volume_slider)

        label_layout = QHBoxLayout()
        label_layout.addWidget(self.volume_label, alignment=Qt.AlignHCenter)

        layout = QVBoxLayout()
        layout.addLayout(slider_layout)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def play(self):
        """
        Plays the currently loaded media file.
        """
        self.media_player.play()

    def pause(self):
        """
        Pauses the currently playing media file.
        """
        self.media_player.pause()

    def stop(self):
        """
        Stops the currently playing media file.
        """
        self.media_player.stop()

    def value_change(self):
        volume = self.volume_slider.value()
        self.volume_label.setText(f'Current Value: {volume}')
        self.media_player.setVolume(volume)

    def add_file(self):
        """
        Opens a file dialog to select an audio file to load into the player.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", os.path.expanduser("~"),
                                                   "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.media_player.play()


if __name__ == "__main__":
    app = QApplication([])
    player = AudioPlayer()
    player.show()
    app.exec_()
