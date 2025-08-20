def my_function(x):
    return 2*x**2 - 45*x + 7

def derivative(x, my_function , epsilon = 0.00001):
    return (my_function(x + epsilon) - my_function(x))/(epsilon)

def approximation_t(t):
    return t - derivative(t, my_function, epsilon)/(derivative(t, derivative(t, my_function, epsilon), epsilon))

def optimize():
    differecnce = approximation_t(x_0)
    epsilon = 0.01
    while difference > threshold:
        x_0 = x_0 + epsilon
        difference = approximation(x_0)
    return approximation(x_0)