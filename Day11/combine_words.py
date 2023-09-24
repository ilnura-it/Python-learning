def combine_words(str, **kwargs):
    if kwargs:
        for key, value in kwargs.items():
            if key == "prefix":
                return f"{value}{str}"
            elif key == "suffix":
                return f"{str}{value}"

    return str

print(combine_words("child")) # child
print(combine_words("child", prefix="man")) #'manchild'
print(combine_words("child", suffix="ish")) # 'childish'
print(combine_words("work", suffix="er")) # 'worker'
print(combine_words("work", prefix="home")) # 'homework

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word