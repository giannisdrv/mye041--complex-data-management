#giannis drivas 5216

def merge_join(r_sorted,s_sorted,joined):

    r_buffer = r_sorted.readline()  
    s_buffer = s_sorted.readline()  
    last_val_buffer = []       
    last_val_buffer_size = 0   

    while r_buffer != "" or s_buffer != "": 
        if r_buffer == "":  
            break
        if s_buffer == "": 
            break 

        r_key = r_buffer[0]+ r_buffer[1]    
        s_key = s_buffer[0] + s_buffer[1]   

        if (r_key == s_key):        

            joined.write(r_key+"\t"+r_buffer[3:-1]+"\t"+s_buffer[3:-1]+"\n")
            last_val_buffer.append(s_buffer)   
            s_buffer = s_sorted.readline()

        elif (r_key < s_key):                      

            last_val_buffer_size = max(last_val_buffer_size,len(last_val_buffer)) 
            r_buffer = r_sorted.readline()

            if (r_buffer != ""):       

                temp_r =r_buffer[0] + r_buffer[1] 

                if (temp_r == r_key):    

                    for vals in last_val_buffer:    
                        joined.write(temp_r+"\t"+r_buffer[3:-1]+"\t"+vals[3:-1]+"\n")    

                    last_val_buffer.clear()             
                    r_buffer = r_sorted.readline()
        else:

            s_buffer = s_sorted.readline()

    return last_val_buffer_size

def main():

    input1_path = input("Give the path of the first file: ")
    input2_path = input("Give the path of the second file: ")
    output_path = input("Give the path of the file you want to export the results: ")

    r_sorted = open(input1_path,"r")
    s_sorted = open(input2_path,"r")
    joined = open(output_path,"a")

    print ("max buffer size is: "+ str(merge_join(r_sorted,s_sorted,joined)))
    
    r_sorted.close()
    s_sorted.close()
    joined.close()

main()
