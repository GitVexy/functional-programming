import timeit

def is_even_bitwiz(x=1) -> bool:
    return x & 1 == 0

def is_even_binary(x=1) -> bool:
    return bin(x)[-1] == 0

def is_even_modulo(x=1) -> bool:
    return x % 2 == 0

def is_even_string(x=1) -> bool:
    return (
        str(x).endswith("0") or
        str(x).endswith("2") or
        str(x).endswith("4") or
        str(x).endswith("6") or                                                                          #
        str(x).endswith("8")
        )
    
def is_even_stupid(x=1) -> bool:
    if x == 0: return True
    elif x == 1: return False
    
    while x > 1:
        if x == 0: return True
        elif x == 1: return False
        x -= 2

##### EVERYTHING UNDER HERE IS COOL, BUT UNIMPORTANT #####

n = 1250
ntimes = 10000

for i in range(0,5):

    results = {
        "Bitwiz time": timeit.timeit(lambda: is_even_bitwiz(n), number=ntimes),
        "Binary time": timeit.timeit(lambda: is_even_binary(n), number=ntimes),
        "Modulo time": timeit.timeit(lambda: is_even_modulo(n), number=ntimes),
        "String time": timeit.timeit(lambda: is_even_string(n), number=ntimes),
        "Stupid time": timeit.timeit(lambda: is_even_stupid(n), number=ntimes)
    }
    
    results = dict(sorted(results.items(), key=lambda x:x[1]))
    
    winner_value = min(results.values())
    winner_name = [key for key, value in results.items() if value == winner_value]
    
    loser_value = max(results.values())
    loser_name = [key for key, value in results.items() if value == loser_value]
    
    print(f"\nTesting all functions with:\nn = {n}, {ntimes} times\n")
    
    for key in results:
        print(f"{key}: {results[key]:.10f} seconds")
    
    print(f"\nWinner: {winner_name}, at {winner_value:.10f} seconds")
    print(f"Loser:  {loser_name}, at {loser_value:.10f} seconds\n")