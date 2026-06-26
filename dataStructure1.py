
from collections import Counter

# Dictionary: Book Name -> Number of Borrowings

books = {
    "Object Oriented Programming and Computer Graphics": 30,
    "Data Structures": 35,
    "Operating Systems": 25,
    "Financial Accounting": 20,
    "Digital Electronics and Logic Dersign": 20,
    "Enterprenurship Development": 15,
    "Universal Human Values and Professional Ethics": 10,
    "Community Engagement Projects": 10,
    "Python Programming": 30,
    "Programming with JAVA": 30,
    "Core Python Programming": 10,
    "C++ Programming": 30,   
}

print("  ")
print("Library Borrowing Management System")
print("  ")
# List: Number of books borrowed by each member
member_borrow_counts = [3, 5, 0, 2, 7, 0, 4, 1, 6, 0, 8, 9, 10, 11, 12]

# 1. Compute average number of books borrowed by members
average_borrowed = sum(member_borrow_counts) / len(member_borrow_counts)
print("Average books borrowed per member:", average_borrowed)
print("  ")
# 2. Find book with highest and lowest borrowings
highest_book = max(books, key=books.get)
lowest_book = min(books, key=books.get)

print("\nBook with Highest Borrowings:")
print("  ")
print(highest_book, "->", books[highest_book])
print("  ")
print("\nBook with Lowest Borrowings:")
print("  ")
print(lowest_book, "->", books[lowest_book])
print("  ")
# 3. Count members who have not borrowed any books
zero_borrow_members = member_borrow_counts.count(0)
print("\nMembers who have not borrowed any books:", zero_borrow_members)
print("  ")
# 4. Display the most frequently borrowed book (Mode of borrow counts)
borrow_values = list(books.values())
frequency = Counter(borrow_values)

mode_borrow_count = max(frequency, key=frequency.get)

most_frequent_books = [book for book, count in books.items()
                       if count == mode_borrow_count]

print("\nMode of Borrow Counts:", mode_borrow_count)
print("  ")
print("Most Frequently Occurring Borrow Count Books:")
print("  ")
for book in most_frequent_books:
    print("  ")
    print(book)
print("  ")
