class Author:
    _all_authors = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self._articles = []
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        unique_categories = {article.magazine.category for article in self._articles}
        return list(unique_categories) if unique_categories else None  # Return None if empty

    @classmethod
    def all(cls):
        return cls._all_authors


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None  # Return None if no articles

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None  # Return None if no qualifying authors

    @classmethod
    def all(cls):
        return cls._all_magazines

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda m: len(m._articles))


class Article:
    all = []  # class attribute list of all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")

        self.author = author
        self.magazine = magazine

        self._title = None
        self.title = title

        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)  # add to class list

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if self._title is not None:
            raise AttributeError("Cannot change title once set.")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value
