def isprime (num):
    for i in range (2,num):
        if num % i ==0:
            print ("nao")
            return
    print("sim")

isprime(289733)