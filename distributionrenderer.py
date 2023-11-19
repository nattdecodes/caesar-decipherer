
from json import dumps

str = """E   12.4%    H    6.5%    U    2.7%    G    2.0%    K    0.7%
T    8.9%    S    6.2%    M    2.5%    Y    2.0%    Q    0.1%
A    8.0%    R    6.1%    W    2.3%    P    1.6%    X    0.1%
O    7.6%    D    4.6%    C    2.2%    B    1.3%    J    0.1%
N    7.0%    L    3.6%    F    2.2%    V    0.8%    Z    0.0%
I    6.7% """;

l = str.split("%");
l = "".join(l).replace("\n", " ");

# Split the modified string back into a list based on spaces
l = l.split();

# Iterate through the list and modify items
for index in range(len(l)):
    try:
        l[index] = float(l[index])
    except ValueError:
        l[index] = l[index].lower()

res_dict = {}
for i in range(0, len(l), 2):
    res_dict[l[i]] = l[i + 1]

res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: item[1], reverse=True)}
s = ',\n   '.join(dumps(res_dict).split(','))
s = s[0] + '\n    ' + s[1:-1] + '\n' + s[-1]
print(s)