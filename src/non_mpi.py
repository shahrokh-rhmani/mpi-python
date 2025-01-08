import time

def non_mpi_calculation():
    s = 0  
    n = 1

    start_time = time.time()  # Record the start time before the calculation begins

    # Loop 1,000,000,000 times
    for i in range(1000000000):
        n = (n + 1) % 1000  # Increment n and wrap it around to stay within 0-999
        s += n  # Add the current value of n to the sum

    end_time = time.time()  # Record the end time after the calculation is complete
    print(f'Total sum without MPI: {s}')  
    print(f'Execution time without MPI: {end_time - start_time} seconds')  

if __name__ == '__main__':
    non_mpi_calculation() 
