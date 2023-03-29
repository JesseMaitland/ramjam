from ramjam.cli import Command


class StubCommand(Command):
    def __call__(self) -> None:
        pass
