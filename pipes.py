import os
import signal
import time

# Função para o produtor
def produtor(pipe):
    for i in range(1, 6):
        print(f"Produtor: Enviando {i}")
        pipe.send(i)
        time.sleep(1)

# Função para o consumidor
def consumidor(pipe):
    while True:
        data = pipe.recv()
        print(f"Consumidor: Recebendo {data}")

if __name__ == '__main__':
    # Criar um pipe
    pipein, pipeout = os.pipe()

    # Criar os processos
    produtor_process = os.fork()

    if produtor_process == 0:
        # Processo filho (produtor)
        os.close(pipein)
        produtor(os.fdopen(pipeout, 'w'))
    else:
        # Processo pai
        os.close(pipeout)
        consumidor(os.fdopen(pipein, 'r'))

    # Esperar os processos filhos terminarem
    os.wait()
