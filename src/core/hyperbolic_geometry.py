"""
Hyperbolic geometry implementation for portfolio optimization
"""

import numpy as np
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class RobustHyperbolicGeometry:
    """Robust hyperbolic geometry implementation"""
    
    def __init__(self, curvature: float = -0.5, eps: float = 1e-8):
        self.c = curvature
        self.eps = eps
        self.clip_norm = 0.95
    
    def safe_norm(self, x: np.ndarray) -> float:
        return np.linalg.norm(x) + self.eps
    
    def safe_clip(self, x: np.ndarray) -> np.ndarray:
        norm = self.safe_norm(x)
        if norm > self.clip_norm:
            return x * (self.clip_norm / norm)
        return x
    
    def poincare_distance(self, x: np.ndarray, y: np.ndarray) -> float:
        x = self.safe_clip(x)
        y = self.safe_clip(y)
        
        x_norm_sq = np.sum(x * x)
        y_norm_sq = np.sum(y * y)
        diff_norm_sq = np.sum((x - y) ** 2)
        
        denominator = (1 - x_norm_sq) * (1 - y_norm_sq)
        inside = 1 + 2 * diff_norm_sq / (denominator + self.eps)
        inside = max(1.001, min(100.0, inside))
        
        return np.arccosh(inside) / np.sqrt(-self.c)
    
    def frechet_mean(self, points: List[np.ndarray], weights: Optional[List[float]] = None,
                    max_iter: int = 50, lr: float = 0.05) -> np.ndarray:
        if weights is None:
            weights = [1.0 / len(points)] * len(points)
        
        euclidean_mean = np.mean(points, axis=0)
        mean_norm = np.linalg.norm(euclidean_mean)
        mean = euclidean_mean / (mean_norm + self.eps) * 0.8
        
        for iteration in range(max_iter):
            total_grad = np.zeros_like(mean)
            
            for i, point in enumerate(points):
                diff = point - mean
                mean_norm_sq = np.sum(mean * mean)
                scale = 2.0 / (1 - mean_norm_sq + self.eps)
                grad = weights[i] * scale * diff
                total_grad += grad
            
            grad_norm = np.linalg.norm(total_grad)
            if grad_norm < 1e-5:
                break
                
            step_size = lr / (1 + 0.05 * iteration)
            mean = mean + step_size * total_grad
            mean = self.safe_clip(mean)
        
        return mean
