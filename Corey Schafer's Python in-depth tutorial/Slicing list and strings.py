my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#list[start:end:step]

print(my_list[1:-2])
print(my_list[1:])
print(my_list[:])
print(my_list[2:7:2])
print(my_list[-2:5:-2])
print(my_list[::-2])

# Outputs
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 4, 6]
# [8, 6]
# [9, 7, 5, 3, 1]

sample_url = 'www.example.com'
print(sample_url)

# reverse the url
print(sample_url[::-1]) # moc.elpmaxe.www

# print the top level domain
print(sample_url[-4:])  # .com

# print the url without the www
print(sample_url[3:])  # .example.com

