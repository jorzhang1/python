class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__ogVolume = 0
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__ogVolume = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__ogVolume
                self.__ogVolume = 0
                self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__ogVolume
                self.__muted = False
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__ogVolume
                self.__muted = False
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1
            else:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
