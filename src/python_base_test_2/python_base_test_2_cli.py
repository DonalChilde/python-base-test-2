"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Base Test 2."""


if __name__ == "__main__":
    main(prog_name="python-base-test-2")  # pragma: no cover