from config import ENV

value = ENV["VALUE"]
print(f"Input value: {value=}")
try:
    value_int = int(value)
    print(f"Result: {value!r} converted to int {value_int}")
except Exception:
    print(f"Result: Cannot convert {value!r} to int")
