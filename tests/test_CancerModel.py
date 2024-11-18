import unittest
from cancer_prediction.cancer_model import CancerModel
class TestCancerModel(unittest.TestCase):

    def test_target_to_diagnoisis(self):
        model = CancerModel()
        target = model.diagnosis_to_target("Benign")
        assert target == 1

        target = model.diagnosis_to_target("Malignant")
        assert target == 0

if __name__ == '_main_':
    unittest.main()
        




