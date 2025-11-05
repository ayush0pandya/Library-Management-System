# main.py
from books import Book
from library import library
from member import Member
from exception import (
    WrongTitleError, WrongAuthorError, WrongDateError,
    searchError, BookRemovalError, BookRetrivalError
)

def seed_books():
    """Create a small, valid catalog."""
    return [
        Book(1949, 6, 8,  author="George Orwell",            title="1984"),
        Book(1997, 6, 26, author="J.K. Rowling",             title="Harry Potter and the Philosopher's Stone"),
        Book(1813, 1, 28, author="Jane Austen",              title="Pride and Prejudice"),
        Book(1954, 7, 29, author="J.R.R. Tolkien",           title="The Fellowship of the Ring"),
        Book(2011, 7, 12, author="George R. R. Martin",      title="A Dance with Dragons"),
    ]

def print_inventory(lib: library, header: str = "Current Library Inventory"):
    print(f"\n=== {header} ===")
    if not any(True for _ in lib):
        print("(empty)")
        return
    for i, b in enumerate(lib, start=1):
        # rely on Book.__str__ if defined; otherwise print key fields
        try:
            print(f"{i}. {b}")
        except Exception:
            print(f"{i}. {getattr(b, 'title', 'Unknown Title')} by {getattr(b, 'author', 'Unknown Author')} "
                  f"({getattr(getattr(b, 'publishing_date', None), 'year', 'Unknown Year')})")

def demo_validators():
    """Intentionally trigger your validators so you can see the custom errors still work."""
    print("\n=== Validator Demo (intentional errors) ===")
    tests = [
        ("Bad title chars",    lambda: Book(2021, 1, 1, author="Tester",      title="My@Book")),
        ("Too long title",     lambda: Book(2020, 1, 1, author="Tester",      title="T" * 60)),
        ("Too long author",    lambda: Book(2020, 1, 1, author="B" * 60,      title="Some Book")),
        ("Invalid date",       lambda: Book(2021, 2, 30, author="Tester",     title="Invalid Date Book")),
    ]
    for label, fn in tests:
        try:
            fn()
        except (WrongTitleError, WrongAuthorError, WrongDateError) as e:
            print(f"{label} → {e}")

def main():
    # 1) Create a library
    lib = library()

    # 2) Seed some books and add them to the library
    for bk in seed_books():
        lib.addbook(bk)
    print_inventory(lib, "After Seeding")

    # 3) Create two members (make sure the emails are valid per email_validator in member.py)
    alice = Member(name="Alice", age=25, email="alice@example.com", library_id=1)
    bob   = Member(name="Bob",   age=22, email="bob@example.com",   library_id=2)

    # 4) Borrow/Return flow
    # Alice borrows the first book
    first_book = next(iter(lib))
    alice.borrow_book(first_book, lib)
    print("\nAlice borrowed one book.")
    print_inventory(lib, "After Alice Borrow")

    # Bob tries to borrow the same book (should raise searchError)
    try:
        bob.borrow_book(first_book, lib)
    except searchError as e:
        print(f"\nExpected borrow failure for Bob → {e}")

    # Alice returns it
    alice.return_book(first_book, lib)
    print("\nAlice returned the book.")
    print_inventory(lib, "After Return")

    # 5) Searches
    try:
        found_title = lib.search_by_title("1984")
        print(f"\nSearch by title '1984' → {len(found_title)} match(es).")
    except searchError as e:
        print(f"\nSearch by title failed → {e}")

    try:
        found_author = lib.search_by_author("Rowling")
        print(f"Search by author 'Rowling' → {len(found_author)} match(es).")
    except searchError as e:
        print(f"Search by author failed → {e}")

    try:
        found_year = lib.search_by_year(1949)
        print(f"Search by year 1949 → {len(found_year)} match(es).")
    except searchError as e:
        print(f"Search by year failed → {e}")

    # 6) Optional: show validator errors (kept short)
    demo_validators()

if __name__ == "__main__":
    main()
