from twtter import shorten

def test_shorties():
    assert shorten("digger") == "dggr"
    assert shorten("rigger") == "rggr"
    assert shorten("bigger") == "bggr"
    assert shorten("baller") == "bllr"
    assert shorten("trigger") == "trggr"
    assert shorten("aaaaaaaaaa") == ""
    assert shorten("t") == "t"
    assert shorten("ayo") == "y"
    assert shorten("12") == "12"
    assert shorten(" ") == " "      

test_shorties()                                                                                                                                                                                  