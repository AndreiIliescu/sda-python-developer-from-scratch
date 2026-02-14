class BlogPostHistory:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def save(self):
        with open('posts.txt', 'a') as f:
            data = f'-{self.title},{self.desc}'
            f.write(data)

    def change_title(self, new_title):
        self.title = new_title
        try:
            self.save()
        except OSError:
            raise Exception('BlogPostHistory cannot save!')

    def change_desc(self, new_desc):
        self.desc = new_desc
        try:
            self.save()
        except OSError:
            raise Exception('BlogPostHistory cannot save!')

    def get_properties(self):
        return self.title, self.desc

if __name__ == "__main__":
    b = BlogPostHistory('Title1', 'Desc1')
    b.save()
    b.change_title('Food blog')
    b.change_desc('A blog about food.')
