# CodeCraft
* This is the my course from mlzoomcamp:

* [0. Introduction](https://github.com/haniyrasul/CodeCraft/blob/main/ML_ZoomCamp/1.%20Introduction/1.%20Introduction.md):
  * Introdcution: Numpy, Linear Algebra, Pandas
 
* [1. Regression](https://github.com/haniyrasul/CodeCraft/tree/main/ML_ZoomCamp/2.%20Regression)
  * Linear Model: <br>
  $g(X_i) ≈ y_i$ <br>
  $X_i = (X_{i1}, X_{i2}, ..... , X_{in})$ <br>
  $g(X_i) = W_0 + W_1.X_{i1} + W_2.X_{i2} + ...... + W_n.X_{in}$ <br>
  $W_0 \rightarrow Bias$ <br>
  -------------------------------------------------
  $g(X_i) = W_0 + W_1.X_{i1} + W_2.X_{i2} + W_3.X_{i3}$ <br>
  $g(X_{i}) = W_0 + \sum_{j=1}^{3} W_j.X_{ij}$ <br>
  -------------------------------------------------
  * Matrix Convertion: <br>
  $X.w = y \rightarrow w = X^{-1}.y$$<br>
  $X^T.X.w = X^T.y $$<br>
  $X^T.X \rightarrow Gram\ Matrix, Has\ Inverse\ $$<br>
  -------------------------------------------------
  $w = I.w =  (X^T.X)^{-1}.X^T.y $$<br>
  $RMSE (Root Mean Squre Error)<br>
  $\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (g(X_i) - y_i)^2}$<br>
