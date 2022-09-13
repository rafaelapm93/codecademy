import utils
import sorts

def main():
    bookshelf = utils.load_books(r'book_large.csv')

    for book in bookshelf:
        print(book['title'])

        book['author_lower'] = book['author'].lower()
        book['title_lower'] = book['title'].lower()

    print(ord("a"))
    print(ord(" "))
    print(ord("A"))

    def by_title_ascending(book_a, book_b):
        if book_a['title_lower'] > book_b['title_lower']:
            return True
        else:
            return False

    
    def by_total_length(book_a, book_b):
        return len(book_a['title'] + book_a['author']) > len(book_b['title'] + book_b['author']) 

    def by_author_ascending(book_a, book_b):
        if book_a['author_lower'] > book_b['author_lower']:
            return True
        else:
            return False

    sort_1 = sorts.bubble_sort(bookshelf,by_total_length )

    for book in sort_1:
        print(book['title'])

    

    bookshelf_v1 = bookshelf.copy()

    sort_2 = sorts.bubble_sort(bookshelf_v1,by_total_length)

    for book in sort_2:
        print(book['author'])

    bookshelf_v2 = bookshelf.copy()

    sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

    for book in bookshelf_v2:
        print(book['author'])




if __name__ == '__main__':
    main()