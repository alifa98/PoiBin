import pytest
from poisson_binomial import PoissonBinomial

def test_method():
    instance = PoissonBinomial()
    assert instance.method() == "result"
