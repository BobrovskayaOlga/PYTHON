import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("привет", "Привет."),
        ("Здравствуй", "Здравствуй."),
        ("привет мир", "Привет мир."),
    ],
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
