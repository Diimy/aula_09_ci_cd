import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14


def test_sums():
    val1 = 1
    val2 = 3

    output = methods.sums(val1, val2)
    assert output == 4
    
def test_sub():
    val1 = 7
    val2 = 6

    output = methods.sub(val1, val2)
    assert output == 1

def test_divs():
    val1 = 4
    val2 = 2

    output = methods.divs(val1, val2)
    assert output == 2

def test_multp():
    val1 = 2
    val2 = 3

    output = methods.multp(val1, val2)
    assert output == 6