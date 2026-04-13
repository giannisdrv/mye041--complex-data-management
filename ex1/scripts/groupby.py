#giannis drivas 5216

def mergesort(array):

    if len(array) <=1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sortedLeft = mergesort(left)
    sortedRight = mergesort(right)
    
    return merge(sortedLeft,sortedRight)

def merge(left,right):

    res = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        r_key1 = left[i][0:2]
        r_key2 = right[j][0:2]

        if (r_key1 < r_key2):
            res.append(left[i])
            i += 1

        elif (r_key1 > r_key2):
            res.append(right[j])
            j += 1

        else:
            r_val1 = int ((left[i][3:-1]))
            r_val2 = int ((right[j][3:-1]))
            vals_list = [r_val1,r_val2]
            r_sum = sum(vals_list)
            r_sum_string = str(r_sum)
            right[j] = r_key1+"\t"+r_sum_string+"\n"
            res.append(right[j])
            i+=1
            j+=1
            
    res.extend(left[i:])
    res.extend(right[j:])

    return res

def main():
    input_path = input("Give path of the file you want to groupby: ")
    r = open(input_path,"r")

    output_path = input("Give path of the file you want to export the results: ")
    out = open(output_path,"a")

    buffer = r.readlines()
    buffer = mergesort(buffer)

    for line in buffer:
        out.write(line)
        
    r.close()
    out.close()

main()
