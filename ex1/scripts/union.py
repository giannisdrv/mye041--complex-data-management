#giannis drivas 5216

def is_next_line_unique(file, current_line):

    while True:

        next_line = file.readline()

        if next_line == "" or next_line != current_line:
            
            return next_line

def set_union(r_sorted,s_sorted,joined):

    r_buffer = r_sorted.readline()  
    s_buffer = s_sorted.readline()  

    while r_buffer != "" or s_buffer != "": 
        if r_buffer == "": 
            joined.write(s_buffer)
            s_buffer = s_sorted.readline()
            continue
        if s_buffer == "": 
            joined.write(r_buffer)
            r_buffer = r_sorted.readline()
            continue  

        r_key = r_buffer[0] + r_buffer[1]
        s_key = s_buffer[0] + s_buffer[1]

        r_val = r_buffer[3:-1]
        s_val = s_buffer[3:-1]
        
        if (r_key == s_key):

            
            if (r_val == s_val):              

                joined.write(r_key+"\t"+r_val+"\n")   
                s_buffer = is_next_line_unique(s_sorted, s_buffer)                     
                r_buffer = is_next_line_unique(r_sorted, r_buffer)

            else:        
                if (r_val < s_val):  

                    joined.write(r_key+"\t"+r_val+"\n")   
                    r_buffer = is_next_line_unique(r_sorted,r_buffer)

                else:

                    joined.write(s_key+"\t"+s_val+"\n")
                    s_buffer = is_next_line_unique(s_sorted, s_buffer)

        elif (r_key < s_key):

            joined.write(r_key+"\t"+r_val+"\n")
            r_buffer = is_next_line_unique(r_sorted, r_buffer)

        else:

            joined.write(s_key+"\t"+s_val+"\n")
            s_buffer = is_next_line_unique(s_sorted, s_buffer)

def main():

    input1_path = input("Give the path of the first file: ")
    input2_path = input("Give the path of the second file: ")
    output_path = input("Give the path of the file you want to export the results: ")

    r_sorted = open(input1_path,"r")
    s_sorted = open(input2_path,"r")
    joined = open(output_path,"a")

    set_union(r_sorted,s_sorted,joined)

    r_sorted.close()
    s_sorted.close()
    joined.close()

main()
