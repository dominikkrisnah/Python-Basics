# PENGENALAN STRING

data = "halo dunia"
print(data,type(data))

# cara membuat string
'''
    1. membuat string dengan single quote ('...')
    2. membuat string dengan double quote ("...")
'''
data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

## menggunakan item double string
print('"Halo Alam Semesta"')
print("'Halo Alam Semesta'")
print("Hai Krisna Herlam'bang")
## menggunakan tanda \, sehingga membuat tanda (') menjadi string
print('ayo kita bermain di hari jum\'at yang cerah ini\n')
print('g\'day, isn\'t it?\n')
## backlash
print("C:\\user\\Dominik")
## tab
print("Dominik\t\t\t\tKrisna")
## backspace
print("Dominik \bKrisna\n")
## newline
print("baris pertama.\nbaris kedua.\n") # LF -> line feed : unix, linux, macos
print("baris pertama.\rbaris kedua.\n") # CR -> carriage return : commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua\n") # CRLF -> line feed carriage return : windows

## String literal atau RAW string
### RAW string membuat semua item menjadi string
print(r'C:\new filder')
## multiline literal string
print("""
Nama : Krisna
Pendidikan : S2
""")
## multiline literal string dan RAW
print(r"""
Name : Krisna
Pendidikan : S2
Website : www.krisna.ac.id/newID
""")