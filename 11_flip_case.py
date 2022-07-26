def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    final_word = ""

    for letter in phrase:
        if letter == to_swap or letter == to_swap.swapcase():
            final_word = final_word+letter.swapcase()
        else:
            final_word = final_word+letter

    return final_word

