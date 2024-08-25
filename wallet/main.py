from click import group
from .models import db
from .models.transactions import Transactions
from .helpers.prompts import AmountPrompt, DescriptionPrompt, Prompt


@group
def main():
    try:
        db.create_tables([Transactions])
    except Exception as e:
        SystemExit("Creating database tables failed\n", e)


@main.command
def add():
    new_transaction = {
        "amount": AmountPrompt.ask("Insert amount"),
        "description": DescriptionPrompt.ask("Insert description", default=None),
        "t_type": Prompt.ask(
            "Insert transaction type",
            choices=['deposit', 'withdraw'],
            default='withdraw',
        )
    }

    try:
        Transactions.insert(**new_transaction).execute()
        print("Transaction created successfully")
    except Exception as e:
        SystemExit("Failed to add new transaction\n", e)


@main.command
def list(): ...


if __name__ == "__main__":
    main()
