#5216 giannis drivas
import sys
import time
import ast


def trf(transactions_array):
    res = {}
    
    for transaction in transactions_array:

        for element in set(transaction):
                if element not in res:
                    res[element] = 0
                res[element] += 1

    return res        

def occ(element, transaction):
    size_of_element_in_transaction = 0

    for elements in transaction:
        if elements == element:
            size_of_element_in_transaction += 1

    return size_of_element_in_transaction          

def rel(transaction, query, transactions_array, trf):
    res = 0

    for elements in set(transaction):
        if elements in query:
            res += occ(elements, transaction) * len(transactions_array) / trf.get(elements)

    return res

def inverted_map(transactions_array):
    res = {}

    for i, transactions in enumerate(transactions_array):

        for elements in transactions:
            if elements not in res:
                res[elements] = set()
            res[elements].add(i)

    return res


def inverted_file_txt(transactions_array, trf, map):
    inverted = open("invfileocc.txt","w")
    for id in sorted(map.keys()):
        occ_of_elem = [] 
        occ_and_map = []
        for transaction in transactions_array:
            temp_res = occ(id,transaction)
            if temp_res > 0:
                occ_of_elem.append(temp_res)

        ordered_map =sorted(list(map.get(id)))
        for i in range(len(map.get(id))):
            occ_and_map.append( [ordered_map[i], occ_of_elem[i]] )

        inverted.write(str(id) + ": " + str(len(transactions_array)/trf.get(id))+ ", " + str(occ_and_map) +"\n")
    
    inverted.close()

def union_of_lists(list_of_lists):
    pointers = [0] * len(list_of_lists)
    res = []
    
    while True:
        min_val = sys.maxsize
        active_lists = 0
        for i in range(len(list_of_lists)):
            if pointers[i] < len(list_of_lists[i]):
                active_lists += 1 
                current_element = list_of_lists[i][pointers[i]]
                if current_element < min_val:
                    min_val = current_element
                    
        if active_lists == 0:
            break     
        
        if not res or min_val != res[-1]:
            res.append(min_val)
            
        for i in range(len(list_of_lists)):
            if pointers[i] < len(list_of_lists[i]) and list_of_lists[i][pointers[i]] == min_val:
                pointers[i] += 1 
        
    return res

def inverted_file(queries_array,inverted_map ,transactions_array,trf,k):
    res = []
    for query in queries_array:
        map_elements = []
        for element in query:
            map_elements.append(inverted_map[element][1])
        union_list = union_of_lists(map_elements)
        for i in range(len(union_list)):
            transaction = transactions_array[union_list[i]]
            rel_res = rel(transaction,query,transactions_array,trf)
            if rel_res > 0:
                res.append([rel_res,union_list[i]])

    res = sorted(res,key=lambda item:item[0], reverse= True)
    return res[:k]

def naive(queries_array, transactions_array, trf, k):
    res = []

    for query in queries_array:
        for id,transaction in enumerate(transactions_array):
            rel_res = rel(transaction, query, transactions_array, trf)
            if rel_res > 0:
                res.append([rel_res, id])

    res = sorted(res,key=lambda item:item[0], reverse= True)
    return res[:k]

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
    k = int(args[4])
    queries_array = []
    trf_res = trf(transactions_array)
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
            result = naive(queries_array, transactions_array, trf_res, k)
            if qnum != "-1":
                print("Naive Method result:\n" + str(result) + "\n")
            print("Naive Method computation time = ",time.time()-start, "\n")
            dic = inverted_map(transactions_array)
            inverted_file_txt(transactions_array,trf_res,dic)
            dic_sorted = list(sorted(dic.items()))
            for i in range(len(dic_sorted)):
                key, value = dic_sorted[i]
                dic_sorted[i] = (key, sorted(list(value)))
            start = time.time()
            result = inverted_file(queries_array,dic_sorted,transactions_array,trf_res,k)
            if qnum != "-1":
                print("Inverted File result:\n" + str(result) + "\n")
            print("Inverted File Computation time = ",time.time()-start, "\n")

        
        case "0":
            start = time.time()
            result = naive(queries_array, transactions_array, trf_res, k)
            if qnum != "-1":
                print("Naive Method result:\n" + str(result) + "\n")
            print("Naive Method computation time = ",time.time()-start)
        
        case "1":
            dic = inverted_map(transactions_array)
            dic_sorted = list(sorted(dic.items()))
            for i in range(len(dic_sorted)):
                key, value = dic_sorted[i]
                dic_sorted[i] = (key, sorted(list(value)))
            inverted_file_txt(transactions_array,trf_res,dic)
            start = time.time()
            result = inverted_file(queries_array,dic_sorted,transactions_array,trf_res,k)
            if qnum != "-1":
                print("Inverted File result:\n" + str(result) + "\n")
            print("Inverted File Computation time = ",time.time()-start)
        
        case default:
            print("Wrong input")
            return

main()
