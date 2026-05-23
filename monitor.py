import psutil

cpu = psutil.cpu_percent()

memory = psutil.virtual_memory()

print("CPU:", cpu)

print("Memory:", memory.percent)