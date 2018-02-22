import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/699991.txt"
text_in_file = requests.get(url=url).text
while not text_in_file.startswith("We"):
    new_url = "https://stepic.org/media/attachments/course67/3.6.3/{0}".format(text_in_file)
    text_in_file = requests.get(url=new_url).text
with open("new_txt_file.txt", "w") as file:
    file.write(text_in_file)