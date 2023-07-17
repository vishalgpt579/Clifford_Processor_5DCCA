# CliffALU5 Emulation

5D Conformal Geometric Algebra (or Conformal Clifford Algebra (CCA)) is one of the elegant ways of representing & computing 3D vector space geometry. And the presented approach in [1], utilized few techniques to optimized already existing co-processor for Clifford algebra [2]. Some of the way it do so, are listed in the the section below.

A 5D CCA has 32 blades (basis) (`2^n`, where n=5), unlike its targeted physical 3D Euclidean space, which only has 3 basis (x, y & x), making the generic application such as reflection, rotation, translation or dilation much slower on a traditional CPU or GPU. Hence, the presented ALU5 and other architecture related operand in [1], aims to adjunct GA's intrinsic nature to exhibits CCA's true capabilities, unlike the traditional Linear Algebra(LA) approach, which is represented only by scalar and 1D vectors, GA uses outer-product to get subspace's unique basis, also called as k-blades. 

A multivector is a unit of GA, that is the linear combination of scalar and k-blades(k<=n, n=N-Dimensions) to represent geometry more verbosely. Table-3 from [1] have presented those blades as quadruples & their complement.  

## Objective

A python class object CliffALU5 is created to emulated the ALU presented in [1]. The targeted emulation consists of 

- Lookup table 3 & 4 [1]: 
	- **Complete**
	- Result - **incorrect**

- 7 channel, 32-bit floating for coefficients
	- incomplete
	- Results - N/A

- Instruction Fetch
	- incomplete
	- Results - N/A

- Complete Emulation
	- incomplete
	- Results - N/A

## Lookup Table

- Paper [1] presents table-4, which contains predefined results for all the possible quadruples multiplication.

- The quadruples tables is created as a ordered dictionary. 

- The result table (table-4) is created as a unordered dictionary.

- The class object `ALU.CliffALU5`, load all the tables and has 2 additional function, 
	- Explicit Geometric Multiplication of two multi-vectors(quadruples) using python's `clifford` library for symbolic mathematics operations and blades initialization. 
	- Fetching corresponding result for two quadruples, from the unordered dictionary emulation Table-4.

### Testing

- Initialise the `conda` environment, to safely use/remove any python library without effecting the rest of the system. 
	- `conda activate`

- Launch `test.py`
	- This takes two quadruples, (can be changed from within the script itself),
		- `V_bar = (1^e04) + (2^e14) + (1^e24) + (2^e34)` & `S_bar = (1^e4) + (1^e034) + (1^e134) + (1^e234)`
		- Checks if `V_bar*S_bar == V+T`.




## Reference

1. Franchini, S., Gentile, A., Sorbello, F., Vassallo, G., & Vitabile, S. (2012). Design and implementation of an embedded coprocessor with native support for 5D, quadruple-based Clifford algebra. IEEE transactions on Computers, 62(12), 2366-2381.

2. Gentile, A., Segreto, S., Sorbello, F., Vassallo, G., Vitabile, S., & Vullo, V. (2005, July). CliffoSor: a parallel embedded architecture for geometric algebra and computer graphics. In Seventh International Workshop on Computer Architecture for Machine Perception (CAMP'05) (pp. 90-95). IEEE.