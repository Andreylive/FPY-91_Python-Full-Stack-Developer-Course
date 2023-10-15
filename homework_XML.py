import collections
import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    tree = ET.parse(file_path)
    root = tree.getroot()
    news_list = root.findall("channel/item/description")
    word_list_all = []

    for news in news_list:
        word_list = news.text.split(' ')
        word_list_all += [word for word in word_list if len(word) > word_max_len]

    count_frequency_dict = dict(collections.Counter(word_list_all))
    sorted_frequency_dict = sorted(count_frequency_dict.items(), key=lambda x: x[1], reverse=True)

    most_frequent_word_list = []

    for element in sorted_frequency_dict[:top_words_amt]:
        most_frequent_word_list.append(element[0])

    print(most_frequent_word_list)
    return most_frequent_word_list


read_xml("newsafr.xml")
