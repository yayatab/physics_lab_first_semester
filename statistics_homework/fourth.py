import general_tools.histogram
from general_tools.statistics import *
from general_tools.plotting import *

if __name__ == '__main__':
    theoretical_sigma = 1 / general_math.sqrt(12)
    n = 1000
    buckets_num = 5
    buckets = [genereate_uniform_random(n) for b in range(buckets_num)]
    sigmas = [standard_diviation(b) for b in buckets]
    print(theoretical_sigma)
    print(sigmas)
    for b, i in zip(buckets, [1, 2, 3, 4, 5]):
        general_tools.generate_histogram_auto(b, './figure' + str(i) + '.jpeg')

    long_bucket = []
    for b in buckets:
        long_bucket.extend(b)
    print(general_math.average_of_list(long_bucket), standard_diviation(long_bucket), theoretical_sigma)
    general_tools.generate_histogram_auto(b, './figure' + str(6) + '_5000.jpeg')

    long_bucket = []
    for i in range(buckets_num):
        long_bucket.append(sum(x[i] for x in buckets))
    print(general_math.average_of_list(long_bucket), standard_diviation(long_bucket), theoretical_sigma)
    general_tools.generate_histogram_auto(b, './figure' + str(7) + '_sum.jpeg')

"""
# theo
0.2886751345948129
# buecket's sigmas
[0.2878930002263699, 0.2832133275430643, 0.2963950044964545, 0.2836081175194647, 0.28973361240359996]
# avg             | sigma            | theo
# ------------------------------------------------------ 
0.5020317807587847 0.2884477843077643 0.2886751345948129
2.8565914124939704 0.3145539162161908 0.2886751345948129
"""