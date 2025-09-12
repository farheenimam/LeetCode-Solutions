class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        counter = []
        len_of_sent = 0

        for word in words:
            if len(word) + len(counter) + len_of_sent > maxWidth:
                for i in range(maxWidth - len_of_sent):
                    counter[i % (len(counter)-1 or 1)] += ' '
                lines.append(''.join(counter))
                counter, len_of_sent = [], 0
            counter += [word] 
            len_of_sent += len(word)
        return lines + [' '.join(counter).ljust(maxWidth)]   

        