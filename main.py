from xmlrpc.client import ServerProxy

worker1 = ServerProxy('http://localhost:3001')
worker2 = ServerProxy('http://localhost:3002')
worker3 = ServerProxy('http://localhost:3003')

if __name__ == "__main__":
    print("Running main node")

    print("Calling wordcount on worker1")
    word_count_1 = worker1.wordcount()
    print("Received results from worker1")

    print("Calling wordcount on worker2")
    word_count_2 = worker2.wordcount()
    print("Received results from worker2")

    print("Calling wordcount on worker3")
    word_count_3 = worker3.wordcount()
    print("Received results from worker3")

    print("Merging results")
    word_count = {}
    word_count.update(word_count_1)
    word_count.update(word_count_2)
    word_count.update(word_count_3)

    print("Results:")
    for word, count in word_count.items():
        print(f"{word}:{count}")
