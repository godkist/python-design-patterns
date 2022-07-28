

class Target:
    def request(self) -> str:
        return 'You only live once.'


class Source:
    def specific_request(self) -> str:
        return '.ecno evil ylno uoY'


class Adapter(Target):
    def __init__(self, source: Source) -> None:
        self.source = source

    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.source.specific_request()[::-1]}'


if __name__ == '__main__':
    print('--- with the Target')
    target = Target()
    print(target.request())

    print('--- with the Source')
    source = Source()
    print(source.specific_request())

    print('--- with the Adapter')
    adapter = Adapter(source)
    print(target.request())
