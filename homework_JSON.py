import json
import collections


def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path, encoding="utf8") as f:
        json_data = json.load(f)

    news_list = json_data["rss"]["channel"]["items"]
    word_list_all = []

    for row in news_list:
        words_list_temp = []
        text = row["description"]
        text_list = text.split(' ')
        for word in text_list:
            if len(word) > word_max_len:
                words_list_temp.append(word)
        word_list_all += words_list_temp

    count_frequency_dict = dict(collections.Counter(word_list_all))
    sorted_frequency_dict = sorted(count_frequency_dict.items(), key=lambda x: x[1], reverse=True)

    most_frequent_word_list = []
    for element in sorted_frequency_dict[:top_words_amt]:
        most_frequent_word_list.append(element[0])

    return most_frequent_word_list


read_json("newsafr.json")
