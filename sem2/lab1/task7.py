#  from rich import print

# print("[bold red]Hello, World![/bold red]")




from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Example Table")
table.add_column("ID", style="cyan")
table.add_column("Name", style="magenta")
table.add_column("Score", style="green")

table.add_row("1", "Alice", "95")
table.add_row("2", "Bob", "89")
table.add_row("3", "Charlie", "92")

console.print(table)
