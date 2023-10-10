# Python program to explain os.fork() method 

#Sintaxe: os.fork()
#Parâmetro: Nenhum parâmetro é necessário
#Tipo de retorno: Este método retorna um valor inteiro representando o ID do processo filho no processo pai enquanto 0 no processo filho. 

# importing os module 
import os 


# Create a child process 
# using os.fork() method 
pid = os.fork() 

# pid greater than 0 represents 
# the parent process 
if pid > 0 : 
	print("Eu sou um processo Pai:") 
	print("ID do Processo PAI:", os.getpid()) 
	print("ID do Processo FILHO resgatado diretamente por pid:", pid) 

# pid equal to 0 represents 
# the created child process 
else : 
	print("\nEu sou um Processo Filho:") 
	print("ID do Processo FILHO:", os.getpid()) 
	print("ID do Processo PAI:", os.getppid()) 


# If any error occurred while 
# using os.fork() method 
# OSError will be raised 
