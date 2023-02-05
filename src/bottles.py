from typing import Optional


class Bottleverse:

    @staticmethod
    def lyrics(number: int):
        lyric: str = (
            Bottleverse.create_line_one(number) +
            Bottleverse.create_line_two(number) +
            Bottleverse.create_line_three(number-1)
        )
        return lyric

    @staticmethod
    def create_line_one(number) -> str:
        if number == 6:
            return '1 six-pack of beer on the wall, 1 six-pack of beer.\n'
        elif number == 1:
            return '1 bottle of beer on the wall, 1 bottle of beer.\n'
        elif number == 0:
            return 'No more bottles of beer on the wall, no more bottles of beer.\n'
        return f'{number} bottles of beer on the wall, {number} bottles of beer.\n'

    @staticmethod
    def create_line_two(number) -> str:
        if number == 0:
            return 'Go to the store and buy some more, '
        elif number == 1:
            return 'Take it down and pass it around, '
        return 'Take one down and pass it around, '

    @staticmethod
    def create_line_three(number) -> str:
        if number == 6:
            return '1 six-pack of beer on the wall.\n'
        elif number == 1:
            return '1 bottle of beer on the wall.\n'
        elif number == 0:
            return 'no more bottles of beer on the wall.\n'
        elif number <= 0:
            return '99 bottles of beer on the wall.\n'
        return f'{number} bottles of beer on the wall.\n'


class CountDownSong:
    def __init__(
        self,
        verse: Bottleverse,
        high: Optional[int] = None,
        low: Optional[int] = None
    ):
        self.verse_generator = verse
        self.high = high
        self.low = low

    def verse(self, number: int):
        return self.verse_generator.lyrics(number=number)

    def verses(self, high: int, low: int):
        verse_collector: list[str] = []
        for number in reversed(range(low, high+1)):
            if number >= 0:
                verse_collector.append(self.verse_generator.lyrics(number=number))
            else:
                break
        return '\n'.join(verse_collector)

    def song(self):
        assert self.high and self.low
        return self.verses(high=self.high, low=self.low)
