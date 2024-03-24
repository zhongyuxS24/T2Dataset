from langdetect import detect, DetectorFactory

# 设置随机种子以获得重复性的结果
DetectorFactory.seed = 0

def detect_language(text):
    try:
        return detect(text) == 'en'
    except Exception as e:
        return "Error: " + str(e)

# 示例文本
text_en = "This is an English text."
text_fr = "Fh d Fcfatgv"
text_jp = "これは日本語のテキストです。"

# 语言检测
print(f"Text: '{text_en}' is in {detect_language(text_en)}")
print(f"Text: '{text_fr}' is in {detect_language(text_fr)}")
print(f"Text: '{text_jp}' is in {detect_language(text_jp)}")
