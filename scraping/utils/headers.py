import random

HEADERS_LIST = [
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.78 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6395.0 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6443.61 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/125.0.2535.92 Chrome/125.0.6422.78 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/125.0.2535.85 Chrome/125.0.6395.0 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/125.0.2542.25 Chrome/126.0.6443.0 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6484.20 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6312.86 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/124.0.2478.80 Chrome/124.0.6367.78 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 13_4; M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.78 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 14_0; M2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 13_5_2; M1 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6395.0 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 14_1; M2 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6443.20 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 14_2; M3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 14_3; M3 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6443.20 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 15_0; M4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 15_1; M4 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6484.20 Safari/537.36"},
  {"User-Agent": "Mozilla/5.0 (Macintosh; arm64; Mac OS X 14_4; M2 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6443.0 Safari/537.36"},
]

def get_random_headers():
  return random.choice(HEADERS_LIST)
