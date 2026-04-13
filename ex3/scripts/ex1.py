#5216 giannis drivas
import sys
import time
import ast

def naive(transactions_array, queries_array):
    result = []

    for queries in queries_array:
        counter = 0

        for transactions in transactions_array:
            is_subset = set(queries).issubset(set(transactions))
            if is_subset:
                result.append(counter)
            counter += 1

    return set(result)

def sigfile_bitmap(transactions_array):
    res = []

    for transactions in transactions_array:
        transactions = set(transactions)
        temp = 0x0
        for elements in transactions:
            temp = temp ^ (0x1 << elements)

        res.append(temp)
    print(res[0])
    return res

def sigfile_txt(array):

    sigfile = open("sigfile.txt","w")
    print(array[0])
    for lines in array:
        sigfile.write(str(lines)+"\n")

    sigfile.close()

def exact_signature_file(queries_array, bits):
    res = []
    bit_map_queries = sigfile_bitmap(queries_array)

    for queries in bit_map_queries:
        counter = 0

        for transactions in bits:
            res_and = queries & transactions
            if  res_and == queries:
                res.append(counter)
            counter += 1

    return set(res)

def bitslice_bitmap(transactions_array):
    res = {}

    for i, transactions in enumerate(transactions_array):
        transactions = set(transactions)

        for elements in transactions:
            if elements not in res:
                res[elements] = 0x0
            res[elements] = res[elements] ^ (0x1<<i)
    print(res)
    return res


def bitslice_text(transactions_array):

    bitslice = open("bitslice.txt","w")

    for elements,bit in sorted(transactions_array.items()):
        bitslice.write(str(elements)+":"+str(bit)+"\n")
    
    bitslice.close()

def exact_bitslice_signature_file(queries_array,bits):
    res = []

    for query in queries_array:

        query_bitmap = []

        for element in query:
            query_bitmap.append(bits.get(element))

        res_and = -1

        for bitmap in query_bitmap:
            if res_and == -1:
                res_and = bitmap
            else:
                res_and &= bitmap

        counter = 0

        while res_and > 0:
            if res_and & 1:
                res.append(counter)
            res_and >>= 1
            counter += 1

    return set(res)

def inverted_map(transactions_array):
    res = {}

    for i, transactions in enumerate(transactions_array):

        for elements in transactions:
            if elements not in res:
                res[elements] = set()
            res[elements].add(i)

    return res

def inverted_txt(transactions_array):

    inverted = open("invfile.txt","w")

    for id,map in sorted(transactions_array.items()):
        inverted.write(str(id) + ": " + str(sorted(list(map)))+"\n")

    inverted.close()

def inverted_file(queries_array, map):
    res = []

    for query in queries_array:
        query_map = []

        for element in query:
            query_map.append(list(sorted(map.get(element))))
    
        pointers = [0] * len(query_map)

        while True:
            current_numbers = []
            break_while = True

            for i in range(len(query_map)):
                if pointers[i] < len(query_map[i]):
                    current_numbers.append(query_map[i][pointers[i]])
                else:
                    break_while = False
                    break
                    
            if break_while == False:
                break    

            max_number = max(current_numbers)
            same_cur_number = True

            for numbers in current_numbers:
                if numbers != max_number:
                    same_cur_number = False
                    break
            
            if same_cur_number:
                res.append(max_number)

                for i in range(len(query_map)):
                    pointers[i] += 1

            else:

                for i in range(len(query_map)):
                    if query_map[i][pointers[i]] < max_number:
                        pointers[i] += 1

    return set(res)

def main():
    
    args = sys.argv[1:]
    transactions = open(args[0],"r")
    transactions_array = []

    for lines in transactions:
        lines = lines.strip()
        transactions_array.append(ast.literal_eval(lines))

    queries = open(args[1],"r")
    

    qnum = args[2]
    method = args[3]
    queries_array = []

    match qnum:

        case "-1":
            for lines in queries:
                lines = lines.strip()
                queries_array.append(ast.literal_eval(lines))

        case default:
            counter = 0

            for lines in queries:
                if counter == int(default):
                    lines = lines.strip()
                    queries_array.append(ast.literal_eval(lines))
                    break
                else:
                    counter +=1

    match method:

        case "-1":
            start = time.time()
            naive(transactions_array, queries_array)
            print("Naive Method computation time = ",time.time()-start)

            
            bits = sigfile_bitmap(transactions_array)
            start = time.time()
            sigfile_txt(bits)
            exact_signature_file(queries_array, bits)
            print("Signature File computation time = ",time.time()-start)
            
            bits = bitslice_bitmap(transactions_array)
            #print(bits)
            #sigfile_txt(bits)
            start = time.time()
            exact_bitslice_signature_file(queries_array, bits)
            print("Bitsliced Signature File computation time = ",time.time()-start)

            map = inverted_map(transactions_array)
            bitslice_text(bits)
            start = time.time()
            inverted_file(queries_array, map)
            print("Inverted File Computation time = ",time.time()-start)

        case "0":
            start = time.time()
            result = naive(transactions_array, queries_array)
            print("Naive Method result:\n" + str(result) + "\n")
            print("Naive Method computation time = ",time.time()-start)

        case "1":
            
            bits = sigfile_bitmap(transactions_array)
            sigfile_txt(bits)
            start = time.time()
            result = exact_signature_file(queries_array, bits)
            print("Signature File result:\n" + str(result) + "\n")
            print("Signature File computation time = ",time.time()-start)

        case "2":
            bits = bitslice_bitmap(transactions_array)
            bitslice_text(bits)
            start = time.time()
            result = exact_bitslice_signature_file(queries_array,bits)
            print("Bitsliced Signature File result:\n" + str(result) + "\n")
            print("Bitsliced Signature File computation time = ",time.time()-start)
        case "3":
            map = inverted_map(transactions_array)
            inverted_txt(map)
            start = time.time()
            result = inverted_file(queries_array, map)
            print("Inverted File result:\n" + str(result) + "\n")
            print("Inverted File Computation time = ",time.time()-start)
        case default:
            print("Wrong input of method argument")
            return



    transactions.close()

main()
