A novel quantitative finance framework that leverages hyperbolic geometry and evolutionary algorithms to achieve superior risk-adjusted returns compared to traditional portfolio optimization methods.

🔬 Research Innovation: First application of hyperbolic multi-agent embeddings for practical portfolio optimization with real-world constraints.

What Makes This Different?
Traditional portfolio optimization (Markowitz) operates in Euclidean space, but financial markets exhibit hierarchical relationships and complex dependencies that are better captured in hyperbolic space.

Key Innovations
Hyperbolic Geometry: Poincaré ball model for natural representation of hierarchical risk-return relationships

Multi-Agent Embeddings: Fuses economic, sentiment, risk, and regime factors as separate agents

Evolutionary Optimization: Robust portfolio selection with real-world constraints

Statistical Validation: Comprehensive backtesting and bootstrap significance testing

Performance Highlights
Metric	Hyperbolic	Markowitz	Improvement
Sharpe Ratio	0.3564	0.2807	+27.0% 
Annual Return	4.84%	2.74%	+76.6% 
Sortino Ratio	0.4571	0.3782	+20.9% 
Calmar Ratio	0.1647	0.1186	+38.9% 
Win Rate	51.74%	50.37%	+1.37% ✅

Quick Start
Installation
bash
git clone https://github.com/yourusername/hyperbolic-portfolio-optimization.git
cd hyperbolic-portfolio-optimization
pip install -r requirements.txt
Basic Usage
python
from hyperbolic_portfolio import HyperbolicPortfolioOptimizer

# Initialize optimizer
optimizer = HyperbolicPortfolioOptimizer()

# Optimize portfolio
result = optimizer.optimize(
    symbols=['SPY', 'GLD', 'TLT', 'AAPL', 'JPM', 'BTC-USD'],
    target_return=0.08,
    max_risk=0.18
)

# Display results
print("Optimal Portfolio Allocation:")
for asset, weight in result.weights.items():
    print(f"  {asset}: {weight:.1%}")

print(f"\nPerformance Metrics:")
print(f"  Sharpe Ratio: {result.sharpe_ratio:.3f}")
print(f"  Expected Return: {result.expected_return:.2%}")
print(f"  Portfolio Diversity: {result.diversity:.1%}")
Advanced Analysis
python
from examples.comprehensive_comparison import run_comprehensive_comparison

# Run full research comparison
results = run_comprehensive_comparison(
    symbols=['SPY', 'GLD', 'TLT', 'AAPL', 'JPM', 'BTC-USD'],
    start_date='2018-01-01',
    end_date='2023-12-31'
)

# Generate publication-quality plots
results.create_visualizations()
📁 Repository Structure
text
hyperbolic-portfolio-optimization/
├──  docs/                    # Research documentation
├──  src/                     # Core implementation
│   ├── core/                  # Hyperbolic geometry & portfolio logic
│   ├── data/                  # Market data fetching & processing
│   ├── optimization/          # Evolutionary algorithms
│   ├── analysis/              # Backtesting & statistical tests
│   └── utils/                 # Configuration & helpers
├── examples/               # Usage examples & demos
├── tests/                  # Comprehensive test suite
├── results/                # Performance results & visualizations
└── config/                 # Configuration files
