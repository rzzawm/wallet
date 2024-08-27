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


def summary_table(deposits, withdrawals):
    table = Table(box=SQUARE, row_styles=['green', 'red', 'yellow bold'])
    table.add_column("")
    table.add_column("Total")
    table.add_column("Count")

    total_sum = deposits.sum or 0 - withdrawals.sum or 0
    total_count = deposits.count or 0 + withdrawals.count or 0

    table.add_row(
        "Deposits",
        f"{deposits.sum or 0}$",
        f"{deposits.count or 0}"
    )
    table.add_row(
        "Withdrawals",
        f"{withdrawals.sum or 0}$",
        f"{withdrawals.count or 0}"
    )
    table.add_row("Total", f"{total_sum}$", f"{total_count}")

    return table
