import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(free)
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print(usage)
    return usage < 75


print(check_disk_usage("/"))
print(check_cpu_usage())

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
