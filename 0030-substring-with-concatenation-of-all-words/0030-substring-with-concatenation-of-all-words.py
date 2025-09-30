class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        n = len(s)

        # build word frequency dictionary
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        ans = []

        # try each possible starting offset within a word
        for offset in range(word_len):
            left = offset
            right = offset
            seen = {}
            count = 0  # how many words matched so far

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # if seen too many of one word, shrink from left
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # if window has all words
                    if count == len(words):
                        ans.append(left)

                else:
                    # reset window
                    seen.clear()
                    count = 0
                    left = right

        return ans
