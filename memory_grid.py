from memory_block import MemoryBlock
from rich import print as print_rich
class MemoryGrid:
    def __init__(self, size):
        self.blocks = [MemoryBlock(size // 10) for _ in range(10)]

    def allocate(self, data):
        for block in self.blocks:
            if not block.occupied:
                block.allocate(data)
                return
        print_rich("[bold red]No free memory blocks available![/bold red]")

    def allocate_dynamic(self, data, size):
        for block in self.blocks:
            if not block.occupied and block.size >= size:
                block.allocate(data)
                return
        print_rich("[bold red]No suitable memory block available![/bold red]")

    def free(self, block_index):
        if 0 <= block_index < len(self.blocks):
            self.blocks[block_index].free()
        else:
            print_rich("[bold red]Invalid block index![/bold red]")

    def view_memory(self):
        for i, block in enumerate(self.blocks):
            status = "Occupied" if block.occupied else "Free"
            print_rich(f"[bold green]Block {i}: Size {block.size}, {status}, Data: {block.data}[/bold green]")

    def compact_memory(self):
        occupied_blocks = [block for block in self.blocks if block.occupied]
        free_blocks = [block for block in self.blocks if not block.occupied]

        self.blocks = occupied_blocks + free_blocks
        print_rich("[bold green]Memory compaction completed. All occupied blocks moved to the beginning.[/bold green]")