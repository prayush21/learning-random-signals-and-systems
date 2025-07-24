import random
import collections
import matplotlib.pyplot as plt

def bernoulli_trial(p):
  """
  Simulates a single Bernoulli trial.

  Args:
    p: The probability of success (a float between 0 and 1).

  Returns:
    1 for success, 0 for failure.
  """
  # --- YOUR CODE GOES HERE --- #
  #
  # TODO: Step 1: Generate a random number between 0 and 1.
  # HINT: The random.random() function is perfect for this.
  if random.random() < p:
    return 1
  else:
    return 0
  # TODO: Step 2: Compare the random number to the probability p.
  # If the number is less than p, it's a success (return 1).
  # Otherwise, it's a failure (return 0).
  
  pass # Replace this line with your code
  # --- END OF YOUR CODE --- #

def run_binomial_experiment(n, p):
  """
  Runs a binomial experiment by performing n Bernoulli trials.

  Args:
    n: The total number of trials.
    p: The probability of success for each trial.

  Returns:
    The total number of successes out of n trials.
  """
  
  success_count = 0
  # --- YOUR CODE GOES HERE --- #
  #
  # TODO: Step 1: Loop n times.
  for i in range(10):
    if(bernoulli_trial(p) == 1):
      success_count += 1
  
  # --- END OF YOUR CODE --- #
  return success_count

def plot_pmf(pmf, n, p, num_experiments):
    """Plots the PMF of the binomial experiment results."""
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))

    # Sort the outcomes for plotting
    sorted_outcomes = sorted(pmf.keys())
    
    # Create the bar plot
    ax.bar(sorted_outcomes, [pmf[k] for k in sorted_outcomes], 
           label='Experimental PMF', color='skyblue', edgecolor='black')

    ax.set_title(f'PMF of Binomial Distribution (n={n}, p={p})', fontsize=16)
    ax.set_xlabel('Number of Successes (k)', fontsize=12)
    ax.set_ylabel('Probability P(X=k)', fontsize=12)
    ax.set_xticks(range(n + 1))
    ax.legend()
    
    plt.suptitle(f'Results from {num_experiments} experiments', y=0.92)
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    # --- Parameters ---
    # Probability of success for a single trial (e.g., a biased coin flip)
    p_success = 0.6 
    
    # Number of trials in one experiment (e.g., how many times we flip the coin)
    n_trials = 10
    
    # Total number of experiments to run to simulate the distribution
    num_experiments = 10000

    print(f"--- Running Binomial Simulation ---")
    print(f"Probability of success (p): {p_success}")
    print(f"Number of trials per experiment (n): {n_trials}")
    print(f"Total experiments: {num_experiments}\n")

    # 1. Run the simulation many times
    results = [run_binomial_experiment(n_trials, p_success) for _ in range(num_experiments)]

    # 2. Calculate the PMF from the results
    # We count how many times we got 0 successes, 1 success, 2 successes, etc.
    counts = collections.Counter(results)
    
    # Then we divide by the total number of experiments to get the probability
    pmf = {k: v / num_experiments for k, v in sorted(counts.items())}

    print("--- Results (Experimental PMF) ---")
    for k, prob in pmf.items():
        print(f"  P(X = {k}) = {prob:.4f}")

    # 3. Visualize the results
    print("\nGenerating plot...")
    plot_pmf(pmf, n_trials, p_success, num_experiments)
