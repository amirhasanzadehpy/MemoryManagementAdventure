from rich import print as print_rich

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.occupied = False
        self.data = None

    def allocate(self, data):
        if not self.occupied:
            self.occupied = True
            self.data = data
            print_rich(f"[bold green]Allocated data is __{data}__ to memory block of size __{self.size}__![/bold green]")
        else:
            print_rich("[bold red]Allocated already occupied![/bold red]")

    def free(self):
        if self.occupied:
            print_rich(f"[bold green]releasing memory block with data: __{self.data}__ ...[/bold green]")
            self.occupied = False
            self.data = None
            print_rich(f"[bold green]... Block is now Free![/bold green]")

        else:
            print_rich("[bold red]memory already free![/bold red]")