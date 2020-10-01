"""Rever list by Lucas Trogo
   GitHub: https://github.com/lucastrogo"""
def reverse_list(vet):
    """Reverse linked lists"""
    size_vet = len(vet)
    for pos in range(size_vet // 2):
        i = vet[pos]
        vet[pos] = vet[size_vet - 1 - pos]
        vet[size_vet - 1 - pos] = i