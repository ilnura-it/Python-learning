# Option 1 with map method
def interleave(a, b):
    return ''.join(
            map(
                lambda x: ''.join(x),
                (zip(a, b))
            )
    )

#Option2 with list comprehension
# def interleave(a, b):
#     return ''.join(''.join(x) for x in zip(a, b))

print(interleave('hi','ha'))  # 'hhia'
print(interleave('aaa', 'zzz')) # 'azazaz'
print(interleave('lzr','iad')) #  'lizard'