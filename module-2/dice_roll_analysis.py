import collections
import matplotlib.pyplot as plt

def get_pmf(outcomes):
  """
  Calculates the Probability Mass Function (PMF) from a list of outcomes.

  Args:
    outcomes: A list of all possible outcomes for the random variable.

  Returns:
    A dictionary representing the PMF, where keys are the outcomes 
    and values are their probabilities.
  """
  
  # --- YOUR CODE GOES HERE --- #
  #
  # TODO: Step 1: Count the occurrences of each outcome.
  # HINT: The collections.Counter class is great for this.
  counts = collections.Counter(outcomes)
  # TODO: Step 2: Calculate the total number of outcomes.
  total_outcomes = len(outcomes)
  # TODO: Step 3: Create the PMF dictionary.
  # Iterate through the counts and divide by the total number of outcomes to get the probability.
  
  # Replace this placeholder
  pmf = {}
  for item, value in counts.items():
    pmf[item] = value/total_outcomes
  
  
  return pmf
  # --- END OF YOUR CODE --- #

def get_cdf(pmf):
  """
  Calculates the Cumulative Distribution Function (CDF) from a PMF.

  Args:
    pmf: A dictionary representing the PMF.

  Returns:
    A dictionary representing the CDF.
  """
  
  # --- YOUR CODE GOES HERE --- #
  #
  # TODO: Step 1: Sort the outcomes from the PMF.
  sorted_pmf = sorted(pmf.items(), key=lambda item: item[1])
  sorted_dict = dict(sorted_pmf)
  # TODO: Step 2: Initialize a cumulative probability variable to 0.
  cdf_var = 0
  # TODO: Step 3: Iterate through the sorted outcomes, adding the probability of each outcome
  # to the cumulative probability and storing the result in a new dictionary.
  cdf = {}
  for item, value in sorted_dict.items():
    cdf_var += value
    cdf[item] = cdf_var
  
  return cdf
  # --- END OF YOUR CODE --- #

def plot_pmf_cdf(pmf, cdf):
    """Plots the PMF and CDF side-by-side."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PMF
    ax1.bar(pmf.keys(), pmf.values(), width=0.1, color='skyblue', edgecolor='black')
    ax1.set_title('Probability Mass Function (PMF)')
    ax1.set_xlabel('Maximum Roll (X)')
    ax1.set_ylabel('Probability P(X=x)')
    ax1.set_xticks(list(pmf.keys()))
    ax1.grid(axis='y', linestyle='--')

    # Plot CDF
    # Create the points for the step function
    sorted_outcomes = sorted(cdf.keys())
    x_cdf = [sorted_outcomes[0] - 1] + sorted_outcomes
    y_cdf = [0] + [cdf[k] for k in sorted_outcomes]
    ax2.step(x_cdf, y_cdf, where='post', color='coral')
    ax2.set_title('Cumulative Distribution Function (CDF)')
    ax2.set_xlabel('Maximum Roll (X)')
    ax2.set_ylabel('Cumulative Probability P(X<=x)')
    ax2.set_xticks(list(pmf.keys()))
    ax2.set_yticks([i/10 for i in range(11)])
    ax2.grid(True, linestyle='--')
    ax2.set_ylim(0, 1.1)
    ax2.set_xlim(min(x_cdf), max(x_cdf))

    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    # Problem: A fair die is rolled twice. Let X be the maximum of the two rolls.
    
    # 1. Generate all possible outcomes
    # The sample space is 36 pairs of rolls (1,1), (1,2), ..., (6,6)
    all_rolls = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    # Our random variable X is the maximum of the two rolls
    X_outcomes = [max(roll) for roll in all_rolls]

    # 2. Calculate PMF and CDF
    pmf = get_pmf(X_outcomes)
    cdf = get_cdf(pmf)

    print("--- Analysis of Rolling a Die Twice (Max Value) ---")
    print(f"\nTotal number of outcomes: {len(X_outcomes)}")
    print(f"\nProbability Mass Function (PMF):")
    for val, prob in pmf.items():
        print(f"  P(X = {val}) = {prob:.4f}")

    print(f"\nCumulative Distribution Function (CDF):")
    for val, prob in cdf.items():
        print(f"  P(X <= {val}) = {prob:.4f}")

    # 3. Visualize the results
    print("\nGenerating plots...")
    plot_pmf_cdf(pmf, cdf)
