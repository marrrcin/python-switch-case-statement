from switch import switch


def test_can_switch_on_int():
    with switch(666) as case:
        case(1, "one")
        case(2, "two")
        case(666, "number of the beast")
        result = case.result

    assert result == "number of the beast"


def test_can_switch_on_string():
    with switch("yolo") as case:
        case("aosdk", 1)
        case("askdoska", 2)
        case("asodaodki", 3)
        case("yolo", 666)
        case("asdksoa", 4)
        assert case.result == 666


def test_can_use_lambdas_as_then():
    result = []
    with switch("yolo") as case:
        case("x", lambda: result.append("x"))
        case("yolo", lambda: result.append("yolo"))
    assert len(result) == 1 and result[0] == "yolo"


def test_can_use_lambdas_as_when():
    SHRUG = r"¯\_(ツ)_/¯"
    y = object()
    with switch(y) as case:
        case(lambda: isinstance(y, str), "Some characters")
        case(lambda: isinstance(y, int), "Numberzzzz")
        case(lambda: isinstance(y, float), "Why u not double?")
        case.default(SHRUG)
        assert case.result == SHRUG


def test_can_use_functions_as_when():
    def one(x):
        one.called = True
        return x == 1

    def two(x):
        two.called = True
        return x == 2

    with switch(2) as case:
        case(one, 10)
        case(two, 20)
        assert case.result == 20 and two.called


def test_can_use_lambdas_in_both_when_and_then():
    def raise_():
        raise_.called = True
        raise ValueError
    raise_.called = False

    with switch(666) as case:
        case(lambda x: x % 777 == 0, lambda: 777)
        case(lambda: False, raise_)
        case(lambda x: x == 666, lambda: "YEAH!")
        assert case.result == "YEAH!" and raise_.called is False

