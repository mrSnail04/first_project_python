import threading
# death_lock лечиться при помощи .Rlock(), разрешает вторичный захват
# только тому потоку, который уже захватил
lock_obj = threading.Lock()

print('Acquaire 1st time')
lock_obj.acquire()

print('Acquaire 2nd time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()

# def reenrance():
#     print('start')
#     lock_obj.acquire()
#     print('Acquaired')
#     reenrance()
# reenrance()


