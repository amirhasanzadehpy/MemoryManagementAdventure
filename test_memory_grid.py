from memory_grid import MemoryGrid

grid = MemoryGrid(block_size=10, num_blocks=5)


print("initial memory state:")
grid.view_memory()

print("\nAllocating Data...")
grid.allocate("Adventure Gear")
grid.allocate("Map")
grid.allocate("Sword")

print("\nMemory State After Allocation:")
grid.view_memory()

print("\nFreeing Block 1...")
grid.free(1)

print("\nMemory State After Freeing Block 1:")
grid.view_memory()

print("\nAllocating More Data...")
grid.allocate("Shield")
grid.allocate("Helmet")
grid.allocate("Potion")

grid.free(1)
grid.free(3)
grid.view_memory()

grid.compact_memory()
grid.view_memory()