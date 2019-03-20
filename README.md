
# The Design and Implementation of a Symmetric Encryption Algorithm Based on DES

<hr/>

### Members:

Jay Satish Shinde 16CO118<br/>
Ayush Kumar 16CO208

### Implementation Details
The project was implemented in parts: <br/>
1. Pure python implementation of DES.
2. Implementation of 3DES using DES.
3. Implementation of new DES algorithm(s).
4. Comparison of performances of the algorithms from the perspective of 
    operational efficiency.
5. Producing graphical outputs to make observations clearer.

### File Structure
1. DES.py - Implementaion of DES
2. ThreeDes.py - Implementaion of 3DES
3. DESnew2.py - Implementation of DESnew2 as specified in the paper.
4. DES_paramterised.py - Paramterised DES to run n rounds.
5. 3DES_paramterised.py - Paramterised 3DES to run n rounds.
6. DESnew2_parameterised.py - Paramterised DESnew2 to run n rounds.
7. Differences.md - Differences between DES based algorithms.


### Results
![Tabular Result](https://github.com/jaysshinde/Modifications-to-DES/blob/master/Images/Table.png)<br/>
Comparison in times taken for the algorithms

![Graphical Result](https://github.com/jaysshinde/Modifications-to-DES/blob/master/Images/Graph.png)<br/>
Overall comparison in performance

### Conclusion
The results obtained demonstrate that even though 3DES improves upon the security<br/>
issues of DES, the operational time of 3DES is very high, in our results the running time<br/>
of 3DES on an average was as high as 2 to 2.5 times.<br/>

In comparison DESnew2 also improves upon the security flaws of DES by using a key which<br/>
has an effective length of 112 bits. DESnew2 does this, and at the same time retains<br/>
the operational efficiency of DES, this algorithm takes almost the same time on average.<br/>



