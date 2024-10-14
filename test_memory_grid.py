from memory_grid import MemoryGrid

grid = MemoryGrid(100)
print("\n--- Testing Dynamic Memory Allocation ---")
grid.view_memory()


grid.allocate_dynamic(size=1, data="Data A")
grid.allocate_dynamic(size=2, data="Data B")
grid.allocate_dynamic(size=3, data="Data C")
grid.allocate_dynamic(size=5, data="Data D")
grid.allocate_dynamic(size=10, data="Data E")


print("\nMemory State After Dynamic Allocations:")
grid.view_memory()


print("\nTrying to allocate a block of size 12 (too large for available free blocks)...")
grid.allocate_dynamic(size = 12, data="Data D")