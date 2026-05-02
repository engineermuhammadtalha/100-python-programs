#  Remove duplicates (preserve order)
def unique(seq):
    seen = set(); out = []
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

print(unique([1,2,2,3,1]))  # Output: [1,2,3]
