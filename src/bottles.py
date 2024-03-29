from typing import Optional, Protocol


class Verse(Protocol):
    @staticmethod
    def lyrics(number: int) -> str: ...


class Bottleverse:

    @staticmethod
    def lyrics(number: int) -> str:
        lyric: str = (
            Bottleverse.create_line_one(number) +
            Bottleverse.create_line_two(number) +
            Bottleverse.create_line_three(number-1)
        )
        return lyric

    @staticmethod
    def create_line_one(number) -> str:
        match number:
            case 6: line = '1 six-pack of beer on the wall, 1 six-pack of beer.\n'
            case 1: line = '1 bottle of beer on the wall, 1 bottle of beer.\n'
            case 0: line = 'No more bottles of beer on the wall, no more bottles of beer.\n'
            case _: line = f'{number} bottles of beer on the wall, {number} bottles of beer.\n'
        return line

    @staticmethod
    def create_line_two(number) -> str:
        line: str
        match number:
            case 0: line = 'Go to the store and buy some more, '
            case 1: line = 'Take it down and pass it around, '
            case _: line = 'Take one down and pass it around, '
        return line

    @staticmethod
    def create_line_three(number) -> str:
        line: str
        match number:
            case 6:
                line = '1 six-pack of beer on the wall.\n'
            case 1:
                line = '1 bottle of beer on the wall.\n'
            case 0:
                line = 'no more bottles of beer on the wall.\n'
            case -1:
                line = '99 bottles of beer on the wall.\n'
            case _:
                line = f'{number} bottles of beer on the wall.\n'
        return line


class CountDownSong:
    def __init__(
        self,
        verse: Verse,
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
