def quadratic(equation):
    x=equation.split("*")
    y=x[3].split("2",1)
    z=x[4].split("x")
    a=int(x[0])
    b=int(y[0])
    c=int(z[1])
    d=(b**2)-(4*a*c)
    sol1=(-b+d**0.5)/(2*a)
    sol2=(-b-d**0.5)/(2*a)
    return sol1,sol2
equation=input("enter the quadratic equation in the form <sign>a*x**2<sign>b*x<sign>c")
print(quadratic(equation))
