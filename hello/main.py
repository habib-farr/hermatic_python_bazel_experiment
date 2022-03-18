import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
def cli(count):

    print("Hello world " * count)


if __name__ == "__main__":
    cli()
