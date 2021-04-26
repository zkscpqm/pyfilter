from pyfilter.core import TextFilter


def test_matched_any_single_inclusion_filters():
    single_inclusion_filters = {'dog', 'cat'}
    cases = [
        ('some_string_with_dog', True),
        ('string without those keywords', False),
        ('do g', False),
    ]
    text_filter = TextFilter.new_filter(single_inclusion_filters=single_inclusion_filters)
    for input_string, expected in cases:
        assert text_filter.filter(input_string) is expected


def test_matched_all_multi_inclusion_filters():
    multi_inclusion_filters = {'dog', 'cat'}
    cases = [
        ('some_string_with_dog', False),
        ('string without those keywords', False),
        ('dogs and cats are cool', True),
    ]
    text_filter = TextFilter.new_filter(multi_inclusion_filters=multi_inclusion_filters)
    for input_string, expected in cases:
        assert text_filter.filter(input_string) is expected


def test_matched_no_exclusion_filters():
    exclusion_filters = {'dog', 'cat'}
    cases = [
        ('some_string_with_dog', False),
        ('string without those keywords', True),
        ('are you a cat', False)
    ]
    text_filter = TextFilter.new_filter(exclusion_filters=exclusion_filters)
    for input_string, expected in cases:
        assert text_filter.filter(input_string) is expected


def test_all_inputs_pass_empty_filter():
    cases = ['some_string_with_dog', 'string without those keywords', 'are you a cat', '', '   ']
    text_filter = TextFilter.new_filter()
    for input_string in cases:
        assert text_filter.filter(input_string) is True
