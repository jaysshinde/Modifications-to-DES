# Differences between the various DES based algorithms<br/>

### 3DES<hr/>
3DES algorithm uses 3 DES algorithms one after the another,the order for encryption<br/>
is ENCRYPT, DECRYPT , ENCRYPT for the 3 algorithms respectively, whereas decryption<br/>
uses DECRYPT, ENCRYPT, DECRYPT for the 3 stages.<br/>

Because this uses 3 consecutive DES algorithms the time taken is significantly higher.<br/>
3 DES provides better security as it uses 3 consecutive keys, thus giving effective key<br/>
length of 168 bits, in another mode 3DES uses 2 keys giving lenght of 112 bits.

### DESnew2<hr/>
DESnew2 uses 2 simultaneously running DES algorithms,each of these algorithms communicate<br/>
with each other and exchange their keys at each round. This leads to an operation time equivalent<br/>
to that of DES but gives an effective key length of 112 bits thus giving more security.

The following image describes this in detail:<br/>
![Algo](https://github.com/jaysshinde/Modifications-to-DES/blob/master/Images/desnew2.png)

