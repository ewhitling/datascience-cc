from statistics import mean


def calculate_residual(y_pred, y_obs):
	return y_pred-y_obs


def calculate_SSR(y_pred, y_obs, deci=4):
	delta = [calculate_residual(a_i, b_i) for a_i, b_i in zip(y_pred, y_obs)]
	return round(sum([d * d for d in delta]), deci)


def calculate_TSS(y_obs, deci=4):
	y_mean = mean(y_obs)
	delta = [y - y_mean for y in y_obs]
	return round(sum([d * d for d in delta]), deci)


def calculate_determination(SSR, TSS, deci=4):
	return round(1-(SSR/TSS), 4)


def fit_line(x_input, y_observed, m_max=5, c_max=5, print_output=True):

	best_model = {
		'm': None,
		'c': None,
		'SSE': None,
		'R^2': None
	}
	assert len(x_input) == len(y_observed), 'Input vectors have differing lengths'

	TSS = calculate_TSS(y_observed)

	for m in range(1, m_max):
		for c in range(0, c_max):
			y_model = list()
			for x_i in x_input:
				y_i = (m*x_i) + c
				y_model.append(y_i)

			SSR = calculate_SSR(y_observed, y_model)
			r2 = calculate_determination(SSR, TSS)
			if print_output:
				print('#####')
				print('using: m=%s and c=%s' % (m, c))
				print('actual: %s' % y_observed)
				print('model: %s' % y_model)
				print('SSE: %s' % SSR)
				print('R^2: %s' % r2)
				print('#####')

			if best_model['SSE'] is None or best_model['SSE'] > SSR:
				best_model['m'] = m
				best_model['c'] = c
				best_model['SSE'] = SSR
				best_model['R^2'] = r2

	return best_model









