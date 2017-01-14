import boilerpipe
from boilerpipe.extract import Extractor
extractor = Extractor(extractor='ArticleExtractor', url="https://www.wittyfeed.com/story/24368/11-Sizzling-Photos-Of-Katrina-Kaifs-Modeling-Days-Will-Make-You-Cry-For-More?article_type=IA")

extracted_text = extractor.getText()

extracted_html = extractor.getHTML()

print(extracted_text)