from Bullshit import Bullshit

if __name__ == "__main__":
    topic = input("請輸入主題: ")
    min_length = input("請輸入最少字數: ")
    obj = Bullshit()
    print(obj.generate(topic,min_length))