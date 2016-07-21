import re

test_a = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
print(test_a)

test_b = 'a b   c'.split(' ')
print(test_b)

test_c = re.split(r'\s+', 'a b   c')
print(test_c)

test_d = re.split(r'[\s,]+','a,b, c  d')
print(test_d)

test_e = re.split(r'[\s;,]+','a,b;; c  d')
print(test_e)

# group

test_f = re.match(r'(\d{3})-(\d{3,8})','010-12345')
print(test_f.group(0), test_f.group(1), test_f.group(2))

test_g = re.match(r'^(\d+)(0*)$', '102300').groups()
print(test_g)

test_h = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(test_h)

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())