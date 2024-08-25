from rich.table import Table
from rich.box import SQUARE


def transactions_table(transactions):
    table = Table(box=SQUARE)
    table.add_column("ID")
    table.add_column("Type")
    table.add_column("Description")
    table.add_column("Amount")
    table.add_column("Created at")

    for idx, transaction in enumerate(transactions, start=1):
        is_deposit = transaction.t_type == "deposit"

        table.add_row(
            f"{idx}",
            transaction.t_type,
            transaction.description or "[dim]no description[/]",
            f"{transaction.amount}$",
            f"[yellow]{transaction.created_at}[/]",
            style="green" if is_deposit else "red"
        )

    return table
