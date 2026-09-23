class Codec:
    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}
        self.base_url = "http://tinyurl.com/"
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        else:
            code = "".join(choices(self.alphabet, k=6))
            shortenedUrl = self.base_url + code
            self.short_to_long[shortenedUrl] = longUrl
            self.long_to_short[longUrl] = shortenedUrl
            return self.long_to_short[longUrl]

    def decode(self, shortUrl: str) -> str:
        if shortUrl not in self.short_to_long:
            return "ShortUrl does not exist"
        else:
            return self.short_to_long[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))