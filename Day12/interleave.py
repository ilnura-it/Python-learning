def interleave(a, b):
    return ''.join(
        list(
            map(
                lambda x: ''.join(x),
                (zip(a, b))
            )
        )
    )


print(interleave('hi','ha'))  # 'hhia'
print(interleave('aaa', 'zzz')) # 'azazaz'
print(interleave('lzr','iad')) #  'lizard'