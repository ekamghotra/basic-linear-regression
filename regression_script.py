from numpy import *

def compute_error_for_line_given_points(b, m, points):
    # initialize error at zero
    totalError = 0

    # for every point
    for i in range(0, len(points)):
        # get x value
        x = points[i, 0]
        # get y value
        y = points[i, 1]
        # get the difference, square it, and add it to the total
        totalError += (y - (m * x + b)) ** 2
    
    # get the average
    return totalError / float(len(points))

# main gradient descent calculation
def step_gradient(b_current, m_current, points, learningRate):
    # starting points for our gradient
    b_gradient = 0
    m_gradient = 0

    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # direction with respect to b and m
        # computing partial derivitives of our error function (gives us our direction)
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    
    # update our b and m values using our partial derivatives
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)

    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    # starting b and m value
    b = starting_b
    m = starting_m
    
    # gradient descent
    for i in range(num_iterations):
        # update b and m with the new more accurate b and m by performing this gradient step
        b, m = step_gradient(b, m, array(points), learning_rate)
    
    return [b, m]


def run():
    # Step 1 - collect data
    points = genfromtxt('data.csv', delimiter=',')

    # Step 2 - define hyperparameters
    # Learning rate below is defining how fast our model should converge
    learning_rate = 0.0001
    # y = mx + b (formula), and below we are setting the initial b and m values
    initial_b = 0
    initial_m = 0
    # Small dataset so only iterating 1000 times
    num_iterations = 1000

    # Step 3 - Train model
    print ('starting gradient descent at b = {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))

    [b, m]= gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)

    print ('ending point at b = {1}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))


if __name__ == '__main__':
    run()