def filtervowel(alpha):
    v=['a','e','i','o','u']
    if alpha in v:
        return True
    else:
        return False
alpha=['a','b','c','d','e','f','g','h','i']
filtered=filter(filtervowel,alpha)
print('Vowels after filteration are: ')
for v in filtered:
    print(v)
# To see more consult EX3.Filter_function.py#