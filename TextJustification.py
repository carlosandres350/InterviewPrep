class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        currentLineLength = 0
        i = 0

        while i < len(words):
            #check if were able to add the current word into our line []
            if currentLineLength + len(line) + len(words[i]) > maxWidth:
                # trying to add the current word exceeds max length of our current line
                # calculate how many spaces we need to make our line equal maxwidth
                # then append the line with spaces to our res list
                extraSpace = maxWidth - currentLineLength # count of spaces we need to add to equal our max width
                spaces = extraSpace // max(1, len(line) - 1) # count of spaces to evenly distribute between our words
                remainder = extraSpace % max(1, len(line) - 1) # count of remaining spaces that we  need to add in greedily from left to right
                #iterate through line and add the spaces
                for x in range(max(1, len(line) - 1)):
                    space = " " * spaces 
                    line[x] += space
                    if remainder > 0:
                        line[x] += " "
                        remainder -=1
                res.append("".join(line))
                line = []
                currentLineLength = 0

            line.append(words[i])
            currentLineLength += len(words[i])
            i+=1
        #handle adding our last line to our res
        last_line = " ".join(line)
        space_left = maxWidth - len(last_line)
        last_line += " " * space_left
        res.append("".join(last_line))
        return res
        
        