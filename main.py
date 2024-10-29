from avl_tree import *

def main():
    # root of our tree
    root = None

    # let's map first 20 Fibonacci numbers into tree
    keys = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    # setup AVL tree
    for key in keys:
        root = insert(root, key)
    
    # display tree
    print("Tree of Top 20 Fibonacci numbers:")
    print(root)

    # test min search
    min_value_in_tree = get_min(root)
    print(f"Minimum value in Fibonacci tree is {min_value_in_tree}")

    # test max search
    max_value_in_tree = get_max(root)
    print(f"Maximum value in Fibonacci tree is {max_value_in_tree}")

    # test sum calculation
    # note about sum, that's it's not the same as sum of keys, because keys have '1' two times, 
    # but in tree we don't have duplicates
    tree_sum = get_sum(root)
    print(f"Sum of values in Fibonacci tree is {tree_sum}")


if __name__ == '__main__':
    main()