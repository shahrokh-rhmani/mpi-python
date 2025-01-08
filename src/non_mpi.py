import time

def non_mpi_calculation():
    s = 0
    n = 1

    start_time = time.time()

    for i in range(1000000000):
        n = (n + 1) % 1000
        s += n 

    end_time = time.time()
    print(f'Total sum without MPI: {s}')
    print(f'Execution time without MPI: {end_time - start_time} seconds')

if __name__ == '__main__':
    non_mpi_calculation()
