from memory_grid import MemoryGrid

# grid = MemoryGrid(100)
# print("\n--- Testing Dynamic Memory Allocation ---")
# grid.view_memory()
#
#
# grid.allocate_dynamic(size=1, data="Data A")
# grid.allocate_dynamic(size=2, data="Data B")
# grid.allocate_dynamic(size=3, data="Data C")
# grid.allocate_dynamic(size=5, data="Data D")
# grid.allocate_dynamic(size=10, data="Data E")
#
#
# print("\nMemory State After Dynamic Allocations:")
# grid.view_memory()
#
#
# print("\nTrying to allocate a block of size 12 (too large for available free blocks)...")
# grid.allocate_dynamic(size = 12, data="Data D")
#
# grid.allocate_dynamic(size=10, data="Data New")
# grid.free(2)
# grid.free(3)
#
# grid.view_memory()
# grid.merge_free_blocks()
# grid.view_memory()
#

# Initialize a memory grid of size 100
grid = MemoryGrid(100)

# Allocate using different strategies
grid.allocate_dynamic(size=5, data="Data A", strategy='first-fit')  # Allocates in the first block that can fit
grid.allocate_dynamic(size=8, data="Data B", strategy='best-fit')   # Allocates in the smallest suitable block
grid.allocate_dynamic(size=6, data="Data C", strategy='worst-fit')  # Allocates in the largest suitable block
grid.allocate_dynamic(size=4, data="Data E", strategy='best-fit')
# Display the current memory status
grid.view_memory()
