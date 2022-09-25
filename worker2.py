from xmlrpc.server import SimpleXMLRPCServer

worker_no = 2
hostname = "localhost"
port = 3002

server = SimpleXMLRPCServer((hostname, port), logRequests=False)


def wordcount():
    print(f"Running wordcount on file {worker_no}.txt")
    word_file = open(f'{worker_no}.txt')

    word_count = {}

    for word in word_file.read().splitlines():
        word = word.lower()
        count = word_count.get(word, 0)
        word_count[word] = count + 1
    
    print("Results:")
    for word, count in word_count.items():
        print(f"{word}:{count}")

    return word_count

server.register_function(wordcount)

if __name__ == '__main__':
    try:
        print(f"Starting worker{worker_no} on port {port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"Exiting worker{worker_no}")