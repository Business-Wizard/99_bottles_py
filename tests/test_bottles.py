from src import bottles


class FakeVerse:
    @staticmethod
    def lyrics(number: int) -> str:
        return f'This is verse {number}.\n'


def test_fake_verse_has_lyrics():
    assert FakeVerse.lyrics


def test_bottle_verse_has_lyrics():
    assert bottles.Bottleverse.lyrics


def test_verse_single():
    expected: str = 'This is verse 500.\n'
    actual: str = bottles.CountDownSong(FakeVerse).verse(500)
    assert actual == expected


def test_verses_range():
    expected: str = (
        'This is verse 99.\n'
        '\n'
        'This is verse 98.\n'
        '\n'
        'This is verse 97.\n'
    )
    actual = bottles.CountDownSong(FakeVerse).verses(99, 97)  # type: ignore
    assert actual == expected


def test_song():
    expected: str = (
        'This is verse 47.\n'
        '\n'
        'This is verse 46.\n'
        '\n'
        'This is verse 45.\n'
        '\n'
        'This is verse 44.\n'
        '\n'
        'This is verse 43.\n'
    )
    actual = bottles.CountDownSong(FakeVerse, 47, 43).song()  # type: ignore
    assert actual == expected


def test_bottle_verse_upper_bound():
    expected: str = (
        '99 bottles of beer on the wall, '
        '99 bottles of beer.\n'
        'Take one down and pass it around, '
        '98 bottles of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(99)
    assert actual == expected


def test_bottle_verse_lower_bound():
    expected: str = (
        '3 bottles of beer on the wall, '
        '3 bottles of beer.\n'
        'Take one down and pass it around, '
        '2 bottles of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(3)
    assert actual == expected


def test_bottle_verse_verse_7():
    expected: str = (
        '7 bottles of beer on the wall, '
        '7 bottles of beer.\n'
        'Take one down and pass it around, '
        '1 six-pack of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(7)
    assert actual == expected


def test_bottle_verse_verse_6():
    expected: str = (
        '1 six-pack of beer on the wall, '
        '1 six-pack of beer.\n'
        'Take one down and pass it around, '
        '5 bottles of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(6)
    assert actual == expected


def test_bottle_verse_2():
    expected: str = (
        '2 bottles of beer on the wall, '
        '2 bottles of beer.\n'
        'Take one down and pass it around, '
        '1 bottle of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(2)
    assert actual == expected


def test_bottle_verse_1():
    expected: str = (
        '1 bottle of beer on the wall, '
        '1 bottle of beer.\n'
        'Take it down and pass it around, '
        'no more bottles of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(1)
    assert actual == expected


def test_bottle_verse_0():
    expected: str = (
        'No more bottles of beer on the wall, '
        'no more bottles of beer.\n'
        'Go to the store and buy some more, '
        '99 bottles of beer on the wall.\n'
    )
    actual: str = bottles.Bottleverse.lyrics(0)
    assert actual == expected
