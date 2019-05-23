class hw:
    def hello_world(self, msg="world"):
        '''
        いわゆるHelloWorld
        >>> d = hw()
        >>> d.hello_world()
        'Hello, world'
        >>> d = hw()
        >>> d.hello_world("hoge")
        'Hello, hoge'
        '''
        return "Hello, " + msg

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
