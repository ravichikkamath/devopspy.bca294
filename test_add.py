from add import addition

def test_pos():
    assert addition (10,20) == 40

def test_zero():
    assert addition (10,0) == 10

def test_neg():
    assert addition (-50,10) == 40

