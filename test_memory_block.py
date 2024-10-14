from memory_block import MemoryBlock

block = MemoryBlock(10)

block.allocate("adventure Gear!")
block.allocate("againg adventure Gear!")

block.free()
block.allocate("againg adventure Gear!")
block.free()
