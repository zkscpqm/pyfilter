from pyfilter import get_new_client


def _wait_enter():
    input("Press 'Enter' to exit...")
    exit(0)


def main():
    cats_in_shelter = [
        "brown siamese cat. It's friendly and healthy.",  # This looks like something we want!
        "A lovely white persian cat. It's healthy, though unvaccinated.",
        # The above looks like something we don't want! Wrong colour, unvaccinated and not friendly
        "A healthy and friendly brown Sphynx kitty. Vaccinations are up to date!"  # Unfortunately, it's the wrong breed
    ]

    # Using our simple object factory API to start up a new client and connect it to the same port as the server
    client = get_new_client(insecure_port=8886, quiet=False)

    # Unary->Unary (single) filter. We are using the first value so we expect it to pass
    resp = client.filter(cats_in_shelter[0], casefold=False)
    print('Unary->Unary response: ', resp)
    assert resp is True

    # Stream->Unary (multi) filter. We expect back a list of all passing strings (aka only the first)
    resp = client.multi_filter(cats_in_shelter, casefold=False)
    print('Stream->Unary response: ', resp)
    assert resp == cats_in_shelter[:1]

    # Stream->Stream (multi) filter. We stream strings to the server and expect a stream of bools (passed/filtered out)
    i = 0
    for resp in client.multi_filter_stream(cats_in_shelter, casefold=False):
        print(f'Stream->Unary for request: {cats_in_shelter[i]} we got response: ', resp)
        i += 1


if __name__ == "__main__":
    main()
    _wait_enter()
