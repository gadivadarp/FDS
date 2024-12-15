def delete_duplicates(books):
    
    return list(set(books))

def sort_books(books):

    return sorted(books)

def count_expensive_books(books, threshold=500):
 
    return sum(1 for cost in books if cost > threshold)

def copy_less_cost_books(books, threshold=500):
    
    return [cost for cost in books if cost < threshold]

# Input List of Book Costs
books = [450, 300, 600, 500, 450, 700, 350, 800, 600]


print("1) Unique Books (Duplicates Removed):", delete_duplicates(books))
print("2) Books Sorted by Cost:", sort_books(books))
print("3) Count of Books with Cost > 500:", count_expensive_books(books))
print("4) Books with Cost < 500 in New List:", copy_less_cost_books(books))
