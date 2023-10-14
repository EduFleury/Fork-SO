import threading
import time
import random

# Definir um buffer compartilhado
buffer = []
buffer_size = 5
mutex = threading.Lock()
produtor_semaforo = threading.Semaphore(buffer_size)
consumidor_semaforo = threading.Semaphore(0)

# Função do produtor
def produtor():
    for i in range(1, 11):
        produtor_semaforo.acquire()
        mutex.acquire()
        item = random.randint(1, 100)
        buffer.append(item)
        print(f"Produtor: Produziu {item}")
        mutex.release()
        consumidor_semaforo.release()
        time.sleep(random.uniform(0.1, 0.5))

# Função do consumidor
def consumidor():
    for i in range(1, 11):
        consumidor_semaforo.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumidor: Consumiu {item}")
        mutex.release()
        produtor_semaforo.release()
        time.sleep(random.uniform(0.1, 0.5))

# Criar threads para o produtor e consumidor
produtor_thread = threading.Thread(target=produtor)
consumidor_thread = threading.Thread(target=consumidor)

# Iniciar as threads
produtor_thread.start()
consumidor_thread.start()

# Aguardar o término das threads
produtor_thread.join()
consumidor_thread.join()
