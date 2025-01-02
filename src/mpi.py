import time
from mpi4py import MPI

def mpi_calculation():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    s = 0
    n = 1

    if rank == 0:
        start_time = time.time()

    for i in range(1000000000 // size):
        n = (n + 1) % 1000
        s += n * i

    # Reduce the sums from all processes
    total_sum = comm.reduce(s, op=MPI.SUM, root=0)

    if rank == 0:
        end_time = time.time()
        print(f'Total sum with MPI: {total_sum}')
        print(f'Execution time with MPI: {end_time - start_time} seconds')

if __name__ == '__main__':
    mpi_calculation()
