from functools import reduce


def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            if not lines: return [word]
            
            current_line = lines[-1]
            
            if len(current_line) + len(word) + 1 > line_length:
                lines.append(word)
            
            else:
                current_line += " " + word
                lines[-1] = current_line
            
            return lines

        return reduce(add_word_to_lines, words, [])

    return lineate

one = lineator(10)
two = one('Autobots roll out! The Autobots are always ready for battle.')
for word in two:
    print(word)