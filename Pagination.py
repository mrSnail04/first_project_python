class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_page = 1 if not self.items else (len(self.items) // self.page_size + 1)
        self.current_page = 1

    def get_items(self):
        return self.items

    def get_current_page(self):
        return self.current_page

    def get_page_size(self):
        return self.page_size

    def prev_page(self):
        if self.current_page == 1:
            return self
        self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page == self.total_page:
            return self
        self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_page
        return self

    def go_to_page(self, page):
        if page > self.total_page:
            page = self.total_page
        elif page < 1:
            page = 1
        self.current_page = page
        return self

    def get_visible_items(self):
        start_index = (self.current_page - 1) * self.page_size
        finish_index = start_index + self.page_size
        return self.items[start_index:finish_index]

    def print_items(self):
        print(self.get_visible_items())


alphabetList = list('abcdefghijklmnopqrstuvwxyz')
p = Pagination(alphabetList)
p.print_items()
p.next_page()
p.print_items()
p.last_page()
p.print_items()
p.first_page()
p.print_items()
p.go_to_page(3)
p.print_items()
