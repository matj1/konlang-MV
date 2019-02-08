import random

with open('vowels.txt') as text_file:
    text = text_file.read()
    vowels = text.split(' ')

with open('consontants.txt') as text_file:
    text = text_file.read()
    consontants = text.split(' ')


def generate_roots(consontants, vowels):

    roots = []
    root = []

    for i in vowels:
        d = 0
        for x in range(pow(len(consontants), 2)):
            for e,j in enumerate(consontants):
                if e+d < len(consontants):
                    root.append(j)
                    root.append(i)
                    root.append(consontants[e+d])
                    roots.append(''.join(root))
                    if root != root[::-1]:
                        roots.append(''.join(root[::-1]))
                    root = []
            d += 1

    return roots

data = generate_roots(consontants, vowels)
number_of_roots = len(data)
data = random.sample(data, len(data))


with open('output.txt', 'w') as text_file:
    print(str(len(data)) + " roots (with " + ', '.join(consontants) + ", " \
         + ', '.join(vowels) + " as symbols):\n" + ' '.join(data), file=text_file)
