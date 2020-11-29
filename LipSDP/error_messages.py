import math


def comb(n: int, k: int) -> int:
    if k <= n:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    else:
        return 0


def cap_input(input_num, N, type):
    # Caps number of a quantity (rand_num_neurons or num_dec_vars) to 
    # N choose 2 and prints information to user
    #
    # params:
    #   * input_num: int - input quantity: rand_num_neurons or num_dec_vars
    #   * N: int         - total number of hideen neurons in neural network
    #   * type: str      - name of input_num to print to user
    #
    # returns:
    #   * input_num: int - capped input number if quantity is over limit
    #                      otherwise, the original quantity is returned
    # ---------------------------------------------------------------------

    if input_num > comb(N, 2):
        print('[INFO]: Capping number of ', type, ' to ', str(comb(N, 2)), '.', sep='')
        print('[INFO]: Your network has ', str(N), ' hidden neurons and this', sep='')
        print('[INFO]: only allows for (', str(N), ' choose 2) = ',
              str(comb(N, 2)), ' ', type, '.', sep='')
        input_num = comb(N, 2)

    return input_num


def invalid_mode(mode):
    # Error message for invalid mode - should already be caught in Python
    #
    # params:
    #   * mode: str - formulation for LipSDP supplied by user
    # ---------------------------------------------------------------------

    error_msg = ('[ERROR]: formulation must be in ' +
                '["neuron", "network", "layer", "network-rand", "network-dec-vars"]\n' +
                '[ERROR]: You supplied formulation = ' + mode
                )
    raise ValueError(error_msg)
