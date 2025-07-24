import math
import matplotlib.pyplot as plt
import numpy as np

def poisson_pmf(lmbda, k):
    """
    Calculates the probability of observing k events in a fixed interval,
    given an average rate of lmbda events per interval.

    This is the Probability Mass Function (PMF) for the Poisson distribution.

    Args:
        lmbda: The average number of events per interval (lambda).
        k: The number of events to calculate the probability for.

    Returns:
        The probability P(X=k).
    """
    # --- YOUR CODE GOES HERE --- #
    # TODO: Implement the Poisson PMF formula:
    # P(k) = (lambda^k * e^(-lambda)) / k!
    # HINT: Use math.exp() for e and math.factorial() for k!

    numerator = pow(lmbda, k) * math.exp(-1*lmbda)
    deno = math.factorial(k)

    return numerator / deno
    # --- END OF YOUR CODE --- #

def hypergeometric_pmf(N, K, n, k):
    """
    Calculates the probability of getting k successes in n draws,
    without replacement, from a finite population of size N
    that contains exactly K successes.

    This is the PMF for the Hypergeometric distribution.

    Args:
        N: The total size of the population.
        K: The total number of "success" items in the population.
        n: The number of items drawn (sample size).
        k: The number of "success" items in the sample.

    Returns:
        The probability P(X=k).
    """
    # --- YOUR CODE GOES HERE --- #
    # TODO: Implement the Hypergeometric PMF formula:
    # P(k) = [ (K choose k) * (N-K choose n-k) ] / (N choose n)
    # HINT: Use a helper function for combinations (nCr).
    numerator = combinations(K, k) * combinations(N-K, n-k)
    deno = combinations(N, n)

    return numerator / deno
    
    # --- END OF YOUR CODE --- #

def combinations(n, r):
    """Helper function to calculate combinations (nCr)."""
    if r < 0 or r > n:
        return 0
    f = math.factorial
    return f(n) // (f(r) * f(n - r))

def plot_poisson_distribution(ax, lmbda):
    """Plots the PMF of a Poisson distribution on a given axes."""
    k_values = np.arange(0, 20)
    probabilities = [poisson_pmf(lmbda, k) for k in k_values]

    ax.bar(k_values, probabilities, color='skyblue', edgecolor='black')
    ax.set_title(f'Poisson Distribution PMF (λ = {lmbda})', fontsize=16)
    ax.set_xlabel('Number of Events (k)', fontsize=12)
    ax.set_ylabel('Probability P(X=k)', fontsize=12)
    ax.set_xticks(k_values)
    ax.grid(True)

def plot_hypergeometric_distribution(ax, N, K, n):
    """Plots the PMF of a Hypergeometric distribution on a given axes."""
    k_values = np.arange(0, n + 1)
    probabilities = [hypergeometric_pmf(N, K, n, k) for k in k_values]

    ax.bar(k_values, probabilities, color='lightgreen', edgecolor='black')
    ax.set_title(f'Hypergeometric Distribution PMF (N={N}, K={K}, n={n})', fontsize=16)
    ax.set_xlabel('Number of Successes in Sample (k)', fontsize=12)
    ax.set_ylabel('Probability P(X=k)', fontsize=12)
    ax.set_xticks(k_values)
    ax.grid(True)


# --- Main Execution ---
if __name__ == "__main__":
    # --- Parameters ---
    # Poisson
    lambda_calls = 5
    k_calls = 3
    # Hypergeometric
    N_cards = 52
    K_aces = 4
    n_hand = 5
    k_in_hand = 2

    # --- Calculations ---
    prob_3_calls = poisson_pmf(lambda_calls, k_calls)
    prob_2_aces = hypergeometric_pmf(N_cards, K_aces, n_hand, k_in_hand)

    # --- Print Results ---
    print(f"--- Poisson Distribution Example ---")
    print(f"The probability of receiving exactly {k_calls} calls is: {prob_3_calls:.4f}")
    print("\n" + "="*40 + "\n")
    print(f"--- Hypergeometric Distribution Example ---")
    print(f"The probability of getting exactly {k_in_hand} aces in a {n_hand}-card hand is: {prob_2_aces:.4f}")

    # --- Plotting ---
    print("\nGenerating combined plot...")
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    fig.suptitle('Comparison of Discrete Probability Distributions', fontsize=20)

    # Plot Poisson
    plot_poisson_distribution(ax1, lambda_calls)

    # Plot Hypergeometric
    plot_hypergeometric_distribution(ax2, N_cards, K_aces, n_hand)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
