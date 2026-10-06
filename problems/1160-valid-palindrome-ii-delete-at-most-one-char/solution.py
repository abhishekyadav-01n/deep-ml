def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            # Try deleting the left character
            l = left + 1
            r = right

            while l < r and s[l] == s[r]:
                l += 1
                r -= 1

            if l >= r:
                return True

            # Try deleting the right character
            l = left
            r = right - 1

            while l < r and s[l] == s[r]:
                l += 1
                r -= 1

            return l >= r

    return True