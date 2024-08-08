> ⚠️ **Warning:** This project is not finished yet.

# Poisson Binomial Distribution

This is a package for the Poisson Binomial Distribution. The Poisson Binomial Distribution is a generalization of the Binomial Distribution. The Binomial Distribution is the distribution of the number of successes in a fixed number of independent Bernoulli trials. The Poisson Binomial Distribution is the distribution of the number of successes in a fixed number of independent Bernoulli trials with different success probabilities.

## Installation

You can install the package using pip:

```bash
pip install poibin
```

## Usage

The package provides a class `PoissonBinomial` that can be used to calculate the probability mass function (PMF) and the cumulative distribution function (CDF) of the Poisson Binomial Distribution. The class takes a list of success probabilities as input and provides methods to calculate the PMF and CDF.

### Example

Here is an example of how to use the `PoissonBinomial` class:

```python
from poisson_binomial import PoissonBinomial

# List of success probabilities
p = [0.1, 0.2, 0.3, 0.4, 0.5]

# Create a PoissonBinomial object
pb = PoissonBinomial(p)

# Calculate the PMF
pmf = pb.pmf(2)

# Calculate the CDF
cdf = pb.cdf(2)

# Mean:
mean = pb.mean()

# Variance:
variance = pb.variance()

```
