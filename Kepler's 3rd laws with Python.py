#Dengan ketentuan anda tidak boleh menggunakan perpangkatan dengan menggunakan math library maupun dengan menggunakan operasi perhitungan perpangkatan di python 
#seperti x*y atau xx*x diluar inner function. Disini, anda diwajibkan untuk membuat function perpangkatan dengan ketentuan sebagai berikut:

#1. Function perpangkatan memiliki 2 parameter (n,p) yang dimana n sebagai angka dan p sebagai jumlah pangkatnya. Misal perpangkatan(2,3) akan me-return 8.
#2. Terdapat error handling jika nilai n dan p yang diinput bukan merupakan digit angka alias diharuskan membuat error handling jika nilai n dan p adalah character.
#3. Diharuskan pada function perpangkatan didalamnya terdapat inner function yang didalam inner function terdapat kalkulasi perpangkatan. 
#Didalam inner function ini, anda dibolehkan menggunakan operasi hitung python untuk perpangkatan seperti n**p.
#4. Jika anda berhasil menggunakan operasi rekursif seperti menghitung factorial pada Percobaan 1 di atas, anda akan mendapat poin tambahan.

def power(n,p):
  #Disini isikan error handling jika user memasukkan inputan selain angka
  if not type(n) is int:
    error = "Error"
    return error
  if not type(p) is int:
      error = "Maaf, inputan harus angka."
      return error

  else:
    def inner_power(n , p):
      if p == 0:
        return 1
      else:
        return n * inner_power(n , p - 1) #Masukkan kalkulasi perpangkatan disini
    return inner_power(n , p)
    
def kepler():
  try:
    T2 = power("ups" , 2)
    R1 = power(2 , "wow")
    R2 = power(4 , 3)
    T1square = T2 / R2 * R1  
    #Disini masukkan perhitungan T1 kuadrat sesuai dengan rumus hukum 3 kepler diatas.
    return T1square
  except:
    return power('','')

print(kepler())

#Test case 1:
#Input:
#R1 = n: 2 p: 3 -> arti dari berikut ini adalah nilai input n dan p masing-masing untuk R1, sehingga n**p = 2**3 = 8
#R2 = n: 4 p: 3 -> arti dari berikut ini adalah nilai input n dan p masing-masing untuk R2, sehingga n**p = 4**3 = 64, begitu seterusnya
#T2 = n: 3 p: 2
#Output: T1square = 1.125

#Test case 2:
#Input:
#R1 = n: "Ups" p: 3 
#R2 = n: 4 p: "Wow" 
#T2 = n: "Ups" p: "Wow"
#Output: ERROR

#Test case 3:
#Input:
#R1 = n: 3 p: 3 
#R2 = n: 3 p: 0 
#T2 = n: 0 p: 0
#Output: T1square = 27