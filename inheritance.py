from abc import ABC


class Thread:
    def __init__(self, title, date, posts):
        self.title = title
        self.date = date
        self.posts = posts

    def add_post(self, post):
        self.posts.append(post)

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")


class Post:
    def __init__(self, content, date, user, thread, file):
        self.content = content
        self.date = date
        self.user = user
        self.thread = thread
        self.file = file

    def display_post(self):
        print(f"Content: {self.content}, Date: {self.date}, User: {self.user}")


class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        pass


class ImageFile(File):
    """Fichier image."""

    def display(self):
        """Affiche l'image."""
        print(f"Fichier image '{self.name}'.")


class FilePost(Post):
    def __init__(self, user, time_posted, content, file, thread):
        super().__init__(user, time_posted, content, thread, file)

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display_post()
        print("pièce jointe:")
        self.file.display()


class Image(FilePost):
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

    def add_post(self, post, file, thread):
        if file:
            post = FilePost(
                user=self, time_posted="aujourd'hui", content=post, file=file
            )
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=post)
        thread.add_post(post)
        return post

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

    def delete_post(self, thread, post):
        index = thread.posts.index(post)
        del thread.posts[index]
