#Using try.except block

print("Practicing for try block")
try:
    numerator = 50
    deno = int(input("enter denominator:"))
    quotient = (numerator/deno)
    print(quotient)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as zero....not allowed")
except ValueError:
    print("Denominator is string....not allowed")
finally:
    print("OUTSIDE try....except block")
