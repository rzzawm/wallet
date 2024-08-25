from click import group
from .models import db
from .models.transactions import Transactions


@group
def main():
    try:
        db.create_tables([Transactions])
    except Exception as e:
        SystemExit("Creating database tables failed\n", e)


@main.command
def add(): ...


@main.command
def list(): ...


if __name__ == "__main__":
    main()
