class Television:
    """
    A class representing a Television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        A method that sets the default values of a TV
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__ogVolume: int = 0
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        A method that turns the TV on or off
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        A method that mutes or unmutes the TV
        """
        if self.__status:
            if not self.__muted:
                self.__ogVolume = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__ogVolume
                self.__ogVolume = 0
                self.__muted = False

    def channel_up(self) -> None:
        """
        A method that changes the channel going up
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        A method that changes the channel going down
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        A method that increases the volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__ogVolume
                self.__muted = False
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self) -> None:
        """
        A method that decreases the volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__ogVolume
                self.__muted = False
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1
            else:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self) -> str:
        """
        A method that prints information about the TV
        :return: A string with information
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
