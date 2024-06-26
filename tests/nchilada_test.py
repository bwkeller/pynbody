import numpy as np
import numpy.testing as npt
import pytest

import pynbody
import pynbody.test_utils


@pytest.fixture(scope='module', autouse=True)
def get_data():
    pynbody.test_utils.ensure_test_data_available("nchilada")


reference_positions = np.array([[4.80664825e+01, -8.99647751e+01,
                                 3.74038162e+01],
                                [-5.44153690e+00,
                                 1.38918352e+00,  -4.13906145e+00],
                                [-2.14025784e+01,  -
                                 1.36437626e+01,  -9.47246170e+00],
                                [4.10247002e+01,
                                 3.61983910e+01,  -2.48513794e+01],
                                [-5.81032515e+00,
                                 7.98453445e+01,  -7.39464235e+00],
                                [-6.44824982e-01,  -
                                 4.91317129e+00,  -2.40600276e+00],
                                [7.13349762e+01,
                                 8.73891678e+01,  -1.09726463e+02],
                                [-3.53511566e+02,  -1.00286308e+02,
                                 2.75888123e+02],
                                [9.16142178e+00,  -1.18060989e+01,
                                 1.95731199e+00],
                                [1.93871933e+02,
                                 3.49774742e+01,  -3.19205170e+01],
                                [-3.21550280e-01,
                                 9.50274229e-01,  -4.75152826e+00],
                                [2.90328884e+01,   3.98563194e+01,
                                 1.80117950e+01],
                                [8.80027390e+01,
                                 3.49581116e+02,  -9.87488022e+01],
                                [7.49165535e+00,  -3.68064928e+00,
                                 5.22999668e+00],
                                [-4.76786423e+01,  -
                                 8.92267323e+00,  -3.53499756e+01],
                                [-5.13045835e+00,
                                 1.15755057e+00,  -1.24432411e+01],
                                [8.40043869e+01,  -3.09200935e+01,
                                 3.42498322e+01],
                                [8.57449875e+01,  -
                                 1.92537506e+02,  -3.21286072e+02],
                                [3.55517745e-01,  -4.25792408e+00,
                                 2.54480147e+00],
                                [5.06873436e+01,  -1.89251003e+01,
                                 6.30320511e+01],
                                [-2.29010391e+01,  -
                                 2.98745537e+01,  -6.39020443e-01],
                                [1.75614227e+02,
                                 3.88110619e+01,  -4.62935669e+02],
                                [-1.56760117e+02,  -
                                 1.05039883e+01,  -2.15488834e+01],
                                [-1.48337769e+02,  -5.88840103e+01,
                                 5.87665253e+01],
                                [-2.57145252e+01,  -
                                 4.37019272e+01,  -8.64454422e+01],
                                [5.60231543e+00,  -5.63358154e+01,
                                 4.04776115e+01],
                                [4.66480751e+01,  -
                                 1.87408848e+01,  -9.87097397e+01],
                                [6.15837526e+00,  -1.72479401e+01,
                                 1.03489981e+01],
                                [2.07985783e+01,  -1.86683559e+01,
                                 4.93654976e+01],
                                [4.72650070e+01,
                                 2.30763443e+02,  -3.23870850e+02],
                                [-8.57861633e+01,  -
                                 1.02004997e+02,  -6.86018219e+01],
                                [2.02718210e+00,   4.22350769e+01,
                                 1.71071274e+02],
                                [-1.36086855e+01,  -1.44415558e+02,
                                 1.09305428e+02],
                                [5.34043312e+01,  -
                                 8.10125961e+01,  -3.63210640e+01],
                                [-5.14458199e+01,  -1.08560707e+02,
                                 6.31101456e+01],
                                [-6.56126976e+00,   5.70295632e-01,
                                 2.85579300e+01],
                                [5.27915688e+01,  -1.28877045e+02,
                                 1.09167343e+02],
                                [1.01338173e+02,  -1.15229092e+01,
                                 1.33744383e+01],
                                [-1.72840710e+01,
                                 2.39051647e+01,  -1.41212740e+01],
                                [8.56790314e+01,  -5.56587563e+01,
                                 2.17376709e+02],
                                [-8.52479858e+01,  -
                                 9.54728546e+01,  -1.59210297e+02],
                                [-4.44902849e+00,  -3.21001472e+01,
                                 2.00425949e+01],
                                [2.36292999e+02,  -1.47405457e+02,
                                 1.10863857e+01],
                                [1.16263481e+02,  -1.98876991e+01,
                                 4.76252327e+01],
                                [-1.89394855e+01,  -5.57372236e+00,
                                 3.53287201e+01],
                                [3.44844589e+01,   2.32600460e+01,
                                 9.82884674e+01],
                                [9.01199222e-01,
                                 2.57520008e+00,  -5.53647995e-01],
                                [3.16543064e+01,
                                 5.56155300e+00,  -4.71191940e+01],
                                [-9.48117828e+01,  -7.04797745e+01,
                                 1.47528107e+02],
                                [2.11919518e+01,  -6.85180740e+01,
                                 3.07458992e+01],
                                [-1.09558213e+00,  -8.14043903e+00,
                                 1.50014961e+00],
                                [-3.43446732e+00,  -1.12701597e+01,
                                 1.03842316e+01],
                                [-6.20061722e+01,  -1.78703461e+02,
                                 1.55959137e+02],
                                [-7.22693024e+01,  -
                                 4.85273781e+01,  -3.17128677e+01],
                                [1.80612230e+00,  -
                                 2.49209857e+00,  -5.65673053e-01],
                                [7.25562210e+01,   5.13925858e+01,
                                 1.36459608e+01],
                                [9.43354034e+01,  -
                                 1.44577225e+02,  -3.63367615e+01],
                                [-9.77776184e+01,  -1.39123398e+02,
                                 1.63941727e+02],
                                [-5.67525139e+01,
                                 3.34907951e+01,  -1.75442715e+01],
                                [-2.68184853e+00,
                                 2.11684442e+00,  -4.06608544e-02],
                                [-2.96782818e+01,   8.53648376e+01,
                                 4.66984673e+01],
                                [-1.54433002e+01,  -9.27590256e+01,
                                 2.82807068e+02],
                                [-1.11955597e+02,
                                 3.67757835e+01,  -9.62517242e+01],
                                [-2.50878549e+00,
                                 4.25698608e-01,  -9.43133712e-01],
                                [6.53796315e-01,
                                 2.00569868e-01,  -2.51112208e-02],
                                [-1.64453244e+00,
                                 2.01585084e-01,  -9.04290155e-02],
                                [-1.18329549e+00,  -
                                 2.19713300e-02,  -4.17537242e-01],
                                [-6.43875718e-01,
                                 2.19385475e-01,  -4.35074180e-01],
                                [-2.17796063e+00,  -
                                 5.66213965e-01,  -2.24855438e-01],
                                [-2.85428286e+00,  -
                                 6.99547052e-01,  -7.77058899e-02],
                                [-9.91025925e-01,  -3.35044384e-01,
                                 1.01516500e-01],
                                [1.48876154e+00,
                                 1.09505355e+00,  -4.32662398e-01],
                                [5.53907633e-01,
                                 5.82947791e-01,  -3.85044366e-01],
                                [5.44333506e+00,
                                 4.35375547e+00,  -1.00743210e+00],
                                [-8.23547661e-01,
                                 1.96279678e-02,  -5.96994758e-01],
                                [-9.66986239e-01,  -
                                 2.12422982e-02,  -1.02104858e-01],
                                [-9.48075593e-01,   2.02855930e-01,  -7.51522779e-02]])


import pytest


@pytest.fixture
def nchilada_file():
    yield pynbody.load("testdata/nchilada_test/12M.00001")


def test_get(nchilada_file):
    global reference_positions
    positions = nchilada_file['pos'][2998::3000]
    assert (np.abs(positions - reference_positions).mean() < 1.e-6)


def test_get_gas(nchilada_file):
    correct = [ 1.19859905e-07,   8.66461534e-08,
               1.36909285e-03,   2.11048416e-07,   2.63381509e-07,
               2.98710262e-07,   1.08983599e-07,   1.07130404e-07,
               7.49599457e-01,   2.05589359e-07,   1.20924241e-07,
               1.72308305e-07,   1.82599763e-07,   1.91588853e-07,
               1.55311682e-07,   2.24381495e-07,   7.48850703e-01,
               3.63184469e-08,   9.44389882e-08,   1.55873153e-07,
               1.49604929e-07,   1.38858326e-07,   1.57812593e-07,
               1.15718933e-07,   7.49949515e-01,   7.47042358e-01,
               1.99594979e-07,   2.19145448e-07,   6.16430157e-07,
               4.46814852e-07]
    current = nchilada_file.gas['HI'][2998::3000]

    assert (np.abs(current - correct).sum() < 1.e-9)


def test_array_completion_unit_sanity(nchilada_file):
    x_pos_3000 = nchilada_file['pos'][2998::3000]
    del nchilada_file['pos']
    assert 'pos' not in nchilada_file.keys()

    nchilada_file.gas['pos'].convert_units("Mpc")
    nchilada_file.star['pos'].convert_units("pc")

    assert (np.abs(nchilada_file['pos'][2998::3000] - x_pos_3000).mean() < 1.e-2)


def test_partial_loading():
    f_f = pynbody.load("testdata/nchilada_test/12M.00001")

    test_ptcls = [11634,  24181,  26275,  37336,  37795,  38040,  38280,  38327,
                  38524,  39349,  46758,  48892,  52160,  53267,  53745,  68970,
                  78073,  83777,  86865,  93492,  94596,  96567,  99713, 106100,
                  107856, 111036, 111830, 112560, 115082, 117111, 117444, 117667,
                  123604, 123665, 124911, 132957, 138551, 154869, 158919, 182131,
                  184252, 190498, 197946, 198288, 204526, 221720, 226375, 226915,
                  229959, 231778]  # randomly generated sample

    f_p = pynbody.load("testdata/nchilada_test/12M.00001", take=test_ptcls)

    assert((f_p['pos'] == f_f['pos'][test_ptcls]).all())

def test_HI_not_present_for_non_gas_particles():
    fresh_f = pynbody.load("testdata/nchilada_test/12M.00001")
    with pytest.raises(KeyError):
        fresh_f['HI']

    with pytest.raises(KeyError):
        fresh_f.dm['HI']

    # correct value of f.gas['HI'] is tested above
