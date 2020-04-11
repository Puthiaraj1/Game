class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have any end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self._title = []

    def add_tag(self, name, contents):
        title_tag = Tag(name, contents)
        self._title.append(title_tag)

    def display(self, file=None):
        for tag in self._title:
            self.contents += str(tag)

        super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def add_title(self, name, contents):
        self._head.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc()
    # my_page.add_title('title', 'Test html')
    # my_page.add_tag('h1', 'Main Heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    # with open("test.html", 'w') as test_doc:
    #     my_page.display(file=test_doc)


    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instance"
                        " of object to build up another object")
    new_body.add_tag('p',"The composed object doesn't actually own the objects that its composed of "
                     " - if its destroyed , those objects continue to exist.")
    new_doc_type = DocType()
    new_header = Head()
    new_header.add_tag('title',"Aggregation documemnt")
    my_page = HtmlDoc(new_doc_type,new_header, new_body)
# give our document new content by switching its body
my_page._body = new_body
with open("test_agg.html", 'w') as test_doc:
    my_page.display(file=test_doc)







