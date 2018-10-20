class switch(object):
    def __init__(self, object_to_switch_on):
        self.object_to_switch_on = object_to_switch_on
        self.default_result = None
        self.result_store = None
        self.cases = {}
        self.evaluated = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _ = self.result

    def __call__(self, when, then):
        if when in self.cases:
            raise ValueError("This case already exists")
        else:
            self.cases[when] = then
        return self

    def default(self, then):
        self.default_result = then
        return self

    @property
    def result(self):
        if not self.evaluated:
            self.result_store = self.__evaluate__()
        return self.result_store

    def __evaluate__(self):
        from inspect import signature
        self.evaluated = True
        result_tmp = None
        if all(callable(x) for x in self.cases.keys()):
            for case_fn, case_result in self.cases.items():
                no_of_params = len(signature(case_fn).parameters)
                if no_of_params >= 2:
                    raise ValueError("Case function must have either 0 or 1 arguments")

                if no_of_params == 1 and case_fn(self.object_to_switch_on):
                    result_tmp = case_result
                    break
                elif no_of_params == 0 and case_fn():
                    result_tmp = case_result
                    break
            else:
                result_tmp = self.default_result
        elif all(not callable(x) for x in self.cases.keys()):
            result_tmp = self.cases[self.object_to_switch_on] if self.object_to_switch_on in self.cases else self.default_result
        else:
            raise ValueError("Inconsistent switch usage, use either simple objects or functions")
        if result_tmp is not None and callable(result_tmp):
            return result_tmp()
        else:
            return result_tmp


var = 2
with switch(var) as case:
    case(1, "x")
    case(2, "yolo")
    case(3, "foo")
    case.default("dunno")
    result = case.result
print(result)

x = "yolo"
with switch(x) as case:
    case("lol", lambda: print(":D"))
    case("rotfl", lambda: print("<rotfl>"))
    case("yolo", lambda: print("Only once you live"))
    case.result

y = object()
with switch(y) as case:
    case(lambda: isinstance(y, str), "Some characters")
    case(lambda: isinstance(y, int), "Numberzzzz")
    case(lambda: isinstance(y, float), "Why u not double?")
    case.default(r"¯\_(ツ)_/¯")
    result = case.result
print(result)