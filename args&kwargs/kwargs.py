# **kwargs

def marks(**kwargs):
    for item in kwargs.keys():
        print(item,kwargs[item])

marks(ajinkya = 84,jack = 92)