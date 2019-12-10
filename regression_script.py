
def calculate_residuals(y_act, y_pred, deci=4):
    delta = [a_i - b_i for a_i, b_i in zip(y_act, y_pred)]
    return round(sum([d * d for d in delta]), deci)


def fit_line(x_input, y_actual, m_max=5, c_max=5, print_output=True):

    best_model = {
        'm': None,
        'c': None,
        'SSE': None
    }
    assert len(x_input) == len(y_actual), 'Input vectors have differing lengths'

    for m in range(1, m_max):
        for c in range(0, c_max):
            y_model = list()
            for x_i in x_input:
                y_i = (m*x_i) + c
                y_model.append(y_i)

            SSE = calculate_residuals(y_actual, y_model)
            if print_output:
                print('#####')
                print('using: m=%s and c=%s' % (m, c))
                print('actual: %s' % y_actual)
                print('model: %s' % y_model)
                print('SSE: %s' % SSE)
                print('#####')

            if best_model['SSE'] is None or best_model['SSE'] > SSE:
                best_model['m'] = m
                best_model['c'] = c
                best_model['SSE'] = SSE

    return best_model


x = [1, 2, 3, 4, 5, 6]
y = [2.11, 3.87, 6.01, 7.93, 9.99, 12.12]

my_model = fit_line(x, y, print_output=False)
print('best model: %s' % my_model)