from transport import TextFilterClient


def _wait_enter():
    input("Press 'Enter' to exit...")
    exit(0)


def main():
    client = TextFilterClient.new(insecure_port=8886)
    resp = client.filter("brown siamese cat. It's friendly and healthy.", casefold=False)
    print(resp)


if __name__ == "__main__":
    main()
    _wait_enter()
