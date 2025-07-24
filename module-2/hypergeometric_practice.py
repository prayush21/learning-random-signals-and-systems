import math

def combinations(n, r):
  """
  Calculates the number of combinations of r objects from a set of n objects.
  This is a helper function for the main calculation.
  """
  if r < 0 or r > n:
      return 0
  # Using math.comb is the most direct way in Python 3.8+
  # If using an older version, the factorial formula is:
  # return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
  return math.comb(n, r)

def hypergeometric_probability(N, K, n, k):
  """
  Calculates the hypergeometric probability.

  Args:
    N: Total number of items in the population.
    K: Total number of "success" items in the population.
    n: The number of items drawn (sample size).
    k: The number of "success" items in the draw.
  
  Returns:
    The probability of getting exactly k successes in a sample of size n.
  """
  
  # --- YOUR CODE GOES HERE --- #
  #
  # TODO: Step 1: Calculate the number of ways to choose k successes from K total successes.
  # HINT: Use the combinations() function.
  ways_success = combinations(K, k)
  # TODO: Step 2: Calculate the number of ways to choose (n-k) failures from the (N-K) total failures.
  ways_failures = combinations(N-K, n-k)
  # TODO: Step 3: Calculate the total number of ways to choose n items from the population N.
  sample_size = combinations(N, n)
  # TODO: Step 4: Use the results from steps 1, 2, and 3 to calculate the final probability.
  # The formula is: (Step 1 * Step 2) / Step 3
  
  # Replace this placeholder with your final calculation
  probability = (ways_success * ways_failures) / (sample_size)
  
  return probability
  # --- END OF YOUR CODE --- #


# --- Main Execution & Practice Problem ---
if __name__ == "__main__":
    print("--- Hypergeometric Probability Practice ---")

    # Problem: A standard deck of 52 cards has 26 red cards and 26 black cards.
    # If you draw 5 cards without replacement, what is the probability that exactly 3 of them are red?

    # Define the parameters for our problem
    N_cards = 52 # Total cards in the deck
    K_red_cards = 26 # Total red cards in the deck (our "successes")
    n_draw = 5 # Number of cards we draw
    k_red_drawn = 3 # Number of red cards we want to get

    # Calculate the probability
    prob_3_red = hypergeometric_probability(N_cards, K_red_cards, n_draw, k_red_drawn)

    print(f"\nProblem: Drawing 5 cards from a 52-card deck.")
    print(f"What is the probability of getting exactly {k_red_drawn} red cards?")
    print(f"\nParameters:")
    print(f"  N (Population size): {N_cards}")
    print(f"  K (Successes in population): {K_red_cards}")
    print(f"  n (Sample size): {n_draw}")
    print(f"  k (Successes in sample): {k_red_drawn}")
    print(f"\nResult:")
    print(f"  The probability is: {prob_3_red:.4f} (or {prob_3_red:.2%})")

    # --- Verification (Optional) ---
    # The known correct answer for this problem is approximately 0.3251
    # You can use this to check if your implementation is correct.
    # For example:
    # ways_to_choose_3_red = combinations(26, 3) -> 2600
    # ways_to_choose_2_black = combinations(26, 2) -> 325
    # total_ways_to_choose_5_cards = combinations(52, 5) -> 2598960
    # probability = (2600 * 325) / 2598960 = 0.32513
