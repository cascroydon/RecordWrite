# RecordWrite
an example of reading and writing records into a binary data file in Python

## What does it do?
This program creates a data file of 100 records. Each record contains a single 32 bit integer value representing a user id, and a 20 character string of bytes representing a password.

It then writes a couple of records into the file. Then it overwrites the second record. Finally, it displays the contents of the second record.

## How does it work?
The program uses the `struct` library to encode and decode the Python data into binary. It uses the file io library to read and writes bytes into the data file.

The layout of the data structure is defined by this object `Struct("i 20s")`. The lower case `i` represents a signed 32 bit integer value. And `20s` represents a 20 byte character string.

Python string need to be encoded into binary format before they can be packed into the binary data structure. This is why the `pack()` method of the `Record` class uses the `encode()` method. Similarly, when a record is unpacked from binary it has to be converted back into a Python string with the `decode()` method.

The file mode `"wb"` tells Python to create a binary file. The mode `"r+b"` opens the file in binary mode and allows writing without truncating the file. And finally, the mode `"rb"` opens the file in binary mode for reading.

When a file is first opened in any of these modes, it is open at the beginning of the file. The `seek()` method allows Python to move some number of bytes through the file which allows it to read or write from anywhere within the file.
