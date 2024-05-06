#tasks for define function 

                                        #1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin
                                    # kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
                                        #mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []

def define(mylist):
    for i in mylist:
        if i >= 0 and (i**(1/2)) % 1 == 0:  
            new_list.append(i)
    print(new_list)

define(mylist)


                             #2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə 
                                        #qaytarsın:   input:[-1,1,2,2,6,7,7,'say']


# input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
# def unique_list(my_list):
#     new_list = []
#     for i in my_list:
#         if my_list.count(i) == 1:  # Əgər ədədin sayı 1dirsə (yəni təkrarlanmıyıbsa)
#             new_list.append(i)
#     return new_list


# result = unique_list(input_list)
# print(result)





                                    #3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# input = [2, 2, 6, 7, 7, 9, 11]

# def multiplication(my_list):
#     hasil = 1
#     if len(my_list) == 0:  # Əgər list boşdursa
#         return hasil  # 1-i geri qaytarır, çünki heç bir ədəd olmadığı üçün hasil 1 olur
#     else:
#         for i in my_list:
#             hasil *= i
#         return hasil

# result = multiplication(input)
# print(result)





                                     #4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın 


# num=36
# bolenler=[i for i in range(1,num+1) if num%i==0]
# print(bolenler)





                                #5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary  
                                        #yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

                                                               #mənim listim
                                                        #mylist=['may','iyun','iyul']
                                                               #bu şəkildə olacaq
                                                        #{'may': 3, 'iyun': 4, 'iyul': 4}


# mylist=['may','iyun','iyul'] 
# month_length = {i: len(i) for i in mylist}
# print(month_length)



                                #6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]  
                                #verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və 
                                    #bunu conprehension ilə edin (əlavə olaraq funksiya da istifadə edəbilərsiz).
                                                  #['rick', 'morty', 'summer', 'jerry', 'beth']



# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# def get_first_names(names):
#     return [name.split()[0].lower() for name in names]

# first_names = get_first_names(names)
# print(first_names)




                                #7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.  
                                                            #nums1 = [1, 2, 3]
                                                            #nums2 = [4, 5, 6]

                                                        #results=[ 2.5, 3.5, 4.5]


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results=[]
# if len(nums1)==len(nums2):
#    for i in range(len(nums1)):
#       ortalama=(nums1[i]+nums2[i])/2
#       results.append(ortalama)
# print(results)