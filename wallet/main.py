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
        console.print("Creating database tables failed\n", e, style="red")
        SystemExit()


@main.command
def add():
    new_transaction = {
        "t_type": Prompt.ask(
            "[blue]What's the type of transaction[/]",
            choices=['deposit', 'withdraw'],
            default='withdraw',
        ),
        "amount": AmountPrompt.ask("[blue]Enter the transaction amount[/]"),
        "description": DescriptionPrompt.ask("[blue]Write a description for it if you want[/]", default=None),
    }

    try:
        Transactions.insert(**new_transaction).execute()
        console.print("Transaction created successfully", style="green")
    except Exception as e:
        console.print("Failed to add new transaction\n", e, style="red")


@main.command
def list():
    try:
        all_transactions = Transactions.select().order_by(Transactions.created_at.desc())
    except Exception as e:
        console.print("Failed to fetch transactions\n", e, style="red")
        return

    table = transactions_table(all_transactions)
    console.print(table)


@main.command
def delete():
    try:
        all_transactions = Transactions.select().order_by(Transactions.created_at.desc())
    except Exception as e:
        console.print("Failed to fetch transactions\n", e, style="red")
        return

    table = transactions_table(all_transactions)
    console.print(table)
    while True:
        idx_to_delete = IDPrompt.ask(
            "[blue]Insert ID of transaction to delete[/]")
        if idx_to_delete > len(all_transactions):
            console.print("ID not found", style="red")
            continue
        confirmed = Confirm.ask("[blue]Are you sure?[/]")
        if confirmed:
            break

    id_to_delete = all_transactions[idx_to_delete - 1]
    try:
        Transactions.get_by_id(id_to_delete).delete_instance()
        console.print("Transaction deleted successfully!", style="green")
    except Exception as e:
        console.print("Failed to delete transaction\n", e, style="red")


if __name__ == "__main__":
    main()
