class Video:
    def create(self, name):
        self.name = name
        return self.name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, *video):
        cls.videos = [i for i in video]

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1, v2 = [Video() for _ in '..']

v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1, v2)

[YouTube.play(i) for i in range(2)]
