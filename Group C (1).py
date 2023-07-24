#Tower of Hanoi

def tower_of_Hanoi(n,source,aux,destination):
    if n == 1:
        print(f"Move disk 1 form{source} to {destination}")
        return
    tower_of_Hanoi(n-1,source,destination,aux)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_Hanoi(n-1,aux,source,destination)
tower_of_Hanoi(3,'A','B','C')