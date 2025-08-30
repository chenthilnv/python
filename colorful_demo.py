from colorama import init, Fore, Style
from rich import print

init(autoreset=True)
print(Fore.RED + "This is red text using colorama!")
print(Fore.GREEN + Style.BRIGHT + "Bright green text using colorama!")

print("[bold magenta]This is bold magenta text using rich![/bold magenta]")
print("[yellow on blue]Yellow on blue background using rich![/yellow on blue]")
