import time  
from mpi4py import MPI 

def mpi_calculation():
    comm = MPI.COMM_WORLD  # Get the global MPI communicator
    rank = comm.Get_rank()  # Get the rank of the current process (0)
    size = comm.Get_size()  # Get the total number of processes (4 or 8)

    s = 0  
    n = 1  

    if rank == 0:
        start_time = time.time()  # Record the start time before the calculation begins

    # Each process executes this loop independently
    for i in range(1000000000 // size):  # Divide the workload among all processes
        n = (n + 1) % 1000  # Increment n and wrap it around to stay within 0-999
        s += n  # Add the current value of n to the sum

    # Reduce the sums from all processes to the root process (rank 0)
    total_sum = comm.reduce(s, op=MPI.SUM, root=0)

    if rank == 0:
        end_time = time.time()  # Record the end time after the calculation is complete
        print(f'Total sum with MPI: {total_sum}')  
        print(f'Execution time with MPI: {end_time - start_time} seconds')  

if __name__ == '__main__':
    mpi_calculation()  
