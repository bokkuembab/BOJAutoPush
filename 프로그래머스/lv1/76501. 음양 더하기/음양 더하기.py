def solution(absolutes, signs):

    return sum(a if signs else -a for a, signs in zip(absolutes, signs))