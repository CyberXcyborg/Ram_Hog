import ctypes
import sys

def allocate_memory():
    block_size = 1024 * 1024 * 10  # Allocate 10 MB of memory each time
    memory_blocks = []

    try:
        while True:
            memory_blocks.append(ctypes.create_string_buffer(block_size))
            print(f"Allocated additional {block_size / (1024 * 1024)} MB, total allocated memory: {sys.getsizeof(memory_blocks)} bytes")
    except MemoryError:
        print("Memory limit exceeded. Exiting...")

if __name__ == '__main__':
    allocate_memory()
