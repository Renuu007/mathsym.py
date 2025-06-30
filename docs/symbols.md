# `mathsym`: Supported Symbols

This document lists the mathematical symbols that `mathsym` supports or plans to support. It serves as a reference for users and a goal for development.

*Source for many symbols and names: [RapidTables Math Symbols](https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html)*

## Current Status Legend
- ✅ **Implemented**: The symbol is supported by the runner.
- 🚧 **Planned**: The symbol is a high-priority target for a future release.
- 📝 **Proposed**: The symbol is under consideration and may be complex to implement.

---

## 1. Basic Math
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `+` | Plus | `+` | N/A (Core Operator) |
| `−` | Minus | `-` | N/A (Core Operator) |
| `×` | Times | `*` | 🚧 Planned |
| `·` | Multiplication Dot | `*` | 🚧 Planned |
| `÷` | Division / Obelus | `/` | 🚧 Planned |
| `±` | Plus-Minus | `(a+b, a-b)` | 📝 Proposed |
| `√` | Square Root | `math.sqrt` | ✅ Implemented |
| `∛` | Cube Root | `math.cbrt` | 🚧 Planned |
| `∜` | Fourth Root | `**(1/4)` | 🚧 Planned |
| `²` | Superscript Two | `**2` | ✅ Implemented |
| `³` | Superscript Three | `**3` | ✅ Implemented |
| `ⁿ` | Superscript n | `**n` | 📝 Proposed |
| `⌊x⌋` | Floor | `math.floor(x)` | 🚧 Planned |
| `⌈x⌉` | Ceiling | `math.ceil(x)` | 🚧 Planned |
| `|x|` | Absolute Value| `abs(x)` | 🚧 Planned |

## 2. Relational Operators
| Symbol | Name | Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `=` | Equals | `==` | N/A (Core Operator) |
| `≠` | Not Equal | `!=` | 🚧 Planned |
| `≈` | Approximately Equal | `math.isclose` | 📝 Proposed |
| `>` | Greater Than | `>` | N/A (Core Operator) |
| `<` | Less Than | `<` | N/A (Core Operator) |
| `≥` | Greater Than or Equal| `>=` | 🚧 Planned |
| `≤` | Less Than or Equal | `<=` | 🚧 Planned |
| `≡` | Equivalent to | `==` | 🚧 Planned |
| `≜` | Equal by Definition | `==` | 📝 Proposed |

## 3. Constants
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `π` | Pi | `math.pi` | ✅ Implemented |
| `e` | Euler's Number | `math.e` | 🚧 Planned |
| `τ` | Tau | `math.tau` | 🚧 Planned |
| `∞` | Infinity | `math.inf` | 🚧 Planned |
| `𝐍` | Natural Numbers Set | `(conceptual)` | 📝 Proposed |
| `𝐙` | Integers Set | `(conceptual)` | 📝 Proposed |
| `𝐐` | Rational Numbers Set | `(conceptual)` | 📝 Proposed |
| `𝐑` | Real Numbers Set | `(conceptual)` | 📝 Proposed |
| `𝐂` | Complex Numbers Set | `(conceptual)` | 📝 Proposed |

## 4. Calculus & Analysis
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `d/dx` | Derivative | `(conceptual)` | 📝 Proposed |
| `∫` | Integral | `integrate` | 🚧 Planned |
| `∬` | Double Integral | `integrate2d` | 🚧 Planned |
| `∭` | Triple Integral | `integrate3d` | 🚧 Planned |
| `∮` | Closed Contour Integral | `cintegrate` | 🚧 Planned |
| `∇` | Nabla / Gradient | `grad` | 🚧 Planned |
| `∂` | Partial derivative | `partial` | 🚧 Planned |
| `lim`| Limit | `limit` | 📝 Proposed |

## 5. Linear Algebra
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `·` | Dot Product | `@` or `numpy.dot`| 🚧 Planned |
| `×` | Cross Product | `numpy.cross`| 🚧 Planned |
| `⊗` | Tensor Product | `numpy.tensordot` | 🚧 Planned |
| `Aᵀ`| Transpose | `A.T` or `transpose(A)`| 📝 Proposed (postfix) |
| `A†`| Hermitian Conjugate | `A.conj().T` or `hermitian(A)`| 📝 Proposed (postfix) |
| `det(A)`| Determinant | `numpy.linalg.det(A)` | 🚧 Planned |
| `‖x‖`| Norm | `numpy.linalg.norm(x)` | 🚧 Planned |

## 6. Logic
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `¬` | Not | `not` | 🚧 Planned |
| `∧` | And | `and` | 🚧 Planned |
| `∨` | Or | `or` | 🚧 Planned |
| `⊕` | XOR | `^` | ✅ Implemented (implicitly) |
| `∀` | For All | `(conceptual)` | 📝 Proposed |
| `∃` | There Exists | `(conceptual)` | 📝 Proposed |
| `∴` | Therefore | `(comment only)` | 📝 Proposed |
| `∵` | Because | `(comment only)` | 📝 Proposed |

## 7. Set Theory
| Symbol | Name | Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `∪` | Union | `|` | 🚧 Planned |
| `∩` | Intersection | `&` | 🚧 Planned |
| `∈` | Element of | `in` | 🚧 Planned |
| `∉` | Not an element of | `not in`| 🚧 Planned |
| `⊂` | Proper Subset of | `<` | 🚧 Planned |
| `⊃` | Proper Superset of | `>` | 🚧 Planned |
| `⊆` | Subset or equal to | `<=` | 🚧 Planned |
| `⊇` | Superset or equal to | `>=` | 🚧 Planned |
| `∅` | Empty set | `set()` | 🚧 Planned |
| `A'`| Complement | `U - A` (conceptual)| 📝 Proposed (postfix) |
| `|A|`| Cardinality | `len(A)`| 🚧 Planned |

## 8. Probability & Statistics
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `∑` | Summation | `sum` | 🚧 Planned |
| `∏` | Product | `math.prod`| 🚧 Planned |
| `n!`| Factorial | `math.factorial(n)`| 📝 Proposed (postfix `!`) |
| `P(n,k)`| Permutations | `math.perm(n,k)`| 🚧 Planned |
| `C(n,k)`| Combinations | `math.comb(n,k)`| 🚧 Planned |
| `μ` | Mean | `statistics.mean()` | 🚧 Planned |
| `σ²`| Variance | `statistics.variance()` | 🚧 Planned |
| `σ` | Standard Deviation | `statistics.stdev()` | 🚧 Planned |
| `E(X)`| Expected Value | `E(X)` | 🚧 Planned |

## 9. Geometry
| Symbol | Name | Proposed Python Equivalent | Status |
|:---:|:---|:---|:---:|
| `°` | Degree | `math.radians()`| 📝 Proposed (suffix) |
| `∠` | Angle | `angle()` | 📝 Proposed |
| `∟` | Right Angle | `90` | 📝 Proposed |
| `Δ` | Triangle | `(conceptual)` | 📝 Proposed |

## 10. Greek Alphabet (for variable names)
These will be treated as standard identifiers and will not be replaced. The goal is for `mathsym` to allow them in variable names seamlessly.

| Lower | Upper | Name |
|:---:|:---:|:---|
| `α` | `Α` | Alpha |
| `β` | `Β` | Beta |
| `γ` | `Γ` | Gamma |
| `δ` | `Δ` | Delta |
| `ε` | `Ε` | Epsilon |
| `ζ` | `Ζ` | Zeta |
| `η` | `Η` | Eta |
| `θ` | `Θ` | Theta |
| `ι` | `Ι` | Iota |
| `κ` | `Κ` | Kappa |
| `λ` | `Λ` | Lambda |
| `μ` | `Μ` | Mu |
| `ν` | `Ν` | Nu |
| `ξ` | `Ξ` | Xi |
| `ο` | `Ο` | Omicron |
| `ρ` | `Ρ` | Rho |
| `σ` | `Σ` | Sigma |
| `τ` | `Τ` | Tau |
| `υ` | `Υ` | Upsilon |
| `φ` | `Φ` | Phi |
| `χ` | `Χ` | Chi |
| `ψ` | `Ψ` | Psi |
| `ω` | `Ω` | Omega |

*Note: The large Pi `Π` and Sigma `∑` symbols are used for Product and Summation respectively.*
