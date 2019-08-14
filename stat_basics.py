'''basic essentials'''
#from scipy.spatial import distance
from matplotlib import pyplot as plt

def euclidean_distance(pt1, pt2):
	#distance.euclidean(pt1, pt2)
	return sum([(pt1[n] - pt2[n])**2 for n in range(len(pt1))])**0.5

def manhattan_distance(pt1, pt2):
	#distance.cityblock(pt1, pt2)
	return sum([abs(pt1[n] - pt2[n]) for n in range (len(pt1))])

def hamming_distance(pt1, pt2, percentage = True):
	#distance.hamming(pt1, pt2)
	dist  = len([True for n in range(len(pt1)) if pt1[n] != pt2[n]])
	return dist/len(pt1) if percentage else dist


def print_distances(sets, funcs):
	for s in sets:
		if len(s[0]) == len(s[1]):
			print('\nset:', *s)
			for name, func in funcs.items():
		  		print('\t',name, func(*s))


#visualize
dataset = ([3,6], [8,0]), ([8,9,11], [6,9,14]), ([1,2], [2,100]), ([8,9,11], [6,9,14])
distances = {'euclidean: ': euclidean_distance,
		 'manhattan: ' : manhattan_distance,
		 'hamming: ' : hamming_distance}

print_distances(dataset, distances)
print()


def line_eq(data, m, b):
	#y = mx + b (y = slope * x + intercept of y)  =  0 * x + b  =  0 + b  =  b
	return [m*x + b for x in data]

def total_loss(data, test_data, m, b):
	#find how bad the model prediction is
	line = line_eq(data, m, b)
	loss = 0
	for i in range (len(line)):
		loss += (test_data[i] - line[i])**2
	return loss

def datafit(data, test_data, mset, bset):
	#select best m and b values
	dataset = {}
	for m in range(len(mset)):
		for b in range(len(bset)):
			dataset[total_loss(data, test_data, m, b)] = m, b
	imin = min(dataset)
	return dataset[imin], imin


#gradient descent for intercept
def get_gradient_at_b(x,y, b, m):
        diff = sum([y[i] - (m*x[i]+b) for i in range(len(x))])
        b_gradient = -2/len(x) * diff
        return b_gradient

#gradient descent for slope
def get_gradient_at_m(x, y, b, m):
        diff = sum([x[n] * (y[n] - (m * x[n] + b)) for n in range(len(x))])
        m_gradient = -2/len(x) * diff
        return m_gradient

def step_gradient(b_current, m_current, x, y, learning_rate):
	b_gradient = get_gradient_at_b(x, y, b_current, m_current)
	m_gradient = get_gradient_at_m(x, y, b_current, m_current)
	b = b_current - (learning_rate * b_gradient)
	m = m_current - (learning_rate * m_gradient)
	return b, m

def gradient_descent(x, y, learning_rate, num_iterations):
	b,m = 0,0
	for num in range(num_iterations):
		b,m = step_gradient(b,m, x,y, learning_rate)
	return b,m

def plot_gradient(ds1, ds2, learning_rate = 0.01, iterations = 1200):
        b,m = gradient_descent(ds1, ds2, learning_rate, iterations)
        y = [m*x + b for x in ds1]
        plt.plot(ds1, ds2, "o")
        plt.plot(ds1, y)
        plt.show()        

months = [month for month in range(1,13)]
revenue = [2200, 700, 1500, 2400, 2200, 1600, 900, 300, 2200, 1800, 2400, 2000]

plot_gradient(months, revenue)

