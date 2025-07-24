
import math

def permutations(n, r):
  """
  Calculates the number of permutations of r objects from a set of n objects.
  """
  return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
  """
  Calculates the number of combinations of r objects from a set of n objects.
  """
  if r < 0 or r > n:
      return 0
  return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def partitions(n, group_sizes):
  """
  Calculates the number of ways to partition n objects into groups of given sizes.
  """
  denominator = 1
  for size in group_sizes:
    denominator *= math.factorial(size)
  return math.factorial(n) // denominator

def binomial_expansion_string(n):
    """
    Returns the string representation of the expansion of (x+y)^n.
    """
    expansion = []
    for r in range(n + 1):
        coeff = combinations(n, r)
        
        # Handle coefficient
        if coeff == 1 and n != 0:
            coeff_str = ""
        else:
            coeff_str = str(coeff)

        # Handle x term
        if n - r > 0:
            if n - r == 1:
                x_term = "x"
            else:
                x_term = f"x^{n-r}"
        else:
            x_term = ""

        # Handle y term
        if r > 0:
            if r == 1:
                y_term = "y"
            else:
                y_term = f"y^{r}"
        else:
            y_term = ""
        
        # Join terms
        term_parts = [part for part in [coeff_str, x_term, y_term] if part]
        term = "".join(term_parts)
        
        # Handle case where term is just a number (e.g., for (x+y)^0)
        if not term and coeff_str:
            term = coeff_str

        expansion.append(term)
        
    return " + ".join(expansion)


# --- Examples ---

print("--- Permutations ---")
# How many ways can you arrange 2 letters from the set {A, B, C}?
n_perm = 3
r_perm = 2
print(f"Number of permutations of {r_perm} objects from {n_perm}: {permutations(n_perm, r_perm)}")
print("-" * 20)


print("\n--- Combinations ---")
# How many ways can you choose 2 letters from the set {A, B, C}?
n_comb = 3
r_comb = 2
print(f"Number of combinations of {r_comb} objects from {n_comb}: {combinations(n_comb, r_comb)}")

# You have 10 friends, and you want to invite 3 of them to a party.
# How many different groups of friends can you invite?
n_friends = 10
r_friends = 3
print(f"Number of ways to invite {r_friends} friends from {n_friends}: {combinations(n_friends, r_friends)}")
print("-" * 20)


print("\n--- Partitions ---")
# How many ways to assign 10 students to a lighting team of 7 and a sound team of 3?
n_students = 10
team_sizes = [7, 3]
print(f"Number of ways to partition {n_students} students into groups of {team_sizes}: {partitions(n_students, team_sizes)}")

# How many ways to deal 52 cards to 4 players (13 each)?
n_cards = 52
player_hand_sizes = [13, 13, 13, 13]
print(f"Number of ways to deal {n_cards} cards to 4 players: {partitions(n_cards, player_hand_sizes)}")
print("-" * 20)


print("\n--- Binomial Theorem ---")
# What is the expansion of (x+y)^3?
n_binom = 3
print(f"The expansion of (x+y)^{n_binom} is: {binomial_expansion_string(n_binom)}")

# What is the expansion of (x+y)^5?
n_binom_2 = 5
print(f"The expansion of (x+y)^{n_binom_2} is: {binomial_expansion_string(n_binom_2)}")
print("-" * 20)
