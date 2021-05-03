from pyfilter import TextFilter


def basic_filtering_example():

    available_breeds = {'siamese', 'bengal', 'persian'}
    required_attributes = {'brown', 'friendly', 'healthy'}
    deal_breakers = {'unvaccinated'}

    cat_filter = TextFilter.new_filter(
        any_inclusion_keywords=available_breeds,
        all_inclusion_keywords=required_attributes,
        exclusion_keywords=deal_breakers
    )
    # In short, we want a cat which is one of 'siamese', 'bengal' or 'persian'
    # It should be brown and friendly and healthy.
    # It should NOT be unvaccinated.

    cats_in_shelter = [
        "brown siamese cat. It's friendly and healthy.",  # This looks like something we want!
        "A lovely white persian cat. It's healthy, though unvaccinated.",
        # The above looks like something we don't want! Wrong colour, unvaccinated and not friendly
        "A healthy and friendly brown Sphynx kitty. Vaccinations are up to date!"  # Unfortunately, it's the wrong breed
    ]

    # The two ways we can run these cats through the filter:
    # One by one in a for-loop and see if they pass:
    passed_cats = []
    for cat in cats_in_shelter:
        # Note: If we wanted to distinguish upper from lower case, we would pass casefold as False in the filter method
        passed_filter = cat_filter.filter(cat)
        if passed_filter:
            passed_cats.append(cat)
        print(f'The cat: "{cat}" {"passes" if passed_filter else "does not pass"} the filter')
    assert passed_cats == cats_in_shelter[:1]  # We expect only the first cat to pass

    # The better way to handle such inputs, however, is like so:
    passed_cats = cat_filter.multi_filter(cats_in_shelter)
    assert passed_cats == cats_in_shelter[:1]


if __name__ == "__main__":
    basic_filtering_example()
