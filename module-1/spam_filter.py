# --- Data ---
# A simple dataset of "spam" and "ham" (not spam) messages.
spam_messages = [
    "Super deal! Buy now!",
    "Exclusive offer: cheap viagra",
    "Limited time deal on viagra",
    "Don't miss this deal"
]

ham_messages = [
    "Hi John, what's up?",
    "Can you review this report?",
    "Meeting at 5pm",
    "Let's catch up later"
]

def calculate_spam_probability(keyword):
    """
    Calculates P(Spam | keyword) using Bayes' Theorem.
    """
    num_spam = len(spam_messages)
    num_ham = len(ham_messages)
    total_messages = num_spam + num_ham

    # 1. Calculate Priors: P(Spam) and P(Ham)
    # The overall probability of any given message being spam or ham.
    p_spam = num_spam / total_messages
    p_ham = num_ham / total_messages

    # 2. Calculate Likelihoods: P(keyword | Spam) and P(keyword | Ham)
    # How likely is the keyword to appear in a spam message?
    spam_containing_keyword = sum(1 for msg in spam_messages if keyword in msg)
    p_keyword_given_spam = spam_containing_keyword / num_spam

    # How likely is the keyword to appear in a ham message?
    ham_containing_keyword = sum(1 for msg in ham_messages if keyword in msg)
    p_keyword_given_ham = ham_containing_keyword / num_ham

    # 3. Calculate Evidence: P(keyword)
    # The overall probability of the keyword appearing in any message.
    # P(keyword) = P(keyword | Spam) * P(Spam) + P(keyword | Ham) * P(Ham)
    p_keyword = (p_keyword_given_spam * p_spam) + (p_keyword_given_ham * p_ham)

    # 4. Calculate Posterior using Bayes' Theorem: P(Spam | keyword)
    # P(Spam | keyword) = [P(keyword | Spam) * P(Spam)] / P(keyword)
    if p_keyword == 0:
        # Avoid division by zero if the keyword is not in any message
        return 0.0

    p_spam_given_keyword = (p_keyword_given_spam * p_spam) / p_keyword

    # --- Optional: Print the intermediate steps for clarity ---
    print(f"\n--- Intermediate Calculations ---")
    print(f"P(Spam) = {p_spam:.2f} ({num_spam}/{total_messages})")
    print(f"P(Ham) = {p_ham:.2f} ({num_ham}/{total_messages})")
    print(f"P('{keyword}' | Spam) = {p_keyword_given_spam:.2f} ({spam_containing_keyword}/{num_spam})")
    print(f"P('{keyword}' | Ham) = {p_keyword_given_ham:.2f} ({ham_containing_keyword}/{num_ham})")
    print(f"P('{keyword}') = {p_keyword:.2f}")
    print(f"--------------------------------")

    return p_spam_given_keyword

# --- Main Execution ---
keyword_to_test = "deal"
spam_probability = calculate_spam_probability(keyword_to_test)

print(f"--- Naive Bayes Spam Filter ---")
print(f"Total messages in dataset: {len(spam_messages) + len(ham_messages)}")
print(f"Keyword to test: '{keyword_to_test}'")
print(f"\nThe probability of a message being SPAM given it contains the word '{keyword_to_test}' is: {spam_probability:.2%}")