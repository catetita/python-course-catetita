
dictionary = {key: value for key, value in zip(range(0, 9), "find the bug")}
assert len(dictionary) == 9


dictionario = {"a": 0, "b": 1, "c": 2}
assert "b" in dictionario


string_original = "abcdefg"
string_modified = "".join([ b.upper()if a % 2 else  b.lower() for a,b in enumerate (string_original)])
assert string_modified == "aBcDeFg"
