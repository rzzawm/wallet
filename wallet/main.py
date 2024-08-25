from click import group
from rich.console import Console
from .models import db
from .models.transactions import Transactions
from .helpers.prompts import AmountPrompt, DescriptionPrompt, Prompt, IDPrompt, Confirm
from .helpers.tables import transactions_table

console = Console()


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
def list():
    try:
        all_transactions = Transactions.select().order_by(Transactions.created_at.desc())
    except Exception as e:
        SystemExit("Failed to fetch transactions\n", e)

    table = transactions_table(all_transactions)
    console.print(table)


@main.command
def delete():
    try:
        all_transactions = Transactions.select().order_by(Transactions.created_at.desc())
    except Exception as e:
        SystemExit("Failed to fetch transactions\n", e)

    table = transactions_table(all_transactions)
    console.print(table)
    while True:
        idx_to_delete = IDPrompt.ask("Insert ID of transaction to delete")
        confirmed = Confirm.ask("Are you sure?")
        if confirmed:
            break

    id_to_delete = all_transactions[idx_to_delete - 1]
    try:
        Transactions.get_by_id(id_to_delete).delete_instance()
        print("Transaction deleted successfully!")
    except Exception as e:
        SystemExit("Failed to delete transaction\n", e)


if __name__ == "__main__":
    main()
