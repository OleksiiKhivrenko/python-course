# mus player
# громкость
# список песен
# текущая пеня
# методы
# сделать громче
# сделать тише
# следующий трек
# проигрывание
# паузна

class MusicPlayer:
    def __init__(self, music_list):
        self.__max_volume = 100
        self.__min_volume = 0
        self.volume = 30
        self.music_list = music_list
        self.current_track_index = 0
        self.__playing = False

    def get_volume(self):
        print("Current volume: ", self.volume)

    def make_louder(self):
        if self.volume < self.__max_volume:
            self.volume += 10
        self.get_volume()

    def make_quieter(self):
        if self.volume > self.__min_volume:
            self.volume -= 10
        self.get_volume()

    def get_track(self):
        print("Current track is", self.music_list[self.current_track_index])

    def next_track(self):
        if len(self.music_list) > 0 and self.current_track_index + 1 < len(self.music_list):
            print(self.current_track_index, self.music_list)
            self.current_track_index += 1
        self.get_track()

    def prev_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
        self.get_track()

    def check_player_playing(self):
        status_text = "is" if self.__playing else "is not"
        print(f"Player {status_text} playing now.")

    def play(self):
        self.__playing = True
        print(f"{self.music_list[self.current_track_index]} is playing.")

    def pause(self):
        self.__playing = False
        print(f"{self.music_list[self.current_track_index]} paused.")


player = MusicPlayer(["song 1", "song 2", "song 3", "song 4"])

player.get_track()
player.next_track()
player.next_track()
player.next_track()
player.next_track()
player.next_track()
player.prev_track()
player.prev_track()
player.prev_track()
player.prev_track()
player.prev_track()
player.make_quieter()
player.make_quieter()
player.make_quieter()
player.make_quieter()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.make_louder()
player.check_player_playing()
player.play()
player.check_player_playing()

