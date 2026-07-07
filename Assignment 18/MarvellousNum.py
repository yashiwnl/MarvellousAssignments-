def chkPrime(num):

  isPrime = True

  if( num < 2):
    isPrime = False

  for i in range(2, num):
    if num % i == 0:
      isPrime = False
      break

    return isPrime
