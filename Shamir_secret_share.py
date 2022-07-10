limit = 10**3
#for x range is limit
import random
from math import ceil
from decimal import Decimal
import os
#new
def main():
    t, n = 4, 7
    #option to convert string to ascii to and use text as integrer
    text_secret = "yo"
    ascii_value=[]
    for character in text_secret:
        ascii_value.append(ord(character))
    int_secret = [str(integer) for integer in ascii_value]
    secret=int("".join(int_secret))
    print("Int secret ", secret)
    #option to predefine integer as secret
    secret = 6996
    print("The original data is ", secret)

    # Phase I: Generation of shares
    shares = generate_shares(n, t, secret)
    print(f'Shares: {", ".join(str(share) for share in shares)}')

    # Phase II: Secret Reconstruction
    random_shares_select = random.sample(shares, t)
    print("shares for Lagrange ", ", ".join(str(share) for share in random_shares_select))
    print("Reconstructed secret: ",reconstruct_secret(random_shares_select,t))

def coeff(t, secret):
#Randomly generate a list of coefficients for a polynomial with degree of t - 1, whose constant is secret.
    coeff = [random.randrange(0, limit) for j in range(t - 1)]
    coeff.append(secret)
    print(' is coeff:', str(coeff))
    #polynomial coeff
    return coeff

def generate_shares(n, m, secret):
#Split given secret into n shares with minimum threshold of m shares to recover this secret, using SSS algorithm.
    coefficients = coeff(m, secret)
    #contains polynomial coeff and secret append
    shares = []

    for i in range(0, n):
        x = random.randrange(1, limit)
        print(" gernerate x is ",x)
        shares.append((x, create_polynomial(x, coefficients)))
    #shares= [(5,3),(7,2),(12,6),(30,5),(6,2.5)]
    return shares

def create_polynomial(x, coefficients):

#This generates a single point on the graph of given polynomial in `x`. The polynomial is given by the list of `coefficients`.
    point = 0
    # Loop through reversed list, so that indices from enumerate match the actual coefficient indices
    for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
        print("coefficient index and coefficient value are ", coefficient_index, coefficient_value)
        point += x ** coefficient_index * coefficient_value
        print("x and coefficients and point are ", x, coefficients, point)
    return point

def reconstruct_secret(shares,t):
#Combines individual shares (points on graph)using Lagranges interpolation.

    sum_lagrange = 0
    if len(shares)<t:
        print("Not enough shares. Add ",t-len(shares), " more")

    for j, share_j in enumerate(shares):
        xj, yj = share_j
        print("xj and yj are ",xj, yj)
        prod = Decimal(1)

        for i, share_i in enumerate(shares):
            print("i, share_i ", i, share_i)
            xi, p = share_i
            print("x_i and p are ",xi,p)
            if i != j:
                prod *= Decimal(Decimal(xi)/(xi-xj))
                print("Res ",prod)

        prod *= yj
        print("yj pr ",prod)
        sum_lagrange += Decimal(prod)
        print("sum ",sum_lagrange)

    return int(round(Decimal(sum_lagrange), 0))

if __name__ == '__main__':

    main()
