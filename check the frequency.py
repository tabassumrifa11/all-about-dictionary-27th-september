print("\033c")

test_dict = {
    'Codingal' : 5,
    'is' : 2,
    'best' : 2,
    'for' : 2,
    'coding' : 1,
}


print("The original dictionary:" , test_dict)


k= int(input("Enter the Frequency:"))

res = 0

for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
        
        
print("Frequency of k is:"  , res)