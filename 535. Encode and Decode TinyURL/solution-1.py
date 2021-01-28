class Codec:
    def __init__(self):
        self.hashMap = {}
        self.counter = 0
        
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = str(self.counter)
        self.hashMap[key] = longUrl
        self.counter += 1
        return "http://tinyurl.com/" + key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split("http://tinyurl.com/")[1]
        return self.hashMap[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))