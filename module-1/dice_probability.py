# Let's model a standard six-sided die roll.

# 1. Define the Sample Space (Ω)
# This is the set of ALL possible outcomes.
sample_space = {1, 2, 3, 4, 5, 6}

# 2. Define the Event (A) we care about.
# We want to know the probability of rolling an even number.
event_a = {2, 4, 6}

# 3. Define a simple probability function.
# This function calculates the probability of an event, assuming all outcomes
# in the sample space are equally likely.
def calculate_probability(event, space):
    """
    Calculates the probability of an event given a sample space.
    """
    # The formula from the slides: P(A) = |A| / |Ω|
    return len(event) / len(space)

# 4. Calculate the probability of our event.
prob_a = calculate_probability(event_a, sample_space)

# Let's print our results in a clear, readable way.
print(f"--- Probability Basics: Rolling a Die ---")
print(f"Sample Space (Ω): {sample_space}")
print(f"Event (A) - Rolling an even number: {event_a}")
print(f"Probability of Event A, P(A): {prob_a:.2f}") # Format to 2 decimal places

# --- Let's test another event ---
# Event (B): Rolling a number greater than 4
event_b = {5, 6}
prob_b = calculate_probability(event_b, sample_space)
print(f"\n--- Another Example ---")
print(f"Event (B) - Rolling a number > 4: {event_b}")
print(f"Probability of Event B, P(B): {prob_b:.2f}")
