class Thread:
    def __init__(self, title, date, posts):
        self.title = title
        self.date = date
        self.posts = posts


    def add_post(self, post):
        self.posts.append(post)

    def display_thread(self):
        print(f"Title: {self.title}, Date: {self.date}, Posts: {self.posts}")


class Post:
    def __init__(self, content, date, user, thread):
        self.content = content
        self.date = date
        self.user = user
        self.thread = thread

    def display_post(self):
        print(f"Content: {self.content}, Date: {self.date}, User: {self.user}")


class ImagePost(Post):
    def __init__(self):
        self.image = None

    def attach_image(self, image):
        self.image = image


class File:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size


class Image(File):
    def __init__(self, url):
        self.url = url


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        return False

    def logout(self):
        self.email = None
        self.password = None

    def add_post(self, post, thread):
        post.user = self
        post.thread = thread

    def attach_file_to_post(self, post, file):
        post.attach_file(file)

    def create_thread(self, title, date):
        thread = Thread(title, date, [])
        return thread

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"


class Moderator(User):
    def __init__(self):
        self.is_moderator = True

    def edit_post(self, post, content):
        post.content = content

    def delete_post(self, post):
        post.content = None
        post.date = None
        post.user = None
        post.image = None
        post.file = None
        post.size = None
