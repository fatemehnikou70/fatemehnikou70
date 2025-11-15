"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a formatted string."""
    prefix = vocab_words[0]
    # Construct each word with prefix applied
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    # Join prefix + all prefixed words
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' while keeping spelling in mind."""
    root = word[:-4]   # remove "ness"

    # If ends in "i" and the original was "...iness", replace 'i' with 'y'
    if root.endswith("i"):
        return root[:-1] + "y"

    return root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    # Remove punctuation, extract word
    words = sentence.replace(".", "").split()
    return words[index] + "en"
