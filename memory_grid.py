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

    def allocate_dynamic(self, data, size, strategy='first-fit'):
        selected_block_index = None
        if strategy == 'first-fit':
            for index, block in enumerate(self.blocks):
                if not block.occupied and block.size >= size:
                    selected_block_index = index
                    break
        elif strategy == 'best-fit':
            self.view_memory()
            min_size = float('inf')
            for index, block in enumerate(self.blocks):
                if not block.occupied and size <= block.size and block.size < min_size:
                    selected_block_index = index
                    min_size = block.size
        elif strategy == 'worst-fit':
            max_size = -1
            for index, block in enumerate(self.blocks):
                if not block.occupied and block.size >= size and size > max_size:
                    max_size = block.size
                    selected_block_index = index

        if selected_block_index is not None:
            block = self.blocks[selected_block_index]
            if block.size >= size:
                new_block = block.split(size)
                if new_block:
                    self.blocks.append(new_block)
                block.allocate(data)
                return True

        print_rich("[bold red]No suitable memory block available![/bold red]")
        return False

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
        print_rich("[bold green]\nCompacting memory...[/bold green]")
        allocated_blocks = []
        free_space = 0

        for block in self.blocks:
            if block.occupied:
                allocated_blocks.append(block)
            else:
                free_space += block.size

        self.blocks = allocated_blocks
        if free_space > 0:
            self.blocks.append(MemoryBlock(free_space))

        print_rich(f"[bold green]Memory compacted. {len(allocated_blocks)} blocks allocated, {free_space} units of free space consolidated.[/bold green]")

    def merge_free_blocks(self):
        i = 0
        while i < len(self.blocks) - 1:
            current_block = self.blocks[i]
            next_block = self.blocks[i + 1]

            if not current_block.occupied and not next_block.occupied:
                current_block.size += next_block.size
                self.blocks.pop(i+1)
            else:
                i += 1
        print_rich("[bold green]Merging complete. Adjacent free blocks combined.[/bold green]")
